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

from SCons.Script import DefaultEnvironment, Import, Return
from os.path import join, exists
import sys

Import("env")
# =======================================================

def resolve_linker_script(env):

    board = env.BoardConfig()

    PROJECT_DIR = env.subst("$PROJECT_DIR")
    upload_protocol = env.subst("$UPLOAD_PROTOCOL")

    user_linker_script_fn = board.get("build.linker_script", "")

    linker_scripts = dict(
        asb=env.subst("$ASB_LINKER_SCRIPT"),
        svl=env.subst("$SVL_LINKER_SCRIPT"),
        jlink=env.subst("$SVL_LINKER_SCRIPT"),
    )

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

    else:
        if upload_protocol in linker_scripts:
            linker_script = linker_scripts[upload_protocol]

        if not exists(linker_script):
            sys.stderr.write("\nError: Could not find linker script: %s\n" % linker_script)
            env.Exit(1)

    return '"{}"'.format(linker_script)


# env = DefaultEnvironment()

def getenv():
    return env


env = getenv()

ld = resolve_linker_script(env)
env.Replace(APOLLO3_LDSCRIPT_PATH=ld)