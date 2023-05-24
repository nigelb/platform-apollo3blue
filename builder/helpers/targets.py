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
import os

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
    platform_apollo3blue = env.PioPlatform()
    jlink_path = platform_apollo3blue.get_package_dir("tool-jlink")
    if jlink_path is None:
        return
    currently_configured_board = env.BoardConfig()
    program = "JLinkSWOViewerCLExe"
    if env.subst("SYSTEM_TYPE") == "windows":
        program = "JLinkSWOViewerCLExe.exe"

    program = join(jlink_path, program)
    debug = currently_configured_board.get("debug", {})
    swo_flags = [
            "-device", debug.get("jlink_device"),
            "-itmport", "0",
            "-swofreq", debug.get("swo_freq", 1000000)
    ]
    env.Replace(
        APOLLO3_SWO_PROGRAM=program,
        APOLLO3_SWO_FLAGS=swo_flags,
        APOLLO3_SWO_COMMAND="$APOLLO3_SWO_PROGRAM $APOLLO3_SWO_FLAGS")
    swo_actions = [env.VerboseAction("$APOLLO3_SWO_COMMAND", "Start the SEGGER Jlink SWO program."),]
    env.AddPlatformTarget("jlink_swo", None, swo_actions, "JLink SWO", "Start the SEGGER Jlink SWO program.")


def add_jlink_rtt(env):
    "JLinkRTTViewerExe --device AMA3B1KK-KBR -a -ti 1"
    platform_apollo3blue = env.PioPlatform()
    jlink_path = platform_apollo3blue.get_package_dir("tool-jlink")
    if jlink_path is None:
        return
    currently_configured_board = env.BoardConfig()
    program = "JLinkRTTViewerExe"
    if env.subst("SYSTEM_TYPE") == "windows":
        program = "JLinkRTTViewerExe.exe"

    program = join(jlink_path, program)
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

def ambiq_sdk_keys_message(env, framework_dir, keys_dir):

    print("For the Ambiq SDK CLI tools to work you need to create a `keys_info.py` file.", file=sys.stderr)
    print("The default location for keys_info.py is in the directory: {}. ".format(join("$PROJECT_DIR", "keys")), file=sys.stderr)
    print("""You can can change the location of the directory containing the keys_info.py file with 
    the `board_build.ota.keys_dir = <NEW_DIRECTORY>` option in your `platformio.ini` file.""", file=sys.stderr)
    print(file=sys.stderr)
    print("You can copy the example file from '{}' to '{}'".format(
        join(framework_dir, "tools", "apollo3_scripts", "keys_info0.py"), join(keys_dir, "keys_info.py")), file=sys.stderr)
    print(file=sys.stderr)

def add_ota_image(env):
    try:
        from Crypto.Cipher import AES
    except:
        env.Execute("$PYTHONEXE -m pip install pycryptodome")
    board = env.BoardConfig()

    platform_apollo3blue = env.PioPlatform()
    FRAMEWORK_DIR = platform_apollo3blue.get_package_dir("framework-ambiqsuitesdkapollo3-sfe")
    keys_dir = env.subst(board.get("build.ambiq_sdk.keys_dir", join("$PROJECT_DIR", "keys")))
    if not os.path.exists(keys_dir):
        print(file=sys.stderr)
        if not os.path.exists(keys_dir):
            print("The directory `{}` does not exist. ".format(keys_dir), file=sys.stderr)
            print(file=sys.stderr)
            ambiq_sdk_keys_message(env, FRAMEWORK_DIR, keys_dir)
            env.Exit(1)
        elif not os.path.exists(join(keys_dir, "keys_info.py")):

            ambiq_sdk_keys_message(env, FRAMEWORK_DIR, keys_dir)
            sys.stderr.write('Error: Board: "%s" not supported by Arduino_Apollo3-%s\n')
            env.Exit(1)


    env.Replace(
        APOLLO3_SECURITY_KEYS=keys_dir,
        APOLLO3_OTA_IMAGE_STAGE1=join("$BUILD_DIR", "ota_image_stage1"),
        APOLLO3_OTA_IMAGE_STAGE1_BIN=join("$BUILD_DIR", "ota_image_stage1.bin"),
        APOLLO3_OTA_IMAGE=join("$BUILD_DIR", "ota_image.bin"),
        APOLLO3_CUSTOM_IMAGE_PROGRAM=join(FRAMEWORK_DIR, "tools", "apollo3_scripts", "create_cust_image_blob.py"),
        APOLLO3_OTA_BINARY_PROGRAM=join(FRAMEWORK_DIR, "tools", "apollo3_amota", "scripts", "ota_binary_converter.py"),
        APOLLO3_CUSTOM_IMAGE_COMMAND="PYTHONPATH=$APOLLO3_SECURITY_KEYS $PYTHONEXE $APOLLO3_CUSTOM_IMAGE_PROGRAM --bin $SOURCE --load-address $UPLOAD_ADDRESS --magic-num 0xcb --version 0x0 -o $APOLLO3_OTA_IMAGE_STAGE1",
        APOLLO3_OTA_IMAGE_COMMAND="$PYTHONEXE $APOLLO3_OTA_BINARY_PROGRAM --appbin $APOLLO3_OTA_IMAGE_STAGE1_BIN -o $APOLLO3_OTA_IMAGE",
    )
    ota_image_actions = [
        env.VerboseAction("$APOLLO3_CUSTOM_IMAGE_COMMAND", "Custom Image."),
        env.VerboseAction("$APOLLO3_OTA_IMAGE_COMMAND", "OTA Image."),
    ]
    env.AddPlatformTarget("ble_ota_image", "$BUILD_DIR/firmware.bin", ota_image_actions, "BLE OTA", "Create a program image to be used by the OTA updater.")

# Removes IDE linting errors :-(
env = env

add_svl_bootloader(env)
add_jlink_swo(env)
add_jlink_rtt(env)
add_ota_image(env)
