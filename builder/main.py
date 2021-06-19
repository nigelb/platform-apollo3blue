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
import os
from os.path import join, isdir
from SCons.Script import AlwaysBuild, Builder, Default, DefaultEnvironment
from platform import system
from platformio.project.config import ProjectOptions

env = DefaultEnvironment()

# The Apollo3bluePlatform object from this projects platform.py file.
platform_apollo3blue = env.PioPlatform()

currently_configured_board = env.BoardConfig()

# The project configuration, derived from the projects platform.ini file.
project_config = env.GetProjectConfig()

# A list of all of the specified build targets
all_build_targets = BUILD_TARGETS

# The currently building build target
build_type = env.GetBuildType()

# The env:<NAME> from the projects platformio.ini file
build_environment = env["PIOENV"]

# The options specified in the `build_environment` section of the platform.ini file.
options = env.GetProjectOptions()

# I have found that using the debug_build_flags defaults of
# ["-Og", "-g2", "-ggdb2"] produces some serious
# "Spooky Action At A Distance", specifically the "-Og" flag.
# It seems to happen when calling functions in libmbed-os.a,
# which has not been compiled with the "-Og". So we clear
# out the default values of debug_build_flags and set it to "-g".
debug_build_flags = ProjectOptions.get("env.debug_build_flags")
debug_build_flags.default.clear()
debug_build_flags.default.append("-g")


# This lets us run the auto-port-detect to find an upload port
# just before we issue the upload command.
def BeforeUpload(target, source, env):
    upload_port = env.subst("$UPLOAD_PORT")
    if len(upload_port) == 0:
        env.AutodetectUploadPort()


upload_actions = [
    env.VerboseAction(BeforeUpload, "Looking for upload port..."),
    env.VerboseAction("$UPLOADCMD", "Uploading $SOURCE"),
]

upload_flags = []
upload_protocol = env.subst("$UPLOAD_PROTOCOL")
upload_speed = env.subst("$UPLOAD_SPEED")
if upload_protocol == "svl":
    if len(upload_speed) == 0:
        upload_speed = "921600"

    valid_svl_baud = ["57600", "115200", "230400", "460800", "921600"]

    if upload_speed not in valid_svl_baud:
        sys.stderr.write(
            "Error: Invalid SVL baud rate specified: {}. \nSelect one of: {}\n".format(upload_speed, valid_svl_baud)
        )
        env.Exit(1)
    upload_flags = ["$UPLOAD_PORT", "-b", "$UPLOAD_SPEED", "-f", "$SOURCES", "-v"],

elif upload_protocol == "asb":
    upload_speed = env.subst("$UPLOAD_SPEED")
    if len(upload_speed) == 0:
        upload_speed = "115200"

    valid_asb_baud = ["115200"]

    if upload_speed not in valid_asb_baud:
        sys.stderr.write(
            "Error: Invalid ASB baud rate specified: {}. \n Select one of: {}\n".format(upload_speed,
                                                                                        valid_asb_baud)
        )
        env.Exit(1)
    upload_flags = [
            "--bin", "$SOURCES",
            "--load-address-blob", "0x20000",
            "--magic-num", "0xCB",
            "-o", "${SOURCES}.ASB",
            "--version", "0x0",
            "--load-address-wired", "0xC000",
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
            "loadbin %s, %s" % (source, currently_configured_board.get(
                "upload.jlink_offset_address")),
            "r",
            "q"
        ]
        with open(script_path, "w") as fp:
            fp.write("\n".join(commands))
        return script_path

    UPLOADER="JLinkExe"
    debug = currently_configured_board.get("debug", {})
    if system() == "Windows":
        UPLOADER+=".exe"
    upload_flags = [
        "-device", debug.get("jlink_device"),
        "-speed", "4000",
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


# A full list with the available variables
# http://www.scons.org/doc/production/HTML/scons-user.html#app-variables
env.Replace(
    AR="arm-none-eabi-ar",
    AS="arm-none-eabi-as",
    CC="arm-none-eabi-gcc",
    CXX="arm-none-eabi-g++",
    GDB="arm-none-eabi-gdb",
    OBJCOPY="arm-none-eabi-objcopy",
    RANLIB="arm-none-eabi-ranlib",
    SIZETOOL="arm-none-eabi-size",

    ARFLAGS=["rc"],
    UPLOADERFLAGS = upload_flags,
    UPLOAD_SPEED=upload_speed,
    UPLOADCMD="$UPLOADER $UPLOADERFLAGS"
)

env.Append(
    ARFLAGS=[],
    ASFLAGS=[],
    CCFLAGS=[],
    CXXFLAGS=[],
    LINKFLAGS=[],
    CPPDEFINES=[],
    LIBS=[],
    BUILDERS=dict(
        ElfToBin=Builder(
            action=" ".join([
                "$OBJCOPY",
                "-O",
                "binary",
                "$SOURCES",
                "$TARGET"]),
            suffix=".bin"
        )
    )
)

#
# Target: Build executable and linkable firmware
#
target_elf = env.BuildProgram()

#
# Target: Build the .bin file
#
target_bin = env.ElfToBin(join("$BUILD_DIR", "firmware"), target_elf)

#
# Target: Upload firmware
#
upload = env.AddPlatformTarget("upload", target_bin, upload_actions, "Upload")
#
# Target: Define targets
#
Default([target_bin, upload])
