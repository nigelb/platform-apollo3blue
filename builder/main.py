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
from SCons.Script import AlwaysBuild, Builder, Default, DefaultEnvironment, ARGUMENTS
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
debug_build_flags.default.append("-ggdb")

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
    UPLOADCMD="$UPLOADER $UPLOADERFLAGS",
    SYSTEM_TYPE=system().lower() if system() != "Darwin" else "macosx"
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

env.Replace(
    SIZEPROGREGEXP=r"^(?:\.text)\s+([0-9]+).*",
    SIZEDATAREGEXP=r"^(?:\.data|\.bss)\s+([0-9]+).*",
    SIZECHECKCMD="$SIZETOOL -A -d $SOURCES",
)

#
# Configure LDSCRIPT_PATH to be replaced later by the call to linker.py
#
env.Replace(LDSCRIPT_PATH="$$APOLLO3_LDSCRIPT_PATH")

def Apollo3SetBuildStandards(env, default_c_std="c17", default_cxx_std="c++17"):
    brd = env.BoardConfig()
    language_std = brd.get("build.standard", None)
    if language_std is not None and type(language_std) == str:
        print(f"The board_build.standard option has been deprecated for board_build.standard.c and board_build.standard.cxx options.{os.linesep}Please update your platform.ini file.", file=sys.stderr)
        sys.exit(1)

    _c_std = brd.get("build.standard.c", default_c_std)
    if _c_std is not None:
        C_STD = "-std={}".format(_c_std)
        env.Append(CFLAGS=[C_STD])

    _cxx_std = brd.get("build.standard.cxx", default_cxx_std)
    if _cxx_std is not None:
        CXX_STD = "-std={}".format(_cxx_std)
        env.Append(CXXFLAGS=[CXX_STD])

env.AddMethod(Apollo3SetBuildStandards)

#
# Target: Build executable and linkable firmware
#
target_elf = env.BuildProgram()

#
# Configure the linker script
#
env.SConscript(join("helpers", "linker.py"), exports="env")


#
# Target: Build the .bin file
#
target_bin = env.ElfToBin(join("$BUILD_DIR", "firmware"), target_elf)
env.Replace(TARGET_BIN=target_bin)

#
# Add extra targets
#
env.SConscript(join("helpers", "targets.py"), exports="env")

#
# Configure the uploader
#
env.SConscript(join("helpers", "uploader.py"), exports="env")

if int(ARGUMENTS.get("PIOVERBOSE", 0)) == 1 and len(all_build_targets) == 0:
    print("Upload Address: %s"%env.subst("$UPLOAD_ADDRESS"))
    print("Linker Script: %s" % env.subst(env.subst("$LDSCRIPT_PATH")))
#
# Target: Define targets
#
Default([target_bin])
