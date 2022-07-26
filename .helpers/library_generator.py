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
import json
import os, os.path
from argparse import ArgumentParser

base={
  "name": "",
  "version": "0.1",
  "description": "",
  "frameworks": [
    "ambiqsdk-sfe"
  ],
  "license": "",
  "build": {
    "flags": [],
    "libArchive": True,
    "srcDir": None,
    "includeDir": None,
    "srcFilter": [
      "+<**/*.c>",
      "+<**/*.h>"
    ],
    "libLDFMode": "deep+"
  }
}

def path_split(file_path):
    start = file_path
    result = []
    while len(start) > 0:
        a,b = os.path.split(start)
        result.insert(0, b)
        start = a
    return result


class LibGenerator:
    def __init__(self, args):
        self.args = args
        self.base_dir = os.path.join(args.framework_dir, args.library_dir)
        self.lib_output_dir = os.path.join(args.output_dir, args.library_dir)
        self.base = json.dumps(base)
        if not os.path.exists(self.lib_output_dir):
            os.makedirs(self.lib_output_dir)

    def create_lib(self, lib):
        sub_lib_dir = os.path.join(self.base_dir, lib)
        include_dirs = []
        manifest = json.loads(self.base)
        manifest['name'] = "%s%s"%(self.args.name_prefix, lib)
        manifest['license'] = self.args.license
        build = manifest["build"]
        build["srcDir"] = sub_lib_dir.replace(self.args.framework_dir, "%(FRAMEWORK_DIR)s")
        build["includeDir"] = sub_lib_dir.replace(self.args.framework_dir, "%(FRAMEWORK_DIR)s")
        for i in os.walk(sub_lib_dir, False):
            _dir, subdirs, files = i
            if _dir[0] != sub_lib_dir:
                tdir = _dir.replace(self.args.framework_dir, "%(FRAMEWORK_DIR)s")
                include_dirs.append(tdir)
        if len(include_dirs) > 1:
            for inc in include_dirs:
                build["flags"].append("-I%s"%inc)
        output = os.path.join(self.lib_output_dir, lib)
        if not os.path.exists(output):
            os.makedirs(output)
        manifest_fn = os.path.join(output, "library.json")
        if True:#not os.path.exists(manifest_fn):
            with open(manifest_fn, "w") as man_out:
                json.dump(manifest, man_out, indent=4, sort_keys=False)
        else:
            print("%s already exists. manifest:", manifest)
        lib_path = ['"%s"'%x for x in path_split(self.args.library_dir)]
        lib_path_str = ", ".join(lib_path)
        print("dict(")
        print('  src_path = join(FRAMEWORK_DIR, %s, "%s"),'%(lib_path_str, lib))
        print('  manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", %s, "%s", "library.json")'%(lib_path_str, lib))
        print("),")


        



    def run(self):
        for lib_name in os.listdir(self.base_dir):
            self.create_lib(lib_name)
            # return


def main():
    parser = ArgumentParser("Library Generator")
    parser.add_argument("--framework_dir", required=True)
    parser.add_argument("--library_dir", required=True)
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--name_prefix", default="")
    parser.add_argument("--license", default="")

    args = parser.parse_args()
    LibGenerator(args).run()



if __name__ == "__main__":
    main()