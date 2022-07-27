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

// This test demonstraights how to use the Single Wire Output (SWO)
// on the Apollo3

#include <Arduino.h>


// JLinkSWOViewerCLExe -device AMA3B1KK-KBR -itmport 0
void setup() {
  Serial.begin(115200);
  am_bsp_itm_printf_enable();  //am_bsp_uart_printf_enable()
}

int count = 0;

void loop() {
  am_util_stdio_printf("SWO Example:%i\n", count++);
  delay(1000);
}

