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

from os.path import isdir, join, exists
from SCons.Script import DefaultEnvironment
import sys

env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()
build_mcu = env.get("BOARD_MCU", board.get("build.mcu", ""))

env.ProcessFlags(board.get("build.framework.arduino.v2.extra_flags"))

FRAMEWORK_DIR = platform.get_package_dir("framework-arduinoapollo3")
assert isdir(FRAMEWORK_DIR)

CORE_DIR = join(FRAMEWORK_DIR, "cores", "arduino")
SDK_DIR = join(CORE_DIR, "am_sdk_ap3")
CMSIS_DIR = join(SDK_DIR, "CMSIS")
THIRD_PARTY_DIR = join(SDK_DIR, "third_party")
EXACTLE_DIR = join(THIRD_PARTY_DIR, "exactle")
LIBRARY_DIR = join(FRAMEWORK_DIR, "libraries")

VARIANTS_DIR = join(FRAMEWORK_DIR, "variants")
BOARD_VARIANTS_DIR = join(VARIANTS_DIR, board.get("build.framework.arduino.v1.variant"))

PROJECT_DIR = env.subst("$PROJECT_DIR")

upload_protocol = env.subst("$UPLOAD_PROTOCOL")

# =======================================================
# Linker Script
framework_linker_dir = join(VARIANTS_DIR, board.get("build.framework.arduino.v1.variant"), "linker_scripts", "gcc")

# =======================================================
# Bootloader location
env.Replace(SVL_BOOTLOADER_BIN=join(FRAMEWORK_DIR, "tools", "bootloaders", "artemis", "artemis_svl.bin"))
# =======================================================

# =======================================================
# Uploader Binary Locations
system_type = env.subst("$SYSTEM_TYPE")
env.Replace(SVL_UPLOADER=join(FRAMEWORK_DIR, "tools", "artemis", system_type, "artemis_svl"))
env.Replace(ASB_UPLOADER=join(FRAMEWORK_DIR, "tools", "ambiq", system_type, "ambiq_bin2board"))
# =======================================================

# =======================================================
# Linker Script Locations
env.Replace(SVL_LINKER_SCRIPT=join(framework_linker_dir, "artemis_sbl_svl_app.ld"))
env.Replace(ASB_LINKER_SCRIPT=join(framework_linker_dir, "ambiq_sbl_app.ld"))
# =======================================================

env.Append(
    ASFLAGS=[
        "-c", "-g", "-MMD",
        "-x", "assembler-with-cpp",
    ],

    CFLAGS=[
        "-std=gnu11",
        "--function-sections", "-mfpu=fpv4-sp-d16", "-Wall"
    ],

    CPPFLAGS=[
        "-c", "-g", "-MMD",
        "-mthumb",
        "-mfloat-abi=hard",
        "-fdata-sections",
        "-Os",
        "-ffunction-sections",
        "-nostdlib",
        "--param", "max-inline-insns-single=500",
        "-fno-exceptions",
        "-mcpu=%s" % board.get("build.cpu")
    ],

    CXXFLAGS=[
        "-include", "Arduino.h",
        "-std=gnu++11",
        "-fno-threadsafe-statics",
        "-fno-rtti",
    ],

    CPPDEFINES=[
        ("F_CPU", "$BOARD_F_CPU"),
        ("ARDUINO", "10809"),
        "AM_PACKAGE_BGA",
        "AM_PART_APOLLO3",
        "PART_apollo3"
    ],

    CPPPATH=[

        # core
        join(CORE_DIR, "ard_sup"),
        join(CORE_DIR, "ard_sup", "ard_supers"),
        join(CORE_DIR),

        # Varient
        join(VARIANTS_DIR, board.get("build.framework.arduino.v1.variant")),
        join(BOARD_VARIANTS_DIR, "config"),
        join(BOARD_VARIANTS_DIR, "bsp"),

        # ambiq_sdk
        join(SDK_DIR, "mcu", "apollo3"),
        join(SDK_DIR, "mcu", "apollo3", "hal"),
        join(SDK_DIR, "mcu", "apollo3", "regs"),
        join(SDK_DIR, "utils"),
        join(SDK_DIR, "devices"),

        # CMSIS
        join(CMSIS_DIR, "AmbiqMicro", "Include"),
        join(CMSIS_DIR, "ARM", "Include"),

    ],

    LINKFLAGS=[
        # "-Os",
        "-mthumb",
        "-mcpu=%s" % board.get("build.cpu"),
        "-mfpu=fpv4-sp-d16",
        "-mfloat-abi=hard",
        "--specs=nano.specs",
        "-mfloat-abi=hard",
        "-nostdlib",
        "-fno-exceptions",
        "-static",
        "-Wl,--gc-sections,--entry,Reset_Handler",
        "-Wl,--check-sections",
        "-Wl,--unresolved-symbols=report-all",
        "-Wl,--warn-common",
        "-Wl,--warn-section-align",

        "-Wl,-Map=%s" % join("$BUILD_DIR", "program.map")
    ],

    LIBS=["m", "arm_cortexM4lf_math", "gcc", "stdc++", "nosys", "c"],

    LIBPATH=[
        join(VARIANTS_DIR, board.get("build.framework.arduino.v1.variant")),
        join(CMSIS_DIR, "ARM", "Lib", "ARM")
    ],
    LIBSOURCE_DIRS=[LIBRARY_DIR]
)

libs = []

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "FrameworkArduino"),
    join(CORE_DIR, "ard_sup"),

))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "apollo3_sdk_mcu"),
    join(SDK_DIR, "mcu"),
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "apollo3_sdk_devices"),
    join(SDK_DIR, "devices"),
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "apollo3_sdk_utils"),
    join(SDK_DIR, "utils"),
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "variant"),
    join(BOARD_VARIANTS_DIR),

))

env.Prepend(LIBS=libs)
