
from platformio.managers.platform import PlatformBase
from _platform import system


class Apollo3bluePlatform(PlatformBase):

    def __init__(self, manifest_path):
        super().__init__(manifest_path)

        # env = DefaultEnvironment()
        # platform = env.PioPlatform()
    def configure_default_packages(self, variables, targets):
        self.variables = variables
        return PlatformBase.configure_default_packages(self, variables, targets)


    def get_boards(self, id_=None):
        # print(id_)
        # print(self.config.get("env:Jim","framework"))

        # print(self.config.get())
        print("=============================================================_==:")
        result = PlatformBase.get_boards(self, id_)

        print(result)
        result.manifest['build']['v2'] = result.manifest['build']['framework']['arduino']['v2']

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
        tools = ("jlink")
        for link in tools:
            if link not in upload_protocols or link in debug["tools"]:
                continue
            elif link == "jlink":
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
                    "onboard": link in debug.get("onboard_tools", [])
                }
        return board
