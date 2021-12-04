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
import platform as system_platform

env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()
build_mcu = env.get("BOARD_MCU", board.get("build.mcu", ""))

env.ProcessFlags(board.get("build.framework.arduino.v2.extra_flags"))

FRAMEWORK_DIR = platform.get_package_dir("framework-arduinoapollo3")
assert isdir(FRAMEWORK_DIR)

BASE_CORE_DIR = join(FRAMEWORK_DIR, "cores")
CORE_DIR = join(BASE_CORE_DIR, "arduino")
BRIDGE_DIR = join(CORE_DIR, "mbed-bridge")
CMSIS_DIR = join(FRAMEWORK_DIR, "cores", "mbed-os", "targets", "TARGET_Ambiq_Micro", "TARGET_Apollo3", "sdk", "CMSIS")

LIBRARY_DIR = join(FRAMEWORK_DIR, "libraries")

VARIANTS_DIR = join(FRAMEWORK_DIR, "variants")
BOARD_VARIANTS_DIR = join(VARIANTS_DIR, board.get("build.framework.arduino.v2.variant").replace("TARGET_", "", 1))

linker_scripts = {
    "asb": "0xC000.ld",
    "svl": "0x10000.ld",
    "jlink": "0x10000.ld",
}
upload_protocol = env.subst("$UPLOAD_PROTOCOL")
linker_script = linker_scripts[upload_protocol]

if upload_protocol == "jlink": upload_protocol = "svl"

TOOLS_DIR = join(FRAMEWORK_DIR, "tools")

system_type = system_platform.system().lower() if system_platform.system() != "Darwin" else "macosx"
env.Replace(SVL_UPLOADER=join(FRAMEWORK_DIR, "tools", "uploaders", upload_protocol, "dist", system_type, "svl"))
env.Replace(ASB_UPLOADER=join(FRAMEWORK_DIR, "tools", "uploaders", upload_protocol, "dist", system_type, "asb"))

env.Append(
    ASFLAGS=[
        "-c", "-g", "-MMD",
        "-x", "assembler-with-cpp",
    ],

    CFLAGS=[
        "-MMD", 
        "-include", join(BOARD_VARIANTS_DIR, "mbed", "mbed_config.h"),
        "-iprefix{}/".format(BASE_CORE_DIR),
        join("@{}".format(BOARD_VARIANTS_DIR), "mbed", ".c-flags"),
        join("@{}".format(BOARD_VARIANTS_DIR), "mbed", ".includes"),
        join("@{}".format(BOARD_VARIANTS_DIR), "mbed", ".c-symbols"),
    ],

    CPPFLAGS=[
#        "-w", "-x", "c++", "-E", "-CC"
    ],

    CXXFLAGS=[
        "-MMD", 
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
        "ARDUINO_ARCH_APOLLO3",
        "ARDUINO_ARCH_MBED",
        "MBED_NO_GLOBAL_USING_DIRECTIVE",
        "CORDIO_ZERO_COPY_HCI",
    ] ,

    CPPPATH=[
        CORE_DIR,
        BOARD_VARIANTS_DIR,
        BRIDGE_DIR,
        join(BRIDGE_DIR, "core-api"),
        join(BRIDGE_DIR, "core-api", "api", "deprecated"),
    ],

    LINKFLAGS=[
        "-T%s" % join(TOOLS_DIR, "uploaders", upload_protocol, linker_script),
        join("@{}".format(BOARD_VARIANTS_DIR), "mbed", ".ld-flags"),
        join("@{}".format(BOARD_VARIANTS_DIR), "mbed", ".ld-symbols"),
        "-Wl,--whole-archive",
        join("{}".format(BOARD_VARIANTS_DIR), "mbed", "libmbed-os.a"),
        "-Wl,--no-whole-archive",
        "-Wl,-Map=%s" % join("$BUILD_DIR", "program.map"),
        # "--specs=nosys.specs",
        # "--specs=nano.specs",
        "--specs={}".format(board.get("build.specs"))
    ],

    LIBS=["stdc++", "supc++", "libmbed-os.a", "arm_cortexM4lf_math", "m"],

    LIBPATH=[
        join(BOARD_VARIANTS_DIR, "mbed"),
        join(CMSIS_DIR, "ARM", "Lib", "ARM")
    ],

    LIBSOURCE_DIRS=[LIBRARY_DIR]
)

libs = []

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "variant"),
    BOARD_VARIANTS_DIR
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "mbed_bridge"),
    BRIDGE_DIR,
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "core-implement"),
    join(CORE_DIR, "sdk", "core-implement"),
))

env.Prepend(LIBS=libs)
