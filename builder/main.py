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

if 'PLATFORMIO_UPLOAD_PROTOCOL' in os.environ:
    env.Replace(UPLOAD_PROTOCOL=os.environ['PLATFORMIO_UPLOAD_PROTOCOL'])
    print("",file=sys.stderr)
    print(f"WARNING! UPLOAD_PROTOCOL has been overridden by the environment variable PLATFORMIO_UPLOAD_PROTOCOL and set to: {os.environ['PLATFORMIO_UPLOAD_PROTOCOL']}", file=sys.stderr)
    print("",file=sys.stderr)

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
