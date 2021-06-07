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
from os.path import join, isdir
from SCons.Script import AlwaysBuild, Builder, Default, DefaultEnvironment
import platform as sys_pf

env = DefaultEnvironment()
platform = env.PioPlatform()

upload_protocol = env.subst("$UPLOAD_PROTOCOL")
FRAMEWORK_DIR = platform.get_package_dir("framework-arduinoapollo3")
assert isdir(FRAMEWORK_DIR)


upload_port = env.subst("$UPLOAD_PORT")
if len(upload_port) == 0:
    env.AutodetectUploadPort()

system_type = sys_pf.system().lower()
if system_type in ["darwin"]:
    system_type = "macosx"

upload_program = join(FRAMEWORK_DIR, "tools", "uploaders", upload_protocol, "dist", system_type, upload_protocol)
if  system_type == "windows":
    upload_program += ".exe"

if upload_protocol == "svl":
    upload_speed = env.subst("$UPLOAD_SPEED")
    if len(upload_speed) == 0:
        upload_speed = "921600"

    valid_svl_baud = ["57600", "115200", "230400", "460800", "921600"]

    if upload_speed not in valid_svl_baud:
        sys.stderr.write(
            "Error: Invalid SVL baud rate specified: {}. \r\nSelect one of: {}\r\n".format(upload_speed, valid_svl_baud)
        )
        env.Exit(1)
        

    uploader_flags=[
        "$UPLOAD_PORT",
        "-b", upload_speed,
        "-f", "$SOURCES",
        "-v",
    ]

elif upload_protocol == "asb":
    upload_speed = env.subst("$UPLOAD_SPEED")
    if len(upload_speed) == 0:
        upload_speed = "115200"

    valid_asb_baud = ["115200"]

    if upload_speed not in valid_asb_baud:
        sys.stderr.write(
            "Error: Invalid ASB baud rate specified: {}. \r\n Select one of: {}\r\n".format(upload_speed, valid_asb_baud)
        )
        env.Exit(1)

    uploader_flags=[
        "--bin", "$SOURCES",
        "--load-address-blob", "0x20000", 
        "--magic-num", "0xCB", 
        "-o", "${SOURCES}",
        "--version", "0x0", 
        "--load-address-wired", "0xC000", 
        "-i", "6", 
        "--options", "0x1", 
        "-b", upload_speed, 
        "-port", "$UPLOAD_PORT", "-r", "2", "-v"
    ]

    
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

    UPLOADER=upload_program,
    UPLOADERFLAGS=uploader_flags,
    UPLOADCMD="$UPLOADER $UPLOADERFLAGS"
)

env.Append(
    ARFLAGS=[],
    ASFLAGS=[],
    CCFLAGS=[],
    CXXFLAGS=[],
    LINKFLAGS=[],
    CPPDEFINES=[ "ARDUINO_ARCH_APOLLO3"],
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
upload = env.Alias(["upload"], target_bin, "$UPLOADCMD")
AlwaysBuild(upload)

#
# Target: Define targets
#
Default(target_bin)
