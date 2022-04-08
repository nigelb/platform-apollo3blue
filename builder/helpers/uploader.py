# platform-apollo3blue: Apollo3Blue development platform for platformio.
# Copyright 2019-present NigelB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from SCons.Script import DefaultEnvironment
from os.path import join, isdir
import os

def get_valid_upload_speed(upload_protocol, upload_speed):
    valid_bauds = dict(
        svl = ["57600", "115200", "230400", "460800", "921600"],
        asb = ["115200"]
    )
    default_bauds = dict(
        svl = "921600",
        asb = "115200"
    )
    if len(upload_speed) == 0 or upload_speed not in valid_bauds[upload_protocol]:
        if len(upload_speed) == 0:
            sys.stderr.write("No baud rate specified.")
        else:
            sys.stderr.write(
                "Error: Invalid {} baud rate specified: {}. \nSelect one of: {}\n".format(upload_protocol, upload_speed, valid_bauds[upload_protocol])
            )
        baud_rate = default_bauds[upload_protocol]
        sys.stderr.write("Using default {} baud rate of {}".format(upload_protocol, baud_rate))
        return baud_rate
    return upload_speed

# This lets us run the auto-port-detect to find an upload port
# just before we issue the upload command.
def BeforeUpload(target, source, env):
    upload_port = env.subst("$UPLOAD_PORT")
    upload_protocol = env.subst("$UPLOAD_PROTOCOL")
    if "jlink" not in upload_protocol and len(upload_port) == 0:
        env.AutodetectUploadPort()


def configure_upload(env):
    platform_apollo3blue = env.PioPlatform()
    currently_configured_board = env.BoardConfig()

    upload_flags = []
    upload_protocol = env.subst("$UPLOAD_PROTOCOL")
    upload_speed = env.subst("$UPLOAD_SPEED")
    if upload_protocol == "svl":
        upload_speed = get_valid_upload_speed(upload_protocol, upload_speed)
        upload_flags = ["$UPLOAD_PORT", "-b", "$UPLOAD_SPEED", "-f", "$SOURCES", "-v"],

    elif upload_protocol == "asb":
        upload_speed = get_valid_upload_speed(upload_protocol, upload_speed)
        upload_flags = [
                "--bin", "$SOURCES",
                "--load-address-blob", "0x20000",
                "--magic-num", "0xCB",
                "-o", "${SOURCES}.ASB",
                "--version", "0x0",
                "--load-address-wired", "$UPLOAD_ADDRESS",
                "-i", "6",
                "--options", "0x1",
                "-b", "$UPLOAD_SPEED",
                "-port", "$UPLOAD_PORT", "-r", "2", "-v"]

    elif upload_protocol.startswith("jlink"):
        # ------------------START------------------------
        # Code segment borrowed and modified from:
        # https://github.com/platformio/platform-atmelsam/blob/798b40a14807e2e9874b2f39c50b0b89781d29ae/builder/main.py#L179
        #
        # The original code (as well as this project) is distributed under
        # an Apache2.0 License: https://www.apache.org/licenses/LICENSE-2.0.html
        def __jlink_cmd_script(env, source):
            build_dir = env.subst("$BUILD_DIR")
            if not isdir(build_dir):
                os.makedirs(build_dir)
            script_path = join(build_dir, "upload.jlink")
            commands = [
                "h",
                "loadbin %s, %s" % (source, env.subst("$UPLOAD_ADDRESS")),
                "r",
                "q"
            ]
            with open(script_path, "w") as fp:
                fp.write("\n".join(commands))
            return script_path

        UPLOADER="JLinkExe"
        debug = currently_configured_board.get("debug", {})
        if env.subst("SYSTEM_TYPE") == "windows":
            UPLOADER="JLink.exe"
        upload_flags = [
            "-device", debug.get("jlink_device"),
            "-speed", env.GetProjectOption("debug_speed", "4000"),
            "-if", "swd",
            "-autoconnect", "1",
            "-CommanderScript", '"${__jlink_cmd_script(__env__, SOURCE)}"'
        ]
        env.Replace(
            __jlink_cmd_script=__jlink_cmd_script,
            UPLOADER=join(platform_apollo3blue.get_package_dir("tool-jlink"), UPLOADER)
        )
        # -------------------END-------------------------


    else:
        sys.stderr.write("Error: Unknown Upload Protocol: {}. \nSelect one of: {}\n".format(
            upload_protocol,
            currently_configured_board.get("upload.protocols")))
        env.Exit(1)

    env.Replace(
        UPLOADERFLAGS=upload_flags,
        UPLOAD_SPEED=upload_speed,
    )

env = DefaultEnvironment()
configure_upload(env)
upload_actions = [
    env.VerboseAction(BeforeUpload, "Looking for upload port..."),
    env.VerboseAction("$UPLOADCMD", "Uploading $SOURCE"),
]
#
# Target: Upload firmware
#
upload = env.AddPlatformTarget("upload", env['TARGET_BIN'], upload_actions, "Upload")
