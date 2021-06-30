# Copyright 2014-present PlatformIO <contact@platformio.org>
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


# ***********************************************************
# Code borrowed and modified from:
# https://github.com/platformio/platform-atmelsam/blob/c98f1b77039f3dac3923416f54662a70f2ee2960/platform.py
#
# The original code (as well as this project) is distributed under
# an Apache2.0 License: https://www.apache.org/licenses/LICENSE-2.0.htm


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

from copy import deepcopy
from platform import system

from platformio.managers.platform import PlatformBase
from platformio.util import get_systype


class Apollo3bluePlatform(PlatformBase):
    def configure_default_packages(self, variables, targets):
        if not variables.get("board"):
            return PlatformBase.configure_default_packages(
                self, variables, targets)
        board = self.board_config(variables.get("board"))
        upload_protocol = variables.get("upload_protocol",
                                        board.get("upload.protocol", ""))
        debug_tool = variables.get("debug_tool", None)

        if "arduino" in variables.get("pioframework", []):
            self.packages["framework-arduinoapollo3"]["optional"] = False
        elif "ambiqsdk-sfe" in variables.get("pioframework", []):
            self.packages["framework-ambiqsuitesdkapollo3-sfe"]["optional"] = False

        # If jlink is used, mark tool-jlink as non-optional
        if "jlink" in upload_protocol:
            self.packages["tool-jlink"]["optional"] = False
        if debug_tool is not None and "jlink" in debug_tool:
            self.packages["tool-jlink"]["optional"] = False

        return PlatformBase.configure_default_packages(self, variables, targets)

    def get_boards(self, id_=None):
        result = PlatformBase.get_boards(self, id_)
        if not result:
            return result
        if id_:
            return self._add_default_debug_tools(result)
        else:
            for key, value in result.items():
                result[key] = self._add_default_debug_tools(result[key])
        return result

    def _add_default_debug_tools(self, board):
        debug = board.manifest.get("debug", {})
        upload_protocols = board.manifest.get("upload", {}).get(
            "protocols", [])
        if "tools" not in debug:
            debug["tools"] = {}

        # J-Link
        tools = ("jlink",)
        for link in tools:
            if link not in upload_protocols or link in debug["tools"]:
                continue

            if link == "jlink":
                assert debug.get("jlink_device"), (
                    "Missed J-Link Device ID for %s" % board.id)
                debug["tools"][link] = {
                    "server": {
                        "package": "tool-jlink",
                        "arguments": [
                            "-singlerun",
                            "-if", "SWD",
                            "-select", "USB",
                            "-device", debug.get("jlink_device"),
                            "-port", "2331"
                        ],
                        "executable": ("JLinkGDBServerCL.exe"
                                       if system() == "Windows" else
                                       "JLinkGDBServer")
                    },
                }

        board.manifest["debug"] = debug
        return board

    def configure_debug_options(self, initial_debug_options, ide_data):
        debug_options = deepcopy(initial_debug_options)
        adapter_speed = initial_debug_options.get("speed")
        if adapter_speed:
            server_options = debug_options.get("server") or {}
            server_executable = server_options.get("executable", "").lower()
            if "jlink" in server_executable:
                debug_options["server"]["arguments"].extend(
                    ["-speed", adapter_speed]
                )

        return debug_options
