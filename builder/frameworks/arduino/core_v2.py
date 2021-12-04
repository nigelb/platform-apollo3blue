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
import platform as system_platform
import sys

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

PROJECT_DIR = env.subst("$PROJECT_DIR")
TOOLS_DIR = join(FRAMEWORK_DIR, "tools")

upload_protocol = env.subst("$UPLOAD_PROTOCOL")

# =======================================================
# Linker Script
linker_script_dir = {
     "0xC000.ld": "asb",
     "0x10000.ld": "svl",
}

linker_script_fn = board.get("build.framework.arduino.v2.linker_script")
user_linker_script_fn = board.get("build.linker_script", "")

if len(user_linker_script_fn) == 0:
    user_linker_script_fn = None

linker_script = None

if user_linker_script_fn is not None:
    if exists(join(PROJECT_DIR, user_linker_script_fn)):
        linker_script = join(PROJECT_DIR, user_linker_script_fn)
        sys.stderr.write("Using linker script: %s\n" % user_linker_script_fn)
    else:
        sys.stderr.write("\nError: Could not find linker script: %s\n" % user_linker_script_fn)
        sys.stderr.write("Searched in:\n")
        sys.stderr.write("\t%s\n" % PROJECT_DIR)
        env.Exit(1)

elif linker_script_fn in linker_script_dir:
    linker_script = join(TOOLS_DIR, "uploaders", linker_script_dir[linker_script_fn], linker_script_fn)
    if not exists(linker_script):
        sys.stderr.write("\nError: Could not find linker script: %s\n" % linker_script)
        env.Exit(1)
else:
    sys.stderr.write("\nError: Could not find linker script: %s\n" % linker_script_fn)
    env.Exit(1)

env.Replace(LDSCRIPT_PATH=linker_script)

# =======================================================
# Bootloader location
env.Replace(SVL_BOOTLOADER_BIN=join(TOOLS_DIR, "uploaders", "svl", "bootloader", "gcc", "artemis_module", "bin", "svl.bin"))
# =======================================================

# =======================================================
# Uploader Binary Locations
system_type = system_platform.system().lower() if system_platform.system() != "Darwin" else "macosx"
env.Replace(SVL_UPLOADER=join(FRAMEWORK_DIR, "tools", "uploaders", "svl", "dist", system_type, "svl"))
env.Replace(ASB_UPLOADER=join(FRAMEWORK_DIR, "tools", "uploaders", "asb", "dist", system_type, "asb"))
# =======================================================

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
