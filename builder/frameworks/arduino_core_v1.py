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

env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()
build_mcu = env.get("BOARD_MCU", board.get("build.mcu", ""))

FRAMEWORK_DIR = platform.get_package_dir("framework-arduinoapollo3")
assert isdir(FRAMEWORK_DIR)

CORE_DIR = join(FRAMEWORK_DIR, "cores", "arduino")
SDK_DIR = join(CORE_DIR, "am_sdk_ap3")
CMSIS_DIR = join(SDK_DIR, "CMSIS")
THIRD_PARTY_DIR = join(SDK_DIR, "third_party")
EXACTLE_DIR = join(THIRD_PARTY_DIR, "exactle")
LIBRARY_DIR = join(FRAMEWORK_DIR, "libraries")

VARIANTS_DIR = join(FRAMEWORK_DIR, "variants")
BOARD_VARIANTS_DIR = join(VARIANTS_DIR, board.get("build.variant"))

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
        "-std=gnu++11",
        "-fno-threadsafe-statics",
        "-fno-rtti",
    ],

    CPPDEFINES=[
        ("F_CPU", "$BOARD_F_CPU"),
        ("ARDUINO", "10809"),
    ],

    CPPPATH=[
        join(BOARD_VARIANTS_DIR, "config"),
        join(BOARD_VARIANTS_DIR, "bsp"),
        join(CORE_DIR, "ard_sup"),
        join(CORE_DIR, "ard_sup", "ard_supers"),
        join(CORE_DIR),
        join(VARIANTS_DIR, board.get("build.variant")),
        join(SDK_DIR, "mcu", "apollo3"),
        join(SDK_DIR, "mcu", "apollo3", "hal"),
        join(SDK_DIR, "mcu", "apollo3", "regs"),
        join(SDK_DIR, "utils"),
        join(SDK_DIR, "devices"),
        join(CMSIS_DIR, "AmbiqMicro", "Include"),
        join(CMSIS_DIR, "ARM", "Include"),
        join(THIRD_PARTY_DIR, "uecc", "micro-ecc"),
        join(EXACTLE_DIR, "sw", "hci", "ambiq"),
        join(EXACTLE_DIR, "sw", "hci", "include"),
        join(EXACTLE_DIR, "sw", "hci", "ambiq", "apollo3"),
        join(EXACTLE_DIR, "sw", "apps", "app"),
        join(EXACTLE_DIR, "sw", "apps", "app", "include"),
        join(EXACTLE_DIR, "sw", "services"),
        join(EXACTLE_DIR, "sw", "stack", "hci"),
        join(EXACTLE_DIR, "sw", "stack", "cfg"),
        join(EXACTLE_DIR, "sw", "sec", "include"),
        join(EXACTLE_DIR, "sw", "sec", "common"),
        join(EXACTLE_DIR, "sw", "services"),
        join(EXACTLE_DIR, "ws-core", "include"),
        join(EXACTLE_DIR, "ws-core", "sw", "util"),
        join(EXACTLE_DIR, "ws-core", "sw", "wsf", "ambiq"),
        join(EXACTLE_DIR, "ws-core", "sw", "wsf", "include"),
        join(EXACTLE_DIR, "sw", "stack", "include"),
        join(EXACTLE_DIR, "sw", "profiles"),
        join(EXACTLE_DIR, "sw", "profiles", "gatt"),
        join(EXACTLE_DIR, "sw", "profiles", "gap"),

        join(LIBRARY_DIR, "EEPROM", "src"),
        join(LIBRARY_DIR, "PDM", "src"),
        join(LIBRARY_DIR, "RTC", "src"),
        join(LIBRARY_DIR, "Servo", "src"),
        join(LIBRARY_DIR, "SoftwareSerial", "src"),
        join(LIBRARY_DIR, "SPI", "src"),
        join(LIBRARY_DIR, "Wire", "src"),

    ],

    LINKFLAGS=[
        "-T%s" % join(VARIANTS_DIR, board.get("build.variant"), "linker_scripts", "gcc", board.get("build.linker_script")),
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
        join(VARIANTS_DIR, board.get("build.variant")),
        join(CMSIS_DIR, "ARM", "Lib", "ARM")
    ]
)

libs = []

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "FrameworkArduino"),
    join(CORE_DIR, "ard_sup"),

))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "apollo3_sdk_mcu"),
    join(SDK_DIR, "mcu"),
    # join(SDK_DIR, "devices")]
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

# Libraries
libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "EEPROM"),
    join(LIBRARY_DIR, "EEPROM", "src"),
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "PDM"),
    join(LIBRARY_DIR, "PDM", "src"),
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "RTC"),
    join(LIBRARY_DIR, "RTC", "src"),
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "Servo"),
    join(LIBRARY_DIR, "Servo", "src"),
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "SoftwareSerial"),
    join(LIBRARY_DIR, "SoftwareSerial", "src"),
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "SPI"),
    join(LIBRARY_DIR, "SPI", "src"),
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "Wire"),
    join(LIBRARY_DIR, "Wire", "src"),
))

env.Prepend(LIBS=libs)
