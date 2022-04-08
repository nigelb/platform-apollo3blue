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

from SCons.Script import DefaultEnvironment, Import, BUILD_TARGETS
from os.path import join
import sys

Import("env")


def add_svl_bootloader(env):
    upload_port = env.subst("$UPLOAD_PORT")
    upload_protocol = env.subst("$UPLOAD_PROTOCOL")
    def BeforeUpload(target, source, env):
        if "jlink" not in upload_protocol and len(upload_port) == 0:
            env.AutodetectUploadPort()

    if 'svl_bootloader' in BUILD_TARGETS:
        env.Replace(UPLOAD_ADDRESS="0xC000")
        if upload_protocol == "svl":
            env.Replace(UPLOAD_PROTOCOL="asb")
            env.Replace(UPLOADER=env.subst("$ASB_UPLOADER"))
            env.Replace(UPLOAD_SPEED="115200")
    env.AddPlatformTarget("svl_bootloader", env.subst("$SVL_BOOTLOADER_BIN"),
                          [BeforeUpload, env.VerboseAction("$UPLOADCMD", "Uploading SVL Bootloader: $SOURCE")],
                          "Sparkfun SVL", "Upload the Sparkfun SVL Bootloader."
                          )


def add_jlink_swo(env):
    "JLinkSWOViewerCLExe -device AMA3B1KK-KBR -itmport 0"
    currently_configured_board = env.BoardConfig()
    program = "JLinkSWOViewerCLExe"
    if env.subst("SYSTEM_TYPE") == "windows":
        program = "JLinkSWOViewerCLExe.exe"
    platform_apollo3blue = env.PioPlatform()
    program = join(platform_apollo3blue.get_package_dir("tool-jlink"), program)
    debug = currently_configured_board.get("debug", {})
    swo_flags = [
            "-device", debug.get("jlink_device"),
            "-itmport", "0"
    ]
    env.Replace(
        APOLLO3_SWO_PROGRAM=program,
        APOLLO3_SWO_FLAGS=swo_flags,
        APOLLO3_SWO_COMMAND="$APOLLO3_SWO_PROGRAM $APOLLO3_SWO_FLAGS")
    swo_actions = [env.VerboseAction("$APOLLO3_SWO_COMMAND", "Start the SEGGER Jlink SWO program."),]
    env.AddPlatformTarget("jlink_swo", None, swo_actions, "JLink SWO", "Start the SEGGER Jlink SWO program.")


def add_jlink_rtt(env):
    "JLinkRTTViewerExe --device AMA3B1KK-KBR -a -ti 1"
    currently_configured_board = env.BoardConfig()
    program = "JLinkRTTViewerExe"
    if env.subst("SYSTEM_TYPE") == "windows":
        program = "JLinkRTTViewerExe.exe"
    platform_apollo3blue = env.PioPlatform()
    program = join(platform_apollo3blue.get_package_dir("tool-jlink"), program)
    debug = currently_configured_board.get("debug", {})
    swo_flags = [
            "--device", debug.get("jlink_device"),
            "-a", "-ti", "1"
    ]
    env.Replace(
        APOLLO3_RTT_PROGRAM=program,
        APOLLO3_RTT_FLAGS=swo_flags,
        APOLLO3_RTT_COMMAND="$APOLLO3_RTT_PROGRAM $APOLLO3_RTT_FLAGS")
    rtt_actions = [env.VerboseAction("$APOLLO3_RTT_COMMAND", "Start the SEGGER Jlink RTT program."),]
    env.AddPlatformTarget("jlink_rtt", None, rtt_actions, "JLink RTT", "Start the SEGGER Jlink RTT program.")


# Removes IDE linting errors :-(
env = env

add_svl_bootloader(env)
add_jlink_swo(env)
add_jlink_rtt(env)
