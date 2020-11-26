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

BASE_CORE_DIR = join(FRAMEWORK_DIR, "cores")
CORE_DIR = join(BASE_CORE_DIR, "arduino")
MBED_DIR = join(FRAMEWORK_DIR, "cores", "mbed-os")
BRIDGE_DIR = join(CORE_DIR, "mbed-bridge") 
TARGETS_DIR = join(MBED_DIR, "targets", "TARGET_Ambiq_Micro", "TARGET_Apollo3")
SDK_DIR    = join(TARGETS_DIR, "sdk")
SDK_TARGETS_DIR = join(MBED_DIR, "targets", "TARGET_Ambiq_Micro", "sdk")
CMSIS_DIR = join(SDK_DIR, "CMSIS") 

LIBRARY_DIR = join(FRAMEWORK_DIR, "libraries")

VARIANTS_DIR = join(FRAMEWORK_DIR, "variants")
BOARD_VARIANTS_DIR = join(VARIANTS_DIR, board.get("build.variant").replace("TARGET_", "", 1))
BOARD_TARGET_DIR = join(TARGETS_DIR, board.get("build.variant"))


TOOLS_DIR = join(FRAMEWORK_DIR, "tools")

env.Append(
    ASFLAGS=[
        "-c", "-g", "-MMD",
        "-x", "assembler-with-cpp",

    ],

    CFLAGS=[
        "-include", join(BOARD_VARIANTS_DIR, "mbed", "mbed_config.h"),
        "-include", join(CORE_DIR, "sdk", "ArduinoSDK.h"),
        "-iprefix{}/".format(BASE_CORE_DIR),
        join("@{}".format(BOARD_VARIANTS_DIR), "mbed", ".c-flags"),
        join("@{}".format(BOARD_VARIANTS_DIR), "mbed", ".includes"),
        join("@{}".format(BOARD_VARIANTS_DIR), "mbed", ".c-symbols"),
    ],

    CPPFLAGS=[
    ],

    CXXFLAGS=[
        "-include", join(BOARD_VARIANTS_DIR, "mbed", "mbed_config.h"),
        "-include", join(CORE_DIR, "sdk", "ArduinoSDK.h"),
        "-iprefix{}/".format(BASE_CORE_DIR),
        join("@{}".format(BOARD_VARIANTS_DIR), "mbed", ".cxx-flags"),
        join("@{}".format(BOARD_VARIANTS_DIR), "mbed", ".includes"),
        join("@{}".format(BOARD_VARIANTS_DIR), "mbed", ".cxx-symbols"),
    ],

    CPPDEFINES=[
        "MBED_NO_GLOBAL_USING_DIRECTIVE",
        ("ARDUINO", "10811"),
        "ARDUINO_ARCH_APOLLO3"
        "ARDUINO_ARCH_MBED",
        "ARDUINO_ARCH_APOLLO3",
        "MBED_NO_GLOBAL_USING_DIRECTIVE",
        "CORDIO_ZERO_COPY_HCI",
    ],
    CPPPATH=[
        CORE_DIR,
        BOARD_VARIANTS_DIR,
        BRIDGE_DIR,
        join(BRIDGE_DIR, "cort-api"),
##        MBED_DIR,
        #join(MBED_DIR, "cmsis", "TARGET_CORTEX_M"),
        #join(MBED_DIR, "hal"),
        #join(MBED_DIR, "rtos"),
        #join(MBED_DIR, "platform", "cxxsupport"),
        #join(BRIDGE_DIR, "core-api"),
        #join(TARGETS_DIR, "device"),
        #join(SDK_DIR, "mcu", "apollo3"),
        #join(CMSIS_DIR, "AmbiqMicro", "Include"),
##        BOARD_TARGET_DIR,
        #join(BOARD_TARGET_DIR, "bsp"),
        #join(SDK_DIR, "mcu", "apollo3"),
        #join(SDK_DIR, "mcu", "apollo3", "hal"),
        #join(SDK_DIR, "mcu", "apollo3", "regs"),
        #join(SDK_TARGETS_DIR, "utils"),
        #join(SDK_TARGETS_DIR, "devices"),

    ],

    LINKFLAGS=[
        "-T%s" % join(TOOLS_DIR, "uploaders", "asb", board.get("build.linker_script")),
        join("@{}".format(BOARD_VARIANTS_DIR), "mbed", ".ld-flags"),
        join("@{}".format(BOARD_VARIANTS_DIR), "mbed", ".ld-symbols"),
        ## "-Os",
        #"-mthumb",
        #"-mcpu=%s" % board.get("build.cpu"),
        #"-mfpu=fpv4-sp-d16",
        #"-mfloat-abi=hard",
        #"--specs=nano.specs",
        #"-mfloat-abi=hard",
        #"-nostdlib",
        #"-fno-exceptions",
        #"-static",
        #"-Wl,--gc-sections,--entry,Reset_Handler",
        #"-Wl,--check-sections",
        #"-Wl,--unresolved-symbols=report-all",
        #"-Wl,--warn-common",
        #"-Wl,--warn-section-align",

        "-Wl,-Map=%s" % join("$BUILD_DIR", "program.map")
    ],

    #LIBS=["m", "arm_cortexM4lf_math", "gcc", "stdc++", "nosys", "c", "libmbed-os.a"],
    LIBS=["stdc++", "supc++", "libmbed-os.a"],

    LIBPATH=[
        join(BOARD_VARIANTS_DIR, "mbed"),
        join(CMSIS_DIR, "ARM", "Lib", "ARM")
    ]
)

libs = []

print("------------------->", BRIDGE_DIR)
print("------------------->", env)

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "varient"),
    BOARD_VARIANTS_DIR
    #BRIDGE_DIR,
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "mbed_bridge"),
    BRIDGE_DIR,
))

#
#libs.append(env.BuildLibrary(
#    join("$BUILD_DIR", "apollo3_sdk_mcu"),
#    join(SDK_DIR, "mcu"),
#    # join(SDK_DIR, "devices")]
#))
#
#libs.append(env.BuildLibrary(
#    join("$BUILD_DIR", "apollo3_sdk_devices"),
#    join(SDK_DIR, "devices"),
#))
#
#libs.append(env.BuildLibrary(
#    join("$BUILD_DIR", "apollo3_sdk_utils"),
#    join(SDK_DIR, "utils"),
#))
#
#libs.append(env.BuildLibrary(
#    join("$BUILD_DIR", "variant"),
#    join(BOARD_VARIANTS_DIR),
#
#))

# Libraries
#libs.append(env.BuildLibrary(
#    join("$BUILD_DIR", "EEPROM"),
#    join(LIBRARY_DIR, "EEPROM", "src"),
#))

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
