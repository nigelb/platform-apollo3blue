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
import os
from argparse import ArgumentParser

template = """{{
  "build": {{
    "cpu": "cortex-m4",
    "f_cpu": "48000000L",
    "mcu": "AMA3B1KK",
    "part": "apollo3",
    "fabi": "hard",
    "specs": "nosys.specs",
    "framework": {{}}
  }},
    "debug": {{
    "jlink_device": "AMA3B1KK-KBR",
    "svd_path": "apollo3.svd",
    "swo_freq": 12000000, 
    "init": {{
        "break": "tbreak setup"
      }}
    }},  
  "frameworks": {frameworks},
  "name": "{board_name}",
  "upload": {{
    "maximum_ram_size": 393216,
    "maximum_size": 983040,
    "protocol": "svl",
    "protocols": [
      "svl",
      "asb",
      "jlink"
    ]
  }},
  "url": "{board_url}",
  "vendor": "{vendor}"
}}
"""

arduino_v1 = """
{{
    "variant": "{arduino_v1_variant}",
    "extra_flags": "{arduino_v1_extra_flags}"
}}
"""
arduino_v2 = """
{{
    "variant": "{arduino_v2_variant}",
    "extra_flags": "{arduino_v2_extra_flags}"
}}

"""

ambiqsdk_sfe = """
      {{
        "variant": {ambiq_variant},
        "extra_flags": "{ambiq_extra_flags}",
        "variant_lib_src_filter": "{ambiq_variant_lib_src_filter}"
      }}
"""

sub_templates = {
    "arduino_v1": {
        'path': "build/framework/arduino/v1",
        'template': arduino_v1,
        'fields': ['arduino_v1_variant', 'arduino_v1_extra_flags']
    },
    "arduino_v2": {
        'path': "build/framework/arduino/v2",
        'template': arduino_v2,
        'fields': ['arduino_v2_variant', 'arduino_v2_extra_flags']
    },
    "ambiqsdk-sfe": {
        'path': "build/framework/ambiqsdk-sfe",
        'template': ambiqsdk_sfe,
        'fields': ['ambiq_variant', 'ambiq_extra_flags', "ambiq_variant_lib_src_filter"]
    }
}

paramaters = {
    "SparkFun_Artemis_Development_Kit.json":
        {
            'board_url': 'https://www.sparkfun.com/products/16828',
            'board_name': 'SparkFun Artemis Development Kit',
            'vendor': 'SparkFun',
            'arduino_v1_variant': 'artemis_dk',
            'arduino_v1_extra_flags': '-DAM_AP3_SFE_ARTEMIS_DK',
            'arduino_v2_variant': 'TARGET_SFE_ARTEMIS_DK',
            'arduino_v2_extra_flags': '-DAPOLLO3_SFE_ARTEMIS_DK',
            'ambiq_variant': ['boards_sfe', 'artemis_dk'],
            'ambiq_extra_flags': '',
            'ambiq_variant_lib_src_filter': '',
            'frameworks': ["arduino", "ambiqsdk-sfe"]
        },

    "SparkFun_Artemis_Module.json":
        {
            'board_url': 'https://www.sparkfun.com/products/15484',
            'board_name': 'SparkFun Artemis Module',
            'vendor': 'SparkFun',
            'arduino_v1_variant': 'artemis',
            'arduino_v1_extra_flags': '-DSFE_ARTEMIS',
            'arduino_v2_variant': 'TARGET_SFE_ARTEMIS_MODULE',
            'arduino_v2_extra_flags': '-DARDUINO_APOLLO3_SFE_ARTEMIS_MODULE',
            'ambiq_variant': ['boards_sfe', 'artemis_module'],
            'ambiq_extra_flags': '',
            'ambiq_variant_lib_src_filter': '',
            'frameworks': ["arduino", "ambiqsdk-sfe"]
        },

    "SparkFun_RedBoard_Artemis_Nano.json":
        {
            'board_url': 'https://www.sparkfun.com/products/15443',
            'board_name': 'SparkFun RedBoard Artemis Nano',
            'vendor': 'SparkFun',
            'arduino_v1_variant': 'redboard_artemis_nano',
            'arduino_v1_extra_flags': '-DAM_AP3_SFE_BB_ARTEMIS_NANO',
            'arduino_v2_variant': 'TARGET_SFE_ARTEMIS_NANO',
            'arduino_v2_extra_flags': '-DARDUINO_APOLLO3_SFE_ARTEMIS_NANO',
            'ambiq_variant': ['boards_sfe', 'redboard_artemis_nano'],
            'ambiq_extra_flags': '',
            'ambiq_variant_lib_src_filter': '',
            'frameworks': ["arduino", "ambiqsdk-sfe"]
        },

    "SparkFun_Edge_Development_Board.json":
        {
            'board_url': 'https://www.sparkfun.com/products/15170',
            'board_name': 'SparkFun Edge Development Board',
            'vendor': 'SparkFun',
            'arduino_v1_variant': 'edge',
            'arduino_v1_extra_flags': '-DSFE_EDGE',
            'arduino_v2_variant': 'TARGET_SFE_EDGE',
            'arduino_v2_extra_flags': '-DARDUINO_APOLLO3_SFE_EDGE',
            'ambiq_variant': ['boards_sfe', ''],
            'ambiq_extra_flags': 'edge',
            'ambiq_variant_lib_src_filter': '',
            'frameworks': ["arduino", "ambiqsdk-sfe"]
        },

    "SparkFun_Edge_2_Development_Board.json":
        {
            'board_url': 'https://www.sparkfun.com/products/15420',
            'board_name': 'SparkFun Edge 2 Development Board',
            'vendor': 'SparkFun',
            'arduino_v1_variant': 'edge2',
            'arduino_v1_extra_flags': '-DSFE_EDGE2',
            'arduino_v2_variant': 'TARGET_SFE_EDGE2',
            'arduino_v2_extra_flags': '-DARDUINO_APOLLO3_SFE_EDGE',
            'ambiq_variant': ['boards_sfe', ''],
            'ambiq_extra_flags': 'edge2',
            'ambiq_variant_lib_src_filter': '',
            'frameworks': ["arduino", "ambiqsdk-sfe"]
        },

    "SparkFun_MicroMod_Artemis_Processor.json":
        {
            'board_url': 'https://www.sparkfun.com/products/16401',
            'board_name': 'SparkFun MicroMod Artemis Processor',
            'vendor': 'SparkFun',
            'arduino_v1_variant': 'artemis_micromod',
            'arduino_v1_extra_flags': '-DAM_AP3_SFE_ARTEMIS_MICROMOD',
            'arduino_v2_variant': 'TARGET_SFE_ARTEMIS_MM_PB',
            'arduino_v2_extra_flags': '-DAPOLLO3_SFE_ARTEMIS_MM_PB',
            'frameworks': ["arduino"]
        },

    "SparkFun_RedBoard_Artemis.json":
        {
            'board_url': 'https://www.sparkfun.com/products/15444',
            'board_name': 'SparkFun RedBoard Artemis',
            'vendor': 'SparkFun',
            'arduino_v1_variant': 'redboard_artemis',
            'arduino_v1_extra_flags': '-DAM_AP3_SFE_BB_ARTEMIS',
            'arduino_v2_variant': 'TARGET_SFE_ARTEMIS',
            'arduino_v2_extra_flags': '-DARDUINO_APOLLO3_SFE_ARTEMIS',
            'ambiq_variant': ['boards_sfe', 'redboard_artemis'],
            'ambiq_extra_flags': '',
            'ambiq_variant_lib_src_filter':'',
            'frameworks': ["arduino", "ambiqsdk-sfe"]
        },

    "SparkFun_RedBoard_Artemis_ATP.json":
        {
            'board_url': 'https://www.sparkfun.com/products/15442',
            'board_name': 'SparkFun RedBoard Artemis ATP',
            'vendor': 'SparkFun',
            'arduino_v1_variant': 'redboard_artemis_atp',
            'arduino_v1_extra_flags': '-DARDUINO_AM_AP3_SFE_BB_ARTEMIS_ATP',
            'arduino_v2_variant': 'TARGET_SFE_ARTEMIS_ATP',
            'arduino_v2_extra_flags': '-DARDUINO_APOLLO3_SFE_ARTEMIS_ATP',
            'ambiq_variant': ['boards_sfe', 'redboard_artemis_atp'],
            'ambiq_extra_flags': '',
            'ambiq_variant_lib_src_filter': '',
            'frameworks': ['arduino', 'ambiqsdk-sfe']
        },

    "SparkFun_Thing_Plus_Artemis.json":
        {
            'board_url': 'https://www.sparkfun.com/products/15574',
            'board_name': 'SparkFun Thing Plus - Artemis',
            'vendor': 'SparkFun',
            'arduino_v1_variant': 'artemis_thing_plus',
            'arduino_v1_extra_flags': '-DAM_AP3_SFE_THING_PLUS',
            'arduino_v2_variant': 'TARGET_SFE_ARTEMIS_THING_PLUS',
            'arduino_v2_extra_flags': '-DARDUINO_APOLLO3_SFE_ARTEMIS_THING_PLUS',
            'ambiq_variant': ['boards_sfe', 'artemis_thing_plus'],
            'ambiq_extra_flags': '',
            'ambiq_variant_lib_src_filter': '',
            'frameworks': ['arduino', 'ambiqsdk-sfe']
        },

    "SparkFun_Thing_Plus_expLoRaBLE.json":
        {
            'board_url': 'https://www.sparkfun.com/products/17506',
            'board_name': 'SparkFun LoRa Thing Plus - expLoRaBLE',
            'vendor': 'SparkFun',
            'arduino_v2_variant': 'TARGET_LoRa_THING_PLUS_expLoRaBLE',
            'arduino_v2_extra_flags': '-DARDUINO_AM_AP3_THING_PLUS_expLoRaBLE',
            'frameworks': ["arduino"]
        },
    "Ambiq_Apollo3_Blue_EVB.json":
        {
            'board_url': 'https://ambiq.com/apollo3-blue/',
            'board_name': 'Ambiq Apollo3 Blue EVB',
            'vendor': 'Ambiq',
            'ambiq_variant': ['boards', 'apollo3_evb'],
            'ambiq_extra_flags': '',
            'ambiq_variant_lib_src_filter': '+<bsp/*> -<examples/**/*>',
            'frameworks': ['ambiqsdk-sfe']
        }
}


def has_framework(params, fields):
    results = {}
    total = True
    for field in fields:
        f = field in params
        results[field] = f
        total &= f
    return total, results


def insert_node_at_path(path, root, node):
    _path = path.split("/")
    s = root
    for p in _path[:-1]:
        if p not in s:
            s[p] = {}
        s = s[p]
    s[_path[-1]] = node
    return s


def convert_board_data(board_data):
    for i in board_data:
        if type(board_data[i]) == list:
            board_data[i] = json.dumps(board_data[i])
    return board_data


def construct_output(board_file):
    board_data = paramaters[board_file]
    print(template.format(**convert_board_data(board_data)))
    res = json.loads(template.format(**board_data))
    for sub_template_name in sub_templates:
        sub_template = sub_templates[sub_template_name]
        hf, results = has_framework(board_data, sub_template['fields'])
        print(results)
        if hf:
            node = sub_template['template'].format(**board_data)
            insert_node_at_path(sub_template['path'], res, json.loads(node))
    return res


def main():
    parser = ArgumentParser("board_generator", description="This program generated the board files for platform-apollo3blue")
    parser.add_argument("output_dir", help="The directory to write the board files to")

    args = parser.parse_args()

    results = {}

    for board_file in paramaters:
        print(board_file)
        board_data = construct_output(board_file)
        with open(os.path.join(args.output_dir, board_file), "w") as out:
            json.dump(board_data, out, indent=4, sort_keys=False)


if __name__ == "__main__":
    main()
