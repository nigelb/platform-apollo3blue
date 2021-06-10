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

__globals = dict(globals())

from os.path import isdir, split, join
from SCons.Script import DefaultEnvironment
import sys

env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()
FRAMEWORK_DIR = platform.get_package_dir("framework-arduinoapollo3")
assert isdir(FRAMEWORK_DIR)

framework_version = platform.get_package_version("framework-arduinoapollo3")
major, minor, patch = framework_version.split(".")

major = int(major)
minor = int(minor)
patch = int(patch)

this_script = env.GetFrameworkScript("arduino")

builder_dir = split(this_script)[0]

script_fn = None

if major == 1:
    script_fn = join(builder_dir, "arduino_core_v1.py")
    scriptname = "arduino_core_v1"
    try:
        board.get("build.v1")
    except:
        sys.stderr.write('Error: Board: "%s" not supported by Arduino_Apollo3-%s\n'%(board.get("name"), framework_version))
        env.Exit(1)
elif major == 2:
    script_fn = join(builder_dir, "arduino_core_v2.py")
    scriptname = "arduino_core_v2"
    try:
        board.get("build.v2")
    except:
        sys.stderr.write('Error: Board: "%s" not supported by Arduino_Apollo3-%s\n'%(board.get("name"), framework_version))
        env.Exit(1)



if script_fn is None:
    sys.stderr.write("Error: Builder script count not be found\n")
    env.Exit(1)

with open(script_fn, "r") as script_in:
    exec(compile(script_in.read(), scriptname, 'exec'), __globals)


