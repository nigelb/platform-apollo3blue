// platform-apollo3blue: Apollo3Blue development platform for platformio.
// Copyright 2019-present NigelB
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

//
const uint32_t
g_am_hal_mcuctrl_flash_size[16] =
{
     16 * 1024,             /* 0x0 0x00004000   16 KB */
     32 * 1024,             /* 0x1 0x00008000   32 KB */
     64 * 1024,             /* 0x2 0x00010000   64 KB */
    128 * 1024,             /* 0x3 0x00020000  128 KB */
    256 * 1024,             /* 0x4 0x00040000  256 KB */
    512 * 1024,             /* 0x5 0x00080000  512 KB */
      1 * 1024 * 1024,      /* 0x6 0x00100000    1 MB */
      2 * 1024 * 1024,      /* 0x7 0x00200000    2 MB */
      3 * 1024 * 1024 / 2,  /* 0x8 0x00600000  1.5 MB */
    0, 0, 0, 0, 0, 0, 0
};

const uint32_t
g_am_hal_mcuctrl_sram_size[16] =
{
     16 * 1024,             /* 0x0 0x00004000   16 KB */
     32 * 1024,             /* 0x1 0x00008000   32 KB */
     64 * 1024,             /* 0x2 0x00010000   64 KB */
    128 * 1024,             /* 0x3 0x00020000  128 KB */
    256 * 1024,             /* 0x4 0x00040000  256 KB */
    512 * 1024,             /* 0x5 0x00080000  512 KB */
      1 * 1024 * 1024,      /* 0x6 0x00100000    1 MB */
    384 * 1024,             /* 0x7 0x00200000  384 KB */
    768 * 1024,             /* 0x8 0x000C0000  768 KB */
    0, 0, 0, 0, 0, 0, 0
};

uint32_t *CHIPPN = (uint32_t*)0x40020000;

#define CHIPPN_PN_MASK 0xFF000000
#define CHIPPN_PN_OFFSET 0x18
#define CHIPPN_PN (((*CHIPPN) & CHIPPN_PN_MASK) >> CHIPPN_PN_OFFSET)

#define CHIPPN_FLASH_SIZE_MASK 0xF00000
#define CHIPPN_FLASH_SIZE_OFFSET 0x14
#define CHIPPN_FLASH_SIZE g_am_hal_mcuctrl_flash_size[(((*CHIPPN) & CHIPPN_FLASH_SIZE_MASK) >> CHIPPN_FLASH_SIZE_OFFSET)]


#define CHIPPN_SRAM_SIZE_MASK 0xF0000
#define CHIPPN_SRAM_SIZE_OFFSET 0x10
#define CHIPPN_SRAM_SIZE g_am_hal_mcuctrl_sram_size[(((*CHIPPN) & CHIPPN_SRAM_SIZE_MASK) >> CHIPPN_SRAM_SIZE_OFFSET)]

#define CHIPPN_REV_MAJ_MASK 0xF000
#define CHIPPN_REV_MAJ_OFFSET 0xC
#define CHIPPN_REV_MAJ (((*CHIPPN) & CHIPPN_REV_MAJ_MASK) >> CHIPPN_REV_MAJ_OFFSET)

#define CHIPPN_REV_MIN_MASK 0xF00
#define CHIPPN_REV_MIN_OFFSET 0x8
#define CHIPPN_REV_MIN (((*CHIPPN) & CHIPPN_REV_MIN_MASK) >> CHIPPN_REV_MIN_OFFSET)

#define CHIPPN_PKG_MASK 0xC0
#define CHIPPN_PKG_OFFSET 0x6
#define CHIPPN_PKG (((*CHIPPN) & CHIPPN_PKG_MASK) >> CHIPPN_PKG_OFFSET)

#define CHIPPN_PINS_MASK 0x38
#define CHIPPN_PINS_OFFSET 0x3
#define CHIPPN_PINS (((*CHIPPN) & CHIPPN_PINS_MASK) >> CHIPPN_PINS_OFFSET)

#define CHIPPN_TEMP_MASK 0x06
#define CHIPPN_TEMP_OFFSET 0x1
#define CHIPPN_TEMP (((*CHIPPN) & CHIPPN_TEMP_MASK) >> CHIPPN_TEMP_OFFSET)

#define CHIPPN_QUALIFIED_MASK 0x01
#define CHIPPN_QUALIFIED_OFFSET 0x0
#define CHIPPN_QUALIFIED (((*CHIPPN) & CHIPPN_QUALIFIED_MASK) >> CHIPPN_QUALIFIED_OFFSET)

//======================================================================================================
uint32_t *CHIPREV = (uint32_t*)0x4002000C;

#define CHIPREV_SIPART_MASK 0xFFF00
#define CHIPREV_SIPART_OFFSET 0x8
#define CHIPREV_SIPART (((*CHIPREV) & CHIPREV_SIPART_MASK) >> CHIPREV_SIPART_OFFSET)

#define CHIPREV_MAJ_MASK 0xF0
#define CHIPREV_MAJ_OFFSET 0x4
#define CHIPREV_MAJ (((*CHIPREV) & CHIPREV_MAJ_MASK) >> CHIPREV_MAJ_OFFSET)

#define CHIPREV_MIN_MASK 0xF
#define CHIPREV_MIN_OFFSET 0x0
#define CHIPREV_MIN (((*CHIPREV) & CHIPREV_MIN_MASK) >> CHIPREV_MIN_OFFSET)

//======================================================================================================


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  delay(100);
  Serial.println();
  Serial.println("================================================================");
  Serial.printf("CHIPPN: %08x\r\n", *CHIPPN);
  Serial.printf("\tCHIPPN_PART_NUMBER: 0x%x, ", CHIPPN_PN);
  switch(CHIPPN_PN)
  {
    case 0x6:
      Serial.println("Apollo3");
      break;
    case 0x3:
      Serial.println("Apollo2");
      break;
    case 0x1:
      Serial.println("Apollo");
      break;
    default:
      Serial.println("UNKNOWN");
      
  }
  Serial.printf("\tCHIPPN_FLASH_SIZE: %i Bytes\r\n", CHIPPN_FLASH_SIZE);
  Serial.printf("\tCHIPPN_SRAM_SIZE: %i Bytes\r\n", CHIPPN_SRAM_SIZE);
  Serial.printf("\tCHIPPN_REV_MAJ: %x\r\n", CHIPPN_REV_MAJ);  
  Serial.printf("\tCHIPPN_REV_MIN: %x\r\n", CHIPPN_REV_MIN);
  Serial.printf("\tCHIPPN_PKG: %x: ", CHIPPN_PKG);
  switch(CHIPPN_PKG)
  {
      case 0x00:
          Serial.println("SIP");
          break;
      case 0x01:
          Serial.println("QFN");
          break;
      case 0x02:
          Serial.println("BGA");
          break;
      case 0x03:
          Serial.println("CSP");
          break;
      default:
            Serial.println("Unknown");

  }
  Serial.printf("\tCHIPPN_PINS: %x ", CHIPPN_PINS);
  switch(CHIPPN_PINS)
  {
      case 0x00:
          Serial.println("25 Pins");
          break;
      case 0x01:
          Serial.println("49 Pins");
          break;
      case 0x02:
          Serial.println("64 Pins");
          break;
      case 0x03:
          Serial.println("81 Pins");
          break;
      case 0x04:
          Serial.println("104 Pins");
          break;
      default:
            Serial.println("Unknown");
  }
  Serial.printf("\tCHIPPN_TEMP: %x\r\n", CHIPPN_TEMP);
  Serial.printf("\tCHIPPN_QUALIFIED: %x\r\n", CHIPPN_QUALIFIED);
  
  Serial.println();
  Serial.printf("CHIPREV: 0x%08x\r\n", *CHIPREV);
  Serial.printf("\tCHIPREV_SIPART: 0x%X\r\n", CHIPREV_SIPART);
  Serial.printf("\tCHIPREV_MAJOR: Apollo3 Revision %x\r\n", CHIPREV_MAJ);
  Serial.printf("\tCHIPREV_MINOR: %i\r\n", CHIPREV_MIN);
  
}

void loop() {}
