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

import os
from os.path import isdir, join
from SCons.Script import DefaultEnvironment
from platformio.builder.tools.piolib import PlatformIOLibBuilder
from platformio.package.manifest.parser import ManifestParserFactory, ManifestFileType

env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()
build_mcu = env.get("BOARD_MCU", board.get("build.mcu", ""))
framework_build = board.get("build.framework.ambiqsdk-sfe")

env.ProcessFlags(framework_build.get("extra_flags"))

FRAMEWORK_DIR        = platform.get_package_dir("framework-ambiqsuitesdkapollo3-sfe")
VARIANT_DIR          = join(FRAMEWORK_DIR, *framework_build.get("variant"))
CMSIS_DIR            = join(FRAMEWORK_DIR, "CMSIS")
ARM_CMSIS_DIR        = join(CMSIS_DIR, "ARM")
AMBIQMICRO_CMSIS_DIR = join(CMSIS_DIR, "AmbiqMicro")
DEVICES_DIR           = join(FRAMEWORK_DIR, "devices")
UTILS_DIR             = join(FRAMEWORK_DIR, "utils")
MCU_DIR               = join(FRAMEWORK_DIR, "mcu", board.get("build.part"))
TOOLS_DIR             = join(FRAMEWORK_DIR, "boards_sfe", "common", "tools_sfe")
BOOTLOADER_DIR        = join(FRAMEWORK_DIR, "bootloader")

system_type = env.subst("$SYSTEM_TYPE")
env.Replace(ASB_UPLOADER=join(FRAMEWORK_DIR, "boards_sfe", "common", "tools_sfe", "asb", "dist", system_type, "asb"))
env.Replace(SVL_UPLOADER=join(FRAMEWORK_DIR, "boards_sfe", "common", "tools_sfe", "svl", "dist", system_type, "svl"))
env.Replace(SVL_LINKER_SCRIPT=join(FRAMEWORK_DIR, "boards_sfe", "common", "tools_sfe", "templates", "asb_svl_linker.ld"))
env.Replace(ASB_LINKER_SCRIPT=join(FRAMEWORK_DIR, "boards_sfe", "common", "tools_sfe", "templates", "asb_linker.ld"))
env.Replace(SVL_BOOTLOADER_BIN=join(FRAMEWORK_DIR, "boards_sfe", "common", "tools_sfe", "svl", "bootloader", "gcc", "artemis_module", "bin", "svl.bin"))


upload_protocol = env.subst("$UPLOAD_PROTOCOL")
if not upload_protocol.startswith("jlink"):
    uploader = join(TOOLS_DIR, upload_protocol, "dist", system_type, upload_protocol)
    if system_type == "windows":
        uploader += ".exe"
    env.Replace(
        UPLOADER=uploader,
    )


env.Append(
    ASFLAGS=[
        "-c", "-g", "-MMD",
        "-x", "assembler-with-cpp",
    ],
    CFLAGS=[
        "-mthumb", "-mcpu=%s"%board.get("build.cpu"), "-mfpu=fpv4-sp-d16", "-mfloat-abi=%s"%board.get("build.fabi"),
        "-ffunction-sections", "-fdata-sections", "-fomit-frame-pointer",
        "-MMD", "-MP", "-std=c99", "-Wall", "-g",
        "-O0",
        "-I{}".format(MCU_DIR),
        "-I{}/Include".format(ARM_CMSIS_DIR),
        "-I{}/Include".format(AMBIQMICRO_CMSIS_DIR),
        "-I{}/bsp".format(VARIANT_DIR),
        "-I{}".format(DEVICES_DIR),
        "-I{}".format(UTILS_DIR),
        "-I{}".format(BOOTLOADER_DIR),
        "-I{}".format(join(env.subst("$PROJECT_DIR"), "src"))
    ],
    CPPDEFINES=[
        "AM_PACKAGE_BGA",
        "AM_CUSTOM_BDADDR",
        "WSF_TRACE_ENABLED",
        "AM_DEBUG_PRINTF",
        "AM_PART_APOLLO3",
        "PART_%s"%board.get("build.part"),
    ],
    LINKFLAGS=[
        "-mthumb", "-mcpu=%s"%board.get("build.cpu"), "-mfpu=fpv4-sp-d16", "-mfloat-abi=%s"%board.get("build.fabi"),
        "-nostartfiles", "-static",
        "-Wl,--gc-sections,--entry,Reset_Handler,-Map,\"%s\""% join("$BUILD_DIR", "program.map"),
        # "-Wl,-T%s"%join(FRAMEWORK_DIR, "boards_sfe","common","tools_sfe", "templates", "asb_svl_linker.ld")
    ],
    LIBS=["arm_cortexM4lf_math", "m"],

    LIBPATH=[
        join(CMSIS_DIR, "ARM", "Lib", "ARM")
    ],
)

lib_builders = []


def create_lib(src_path, manifest_path, context):
    manifest_data = ManifestParserFactory.read_manifest_contents(manifest_path)
    manifest = ManifestParserFactory.new(manifest_data%context, ManifestFileType.from_uri(manifest_path), False)
    return PlatformIOLibBuilder(env, src_path, manifest.as_dict())


context = {"FRAMEWORK_DIR": FRAMEWORK_DIR}

ambiq_libraries=[
    dict(
        src_path=join(FRAMEWORK_DIR, "third_party", "FreeRTOSv10.1.1"),
        manifest_path=join(platform.PlatformPath, 'extra', 'ambiqsdk-sfe', 'libraries', "third_party", "FreeRTOS", "library.json")
    ),
    dict(
        src_path=join(FRAMEWORK_DIR, "third_party", "cordio", "wsf"),
        manifest_path=join(platform.PlatformPath, 'extra', 'ambiqsdk-sfe', 'libraries', "third_party", "cordio", "wsf", "library.json")
    ),
    dict(
        src_path=join(FRAMEWORK_DIR, "third_party", "prime_mpi"),
        manifest_path=join(platform.PlatformPath, 'extra', 'ambiqsdk-sfe', 'libraries', "third_party", "prime_mpi", "library.json")
    ),
    dict(
        src_path=join(FRAMEWORK_DIR, "third_party", "cordio", "ble-host"),
        manifest_path=join(platform.PlatformPath, 'extra', 'ambiqsdk-sfe', 'libraries', "third_party", "cordio", "ble-host", "library.json")
    ),
    dict(
        src_path=join(FRAMEWORK_DIR, "third_party", "cordio", "ble-profiles"),
        manifest_path=join(platform.PlatformPath, 'extra', 'ambiqsdk-sfe', 'libraries', "third_party", "cordio", "ble-profiles", "library.json")
    ),
    dict(
        src_path=join(FRAMEWORK_DIR, "third_party", "uecc"),
        manifest_path=join(platform.PlatformPath, 'extra', 'ambiqsdk-sfe', 'libraries', "third_party", "uECC", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "bootloader"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "bootloader", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "em9304"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "em9304", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "menu"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "menu", "library.json")
    ),

    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "services"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "services", "library.json")
    ),

    # ambiq_ble apps
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "apps", "adv_ext"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "apps", "adv_ext", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "apps", "amdtpc"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "apps", "amdtpc", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "apps", "amdtps"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "apps", "amdtps", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "apps", "amota"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "apps", "amota", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "apps", "ancs"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "apps", "ancs", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "apps", "barebone"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "apps", "barebone", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "apps", "beaconscanner"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "apps", "beaconscanner", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "apps", "ibeacon"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "apps", "ibeacon", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "apps", "prodtest_datc"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "apps", "prodtest_datc", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "apps", "prodtest_dats"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "apps", "prodtest_dats", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "apps", "vole"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "apps", "vole", "library.json")
    ),

    # ambiq_ble profile_appl
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profile_appl", "amdtpcommon"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profile_appl", "amdtpcommon", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profile_appl", "amdtps"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profile_appl", "amdtps", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profile_appl", "amota"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profile_appl", "amota", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profile_appl", "ams"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profile_appl", "ams", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profile_appl", "ancs"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profile_appl", "ancs", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profile_appl", "fcc_test"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profile_appl", "fcc_test", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profile_appl", "ibeacon"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profile_appl", "ibeacon", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profile_appl", "txpower_ctrl"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profile_appl", "txpower_ctrl", "library.json")
    ),
    # ambiq_ble profiles
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profiles", "amdtpc"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profiles", "amdtpc", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profiles", "amdtpcommon"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profiles", "amdtpcommon", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profiles", "amdtps"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profiles", "amdtps", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profiles", "amota"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profiles", "amota", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profiles", "amsc"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profiles", "amsc", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profiles", "ancc"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profiles", "ancc", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profiles", "custss"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profiles", "custss", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profiles", "vole"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profiles", "vole", "library.json")
    ),
    dict(
        src_path = join(FRAMEWORK_DIR, "ambiq_ble", "profiles", "volecommon"),
        manifest_path = join(platform.PlatformPath, "extra", "ambiqsdk-sfe", "libraries", "ambiq_ble", "profiles", "volecommon", "library.json")
    ),
]

for ambiq_lib in ambiq_libraries:
    lib_builders.append(create_lib(ambiq_lib['src_path'], ambiq_lib['manifest_path'], context))

libs = []

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "Variant"),
    join(FRAMEWORK_DIR, *framework_build.get("variant")),
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "Hal"),
    join(FRAMEWORK_DIR, "mcu", board.get("build.part"), "hal"),
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "Devices"),
    DEVICES_DIR,
    "+<am_devices_led.c>"
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "Utils"),
    UTILS_DIR,
    "+<*> -<am_util_regdump.c>"
))

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "Entry"),
    join(FRAMEWORK_DIR, "boards_sfe", "common", "tools_sfe", "templates"),
    "+<startup_gcc.c>"
))

def configure_upload_address(env, board):
    upload_protocol = env.subst("$UPLOAD_PROTOCOL")
    upload_address = ""
    if upload_protocol == "svl":
        upload_address = "0x10000"
    elif upload_protocol == "asb":
        upload_address = "0xC000"
    elif upload_protocol == "jlink":
        upload_address = "0x10000"
    user_upload_address = board.get("build.upload.address", "").strip()
    if len(user_upload_address) > 0:
        upload_address = user_upload_address
    env.Replace(UPLOAD_ADDRESS=upload_address)

configure_upload_address(env, board)
env.Prepend(LIBS=libs)
env.Prepend(LIBS=libs, __PIO_LIB_BUILDERS=lib_builders)

