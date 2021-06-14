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

from os.path import isdir, join
from SCons.Script import DefaultEnvironment
import platform as sys_pf


env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()
build_mcu = env.get("BOARD_MCU", board.get("build.mcu", ""))
framework_build = board.get("build.framework.ambiqsdk-sfe")

env.ProcessFlags(framework_build.get("extra_flags"))

FRAMEWORK_DIR        = platform.get_package_dir("framework-ambiqsuitesdkapollo3-sfe")
VARIANT_DIR          = join(FRAMEWORK_DIR, *framework_build.get("variant"))
CMSIS_DIR            = join(FRAMEWORK_DIR, "CMSIS")
ARM_CMSIS_DIR        = join(CMSIS_DIR, "ARM")
AMBIQMICRO_CMSIS_DIR = join(CMSIS_DIR, "AmbiqMicro")
DEVICES_DIR           = join(FRAMEWORK_DIR, "devices")
UTILS_DIR             = join(FRAMEWORK_DIR, "utils")
MCU_DIR               = join(FRAMEWORK_DIR, "mcu", board.get("build.part"))

TOOLS_DIR             = join(FRAMEWORK_DIR, "boards_sfe", "common", "tools_sfe")

system_type = sys_pf.system().lower() if sys_pf.system() != "Darwin" else "macosx"

upload_protocol = env.subst("$UPLOAD_PROTOCOL")
uploader = join(TOOLS_DIR, upload_protocol, "dist", system_type, upload_protocol)

if system_type == "windows":
    uploader += ".exe"

env.Replace(
    SIZEPROGREGEXP=r"^(?:\.text)\s+([0-9]+).*",
    SIZEDATAREGEXP=r"^(?:\.data|\.bss)\s+([0-9]+).*",
    SIZECHECKCMD="$SIZETOOL -A -d $SOURCES",
    UPLOADER=uploader,
)

env.Append(
    ASFLAGS=[
        "-c", "-g", "-MMD",
        "-x", "assembler-with-cpp",
    ],
    CFLAGS=[
        "-mthumb", "-mcpu=%s"%board.get("build.cpu"), "-mfpu=fpv4-sp-d16", "-mfloat-abi=%s"%board.get("build.fabi"),
        "-ffunction-sections", "-fdata-sections",
        "-MMD", "-MP", "-std=c99", "-Wall", "-g",
        "-O0",
        "-I{}".format(MCU_DIR),
        "-I{}/Include".format(ARM_CMSIS_DIR),
        "-I{}/Include".format(AMBIQMICRO_CMSIS_DIR),
        "-I{}/bsp".format(VARIANT_DIR),
        "-I{}".format(DEVICES_DIR),
        "-I{}".format(UTILS_DIR),
    ],
    CPPDEFINES=[
        "AM_PACKAGE_BGA",
        "AM_CUSTOM_BDADDR",
        "WSF_TRACE_ENABLED",
        "AM_DEBUG_PRINTF",
        "AM_PART_APOLLO3",
        "%s_PART"%board.get("build.part"),
    ],
    LINKFLAGS=[
        "-mthumb", "-mcpu=%s"%board.get("build.cpu"), "-mfpu=fpv4-sp-d16", "-mfloat-abi=%s"%board.get("build.fabi"),
        "-nostartfiles", "-static",
        "-Wl,--gc-sections,--entry,Reset_Handler,-Map,%s"% join("$BUILD_DIR", "program.map"),
        "-Wl,-T%s"%join(FRAMEWORK_DIR, "boards_sfe","common","tools_sfe", "templates", "asb_svl_linker.ld")
    ],
)

libs = []

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "Variant"),
    join(FRAMEWORK_DIR, *framework_build.get("variant")),
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "Hal"),
    join(FRAMEWORK_DIR, "mcu", board.get("build.part"), "hal"),
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "Devices"),
    DEVICES_DIR,
    "+<am_devices_led.c>"
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "Utils"),
    UTILS_DIR,
    "+<*> -<am_util_regdump.c>"
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "Entry"),
    join(FRAMEWORK_DIR, "boards_sfe", "common", "tools_sfe", "templates"),
    "+<startup_gcc.c>"
))

env.Prepend(LIBS=libs)

