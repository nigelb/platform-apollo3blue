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

# __globals = dict(globals())
from os.path import isdir, split, join
from SCons.Script import AlwaysBuild, Builder, Default, DefaultEnvironment
import sys
import platform as sys_pf


def launch_arduino_core_builder(env, platform, board):
    FRAMEWORK_DIR = platform.get_package_dir("framework-arduinoapollo3")
    project = env.GetProjectConfig()
    assert isdir(FRAMEWORK_DIR)

    framework_version = platform.get_package_version("framework-arduinoapollo3")
    framework_semantic_version, framework_commit = framework_version.split("+")
    major, minor, patch = framework_semantic_version.split(".")

    major = int(major)
    minor = int(minor)
    patch = int(patch)

    script_name= "unknown"

    if major == 1:
        script_name = "core_v1"
        try:
            board.get("build.framework.arduino.v1")
        except:
            sys.stderr.write('Error: Board: "%s" not supported by Arduino_Apollo3-%s\n'%(board.get("name"), framework_version))
            env.Exit(1)
    elif major == 2:
        script_name = "core_v2"
        try:
            board.get("build.framework.arduino.v2")
        except:
            sys.stderr.write('Error: Board: "%s" not supported by Arduino_Apollo3-%s\n'%(board.get("name"), framework_version))
            env.Exit(1)
    else:
        sys.stderr.write('Error: Could not find builder for "%s" "%s" ' % (board.get("name"), framework_version))
        env.Exit(1)

    env.SConscript(join("arduino", "%s.py" % script_name))


def configure_base_arduino_environment(env, platform, board):
    upload_protocol = env.subst("$UPLOAD_PROTOCOL")
    FRAMEWORK_DIR = platform.get_package_dir("framework-arduinoapollo3")
    assert isdir(FRAMEWORK_DIR)

    system_type = sys_pf.system().lower() if sys_pf.system() != "Darwin" else "macosx"

    framework_version = platform.get_package_version("framework-arduinoapollo3")
    framework_semantic_version, framework_commit = framework_version.split("+")
    major, minor, patch = framework_semantic_version.split(".")

    framework_major_version = int(major)
    framework_minor_version = int(minor)
    framework_patch_version = int(patch)

    if upload_protocol in ["svl", "asb"]:
        upload_program = None

        if framework_major_version == 1:
            if upload_protocol == "svl":
                upload_program = join(FRAMEWORK_DIR, "tools", "artemis", system_type, "artemis_svl")
            elif upload_protocol == "asb":
                upload_program = join(FRAMEWORK_DIR, "tools", "ambiq", system_type, "ambiq_bin2board")
            #if upload_protocol != "svl":
            #    sys.stderr.write("Error: Upload protocol %s is not supported on Core V1\n")
            #    env.Exit(1)
        elif framework_major_version == 2:
            if upload_protocol in ["svl", "asb"]:
                upload_program = join(FRAMEWORK_DIR, "tools", "uploaders", upload_protocol, "dist", system_type,
                                  upload_protocol)
        else:
            sys.stderr.write("Error: cannot determine the uploader program\n")
            env.Exit(1)

        if system_type == "windows":
            upload_program += ".exe"

        env.Replace(UPLOADER=upload_program)

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

    )


# if script_fn is None:
#     sys.stderr.write("Error: Builder script count not be found\n")
#     env.Exit(1)

# with open(script_fn, "r") as script_in:
#     exec(compile(script_in.read(), scriptname, 'exec'), __globals)
# print(join(builder_dir, "arduino", "%s.py" % scriptname))
# env.SConscript(join(builder_dir, "arduino", "%s.py" % scriptname))



env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()

configure_base_arduino_environment(env, platform, board)
launch_arduino_core_builder(env, platform, board)



