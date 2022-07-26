
from SCons.Script import DefaultEnvironment, Import, BUILD_TARGETS
from os.path import join
import sys

Import("env")
platform = env.PioPlatform()
FRAMEWORK_DIR = platform.get_package_dir("framework-ambiqsuitesdkapollo3-sfe")
env.Replace(FRAMEWORK_DIR=FRAMEWORK_DIR)
for lb in env.GetLibBuilders():
    print(lb.name, file=sys.stderr)
    if lb.name == "OneWire":
        lb.env.Append(CPPDEFINES=[("OW_PIN", 13)])