#Using a SEGGER JLink with platform-apollo3
With platform-apollo3 you can use your SEGGER JLink to both upload your firmware to your device and as a debugger.

#Upload Firmware
To use your SEGGER JLink to upload your firmware to your apollo3 device you need to add `upload_protocol = jlink` to your projects `platformio.ini` file

For example from this:
```ini
; PlatformIO Project Configuration File
;
;   Build options: build flags, source filter
;   Upload options: custom upload port, speed and extra flags
;   Library options: dependencies, extra library storages
;   Advanced options: extra scripting
;
; Please visit documentation for the other options and examples
; https://docs.platformio.org/page/projectconf.html

[env:SparkFun_RedBoard_Artemis_ATP]
platform = apollo3blue
board = SparkFun_Artemis_Nano
framework = arduino
platform_packages = framework-arduinoapollo3@2.1.0
```

Becomes this:
```ini
; PlatformIO Project Configuration File
;
;   Build options: build flags, source filter
;   Upload options: custom upload port, speed and extra flags
;   Library options: dependencies, extra library storages
;   Advanced options: extra scripting
;
; Please visit documentation for the other options and examples
; https://docs.platformio.org/page/projectconf.html

[env:SparkFun_RedBoard_Artemis_ATP]
platform = apollo3blue
board = SparkFun_Artemis_Nano
framework = arduino
platform_packages = framework-arduinoapollo3@2.1.0
upload_protocol = jlink
```

Then, once we have connected our SEGGER JLink to our board, we can upload the firmware:
```
$> platformio run 
Processing SparkFun_RedBoard_Artemis_ATP (platform: apollo3blue; board: SparkFun_RedBoard_Artemis_ATP; framework: arduino)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
CONFIGURATION: https://docs.platformio.org/page/boards/apollo3blue/SparkFun_RedBoard_Artemis_ATP.html
PLATFORM: Apollo 3 Blue (0.0.2) > SparkFun RedBoard Artemis ATP
HARDWARE: AMA3B1KK 48MHz, 384KB RAM, 960KB Flash
DEBUG: Current (jlink) External (jlink)
PACKAGES: 
 - framework-arduinoapollo3 2.1.0 
 - toolchain-gccarmnoneeabi 1.90301.200702 (9.3.1)
LDF: Library Dependency Finder -> http://bit.ly/configure-pio-ldf
LDF Modes: Finder ~ chain, Compatibility ~ soft
Found 0 compatible libraries
Scanning dependencies...
No dependencies
Building in release mode
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/src/main.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/variant/config/pins.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/variant/variant.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/bridge/pins.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-api/api/Common.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-api/api/IPAddress.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-api/api/PluggableUSB.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-api/api/Print.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-api/api/Stream.cpp.o
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libvariant.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libvariant.a
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-api/api/String.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonAnalog.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonDigital.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonInit.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonInterrupt.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonMath.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonPulse.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonTiming.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/HardwareSerial.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/Yield.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/itoa.c.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/main.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/core-implement/CommonAnalog.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/core-implement/CommonPulse.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/EEPROM/EEPROM.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/PDM/PDM.cpp.o
In file included from /home/eng-nbb/.platformio/packages/framework-arduinoapollo3@2.1.0/libraries/PDM/src/PDM.cpp:22:
/home/eng-nbb/.platformio/packages/framework-arduinoapollo3@2.1.0/libraries/PDM/src/PDM.h:32:2: warning: #warning "Mic DATA pin not defined in variant. Using default." [-Wcpp]
   32 | #warning "Mic DATA pin not defined in variant. Using default."
      |  ^~~~~~~
/home/eng-nbb/.platformio/packages/framework-arduinoapollo3@2.1.0/libraries/PDM/src/PDM.h:37:2: warning: #warning "Mic CLOCK pin not defined in variant. Using default." [-Wcpp]
   37 | #warning "Mic CLOCK pin not defined in variant. Using default."
      |  ^~~~~~~
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/RTC/RTC.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/Servo/Servo.cpp.o
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libSoftwareSerial.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libSoftwareSerial.a
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/SPI/SPI.cpp.o
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libmbed_bridge.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libmbed_bridge.a
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/Wire/Wire.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/WDT/WDT.cpp.o
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libEEPROM.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libEEPROM.a
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/BurstMode/BurstMode.cpp.o
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libPDM.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libPDM.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libcore-implement.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libcore-implement.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libRTC.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libRTC.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libBurstMode.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libBurstMode.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libServo.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libServo.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libSPI.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libSPI.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libWDT.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libWDT.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libWire.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libWire.a
Linking .pio/build/SparkFun_RedBoard_Artemis_ATP/program
arm-none-eabi-objcopy -O binary .pio/build/SparkFun_RedBoard_Artemis_ATP/program .pio/build/SparkFun_RedBoard_Artemis_ATP/firmware.bin
Checking size .pio/build/SparkFun_RedBoard_Artemis_ATP/program
Advanced Memory Usage is available via "PlatformIO Home > Project Inspect"
RAM:   [=         ]   7.5% (used 29384 bytes from 393216 bytes)
Flash: [=         ]  12.0% (used 117700 bytes from 983040 bytes)
Configuring upload protocol...
AVAILABLE: asb, jlink, svl
CURRENT: upload_protocol = jlink
Looking for upload port...

Warning! Your `/etc/udev/rules.d/99-platformio-udev.rules` are outdated. Please update or reinstall them.
More details: https://docs.platformio.org/page/faq.html#platformio-udev-rules

Auto-detected: /dev/ttyUSB0
Uploading .pio/build/SparkFun_RedBoard_Artemis_ATP/firmware.bin
SEGGER J-Link Commander V7.20 (Compiled Apr 28 2021 17:38:41)
DLL version V7.20, compiled Apr 28 2021 17:38:26


J-Link Command File read successfully.
Processing script file...

J-Link connection not established yet but required for command.
Connecting to J-Link via USB...O.K.
Firmware: J-Link V11 compiled Jun  7 2021 15:48:52
Hardware version: V11.00
S/N: 261003515
License(s): FlashBP, GDB
OEM: SEGGER-EDU
VTref=3.328V
Target connection not established yet but required for command.
Device "AMA3B1KK-KBR" selected.


Connecting to target via SWD
Found SW-DP with ID 0x2BA01477
DPIDR: 0x2BA01477
Scanning AP map to find all available APs
AP[1]: Stopped AP scan as end of AP map has been reached
AP[0]: AHB-AP (IDR: 0x24770011)
Iterating through AP map to find AHB-AP to use
AP[0]: Core found
AP[0]: AHB-AP ROM base: 0xE00FF000
CPUID register: 0x410FC241. Implementer code: 0x41 (ARM)
Found Cortex-M4 r0p1, Little endian.
FPUnit: 6 code (BP) slots and 2 literal slots
CoreSight components:
ROMTbl[0] @ E00FF000
ROMTbl[0][0]: E000E000, CID: B105E00D, PID: 000BB00C SCS-M7
ROMTbl[0][1]: E0001000, CID: B105E00D, PID: 003BB002 DWT
ROMTbl[0][2]: E0002000, CID: B105E00D, PID: 002BB003 FPB
ROMTbl[0][3]: E0000000, CID: B105E00D, PID: 003BB001 ITM
ROMTbl[0][4]: E0040000, CID: B105900D, PID: 000BB9A1 TPIU
Cortex-M4 identified.
PC = 00021194, CycleCnt = 00105BCD
R0 = 00000000, R1 = 00000001, R2 = 100042A8, R3 = 00000001
R4 = 100002DC, R5 = 00000000, R6 = 00000000, R7 = 00000000
R8 = 00000000, R9 = 00000000, R10= 00000000, R11= 00000000
R12= 00000000
SP(R13)= 10004AA0, MSP= 1005FF70, PSP= 10004AA0, R14(LR) = 0002220D
XPSR = 01000000: APSR = nzcvq, EPSR = 01000000, IPSR = 000 (NoException)
CFBP = 02000001, CONTROL = 02, FAULTMASK = 00, BASEPRI = 00, PRIMASK = 01

FPS0 = 00000000, FPS1 = 00000000, FPS2 = 00000000, FPS3 = 00000000
FPS4 = 00000000, FPS5 = 00000000, FPS6 = 00000000, FPS7 = 00000000
FPS8 = 00000000, FPS9 = 00000000, FPS10= 00000000, FPS11= 00000000
FPS12= 00000000, FPS13= 00000000, FPS14= 00000000, FPS15= 00000000
FPS16= 00000000, FPS17= 00000000, FPS18= 00000000, FPS19= 00000000
FPS20= 00000000, FPS21= 00000000, FPS22= 00000000, FPS23= 00000000
FPS24= 00000000, FPS25= 00000000, FPS26= 00000000, FPS27= 00000000
FPS28= 00000000, FPS29= 00000000, FPS30= 00000000, FPS31= 00000000
FPSCR= 02000000

Downloading file [.pio/build/SparkFun_RedBoard_Artemis_ATP/firmware.bin]...
J-Link: Flash download: Bank 0 @ 0x0000C000: Skipped. Contents already match
O.K.

Reset delay: 0 ms
Reset type NORMAL: Resets core & peripherals via SYSRESETREQ & VECTRESET bit.
ResetTarget() start
JDEC PID 0x000000CF
Ambiq Apollo3 ResetTarget
Bootldr = 0x04000000
Secure Part.
Secure Chip. Bootloader needs to run which will then halt when finish.
CPU halted after reset. TryCount = 0x00000000
ResetTarget() end


Script processing completed.

============================================================================= [SUCCESS] Took 15.83 seconds =============================================================================
en
```

#Debug Firmware
We need to add `debug_tool = jlink` to our `platformio.ini` file, so that this:
```ini
; PlatformIO Project Configuration File
;
;   Build options: build flags, source filter
;   Upload options: custom upload port, speed and extra flags
;   Library options: dependencies, extra library storages
;   Advanced options: extra scripting
;
; Please visit documentation for the other options and examples
; https://docs.platformio.org/page/projectconf.html

[env:SparkFun_RedBoard_Artemis_ATP]
platform = apollo3blue
board = SparkFun_Artemis_Nano
framework = arduino
platform_packages = framework-arduinoapollo3@2.1.0
upload_protocol = jlink
```

Becomes this:

```ini
; PlatformIO Project Configuration File
;
;   Build options: build flags, source filter
;   Upload options: custom upload port, speed and extra flags
;   Library options: dependencies, extra library storages
;   Advanced options: extra scripting
;
; Please visit documentation for the other options and examples
; https://docs.platformio.org/page/projectconf.html

[env:SparkFun_RedBoard_Artemis_ATP]
platform = apollo3blue
board = SparkFun_Artemis_Nano
framework = arduino
platform_packages = framework-arduinoapollo3@2.1.0
upload_protocol = jlink
debug_tool = jlink
```


```
$> platformio debug --interface=gdb -x .pioinit
Preparing firmware for debugging...
Processing SparkFun_RedBoard_Artemis_ATP (platform: apollo3blue; board: SparkFun_RedBoard_Artemis_ATP; framework: arduino)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
CONFIGURATION: https://docs.platformio.org/page/boards/apollo3blue/SparkFun_RedBoard_Artemis_ATP.html
PLATFORM: Apollo 3 Blue (0.0.2) > SparkFun RedBoard Artemis ATP
HARDWARE: AMA3B1KK 48MHz, 384KB RAM, 960KB Flash
DEBUG: Current (jlink) External (jlink)
PACKAGES: 
 - framework-arduinoapollo3 2.1.0 
 - toolchain-gccarmnoneeabi 1.90301.200702 (9.3.1)
LDF: Library Dependency Finder -> http://bit.ly/configure-pio-ldf
LDF Modes: Finder ~ chain, Compatibility ~ soft
Found 0 compatible libraries
Scanning dependencies...
No dependencies
Building in debug mode
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/src/main.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/variant/config/pins.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/variant/variant.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/bridge/pins.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-api/api/Common.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-api/api/IPAddress.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-api/api/PluggableUSB.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-api/api/Print.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-api/api/Stream.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-api/api/String.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonAnalog.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonDigital.cpp.o
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libvariant.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libvariant.a
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonInit.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonInterrupt.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonMath.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonPulse.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonTiming.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/HardwareSerial.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/Yield.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/itoa.c.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/main.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/core-implement/CommonAnalog.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/core-implement/CommonPulse.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/EEPROM/EEPROM.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/PDM/PDM.cpp.o
In file included from /home/eng-nbb/.platformio/packages/framework-arduinoapollo3@2.1.0/libraries/PDM/src/PDM.cpp:22:
/home/eng-nbb/.platformio/packages/framework-arduinoapollo3@2.1.0/libraries/PDM/src/PDM.h:32:2: warning: #warning "Mic DATA pin not defined in variant. Using default." [-Wcpp]
   32 | #warning "Mic DATA pin not defined in variant. Using default."
      |  ^~~~~~~
/home/eng-nbb/.platformio/packages/framework-arduinoapollo3@2.1.0/libraries/PDM/src/PDM.h:37:2: warning: #warning "Mic CLOCK pin not defined in variant. Using default." [-Wcpp]
   37 | #warning "Mic CLOCK pin not defined in variant. Using default."
      |  ^~~~~~~
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/RTC/RTC.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/Servo/Servo.cpp.o
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libSoftwareSerial.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libSoftwareSerial.a
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/SPI/SPI.cpp.o
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libmbed_bridge.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libmbed_bridge.a
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/Wire/Wire.cpp.o
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/WDT/WDT.cpp.o
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libEEPROM.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libEEPROM.a
Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/BurstMode/BurstMode.cpp.o
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libPDM.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libPDM.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libcore-implement.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libcore-implement.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libRTC.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libRTC.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libWDT.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libWDT.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libServo.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libServo.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libSPI.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libSPI.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libBurstMode.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libBurstMode.a
Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libWire.a
Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libWire.a
Linking .pio/build/SparkFun_RedBoard_Artemis_ATP/program
arm-none-eabi-objcopy -O binary .pio/build/SparkFun_RedBoard_Artemis_ATP/program .pio/build/SparkFun_RedBoard_Artemis_ATP/firmware.bin
Checking size .pio/build/SparkFun_RedBoard_Artemis_ATP/program
Advanced Memory Usage is available via "PlatformIO Home > Project Inspect"
RAM:   [=         ]   7.5% (used 29384 bytes from 393216 bytes)
Flash: [=         ]  12.0% (used 117700 bytes from 983040 bytes)
Configuring upload protocol...
AVAILABLE: asb, jlink, svl
CURRENT: upload_protocol = jlink
Looking for upload port...

Warning! Your `/etc/udev/rules.d/99-platformio-udev.rules` are outdated. Please update or reinstall them.
More details: https://docs.platformio.org/page/faq.html#platformio-udev-rules

Auto-detected: /dev/ttyUSB0
Uploading .pio/build/SparkFun_RedBoard_Artemis_ATP/firmware.bin
SEGGER J-Link Commander V7.20 (Compiled Apr 28 2021 17:38:41)
DLL version V7.20, compiled Apr 28 2021 17:38:26


J-Link Command File read successfully.
Processing script file...

J-Link connection not established yet but required for command.
Connecting to J-Link via USB...O.K.
Firmware: J-Link V11 compiled Jun  7 2021 15:48:52
Hardware version: V11.00
S/N: 261003515
License(s): FlashBP, GDB
OEM: SEGGER-EDU
VTref=3.328V
Target connection not established yet but required for command.
Device "AMA3B1KK-KBR" selected.


Connecting to target via SWD
Found SW-DP with ID 0x2BA01477
DPIDR: 0x2BA01477
Scanning AP map to find all available APs
AP[1]: Stopped AP scan as end of AP map has been reached
AP[0]: AHB-AP (IDR: 0x24770011)
Iterating through AP map to find AHB-AP to use
AP[0]: Core found
AP[0]: AHB-AP ROM base: 0xE00FF000
CPUID register: 0x410FC241. Implementer code: 0x41 (ARM)
Found Cortex-M4 r0p1, Little endian.
FPUnit: 6 code (BP) slots and 2 literal slots
CoreSight components:
ROMTbl[0] @ E00FF000
ROMTbl[0][0]: E000E000, CID: B105E00D, PID: 000BB00C SCS-M7
ROMTbl[0][1]: E0001000, CID: B105E00D, PID: 003BB002 DWT
ROMTbl[0][2]: E0002000, CID: B105E00D, PID: 002BB003 FPB
ROMTbl[0][3]: E0000000, CID: B105E00D, PID: 003BB001 ITM
ROMTbl[0][4]: E0040000, CID: B105900D, PID: 000BB9A1 TPIU
Cortex-M4 identified.
PC = 00021192, CycleCnt = 00F56922
R0 = 00000000, R1 = 00000001, R2 = 100042A8, R3 = 000221ED
R4 = 100002DC, R5 = 00000000, R6 = 00000000, R7 = 00000000
R8 = 00000000, R9 = 00000000, R10= 00000000, R11= 00000000
R12= 00000000
SP(R13)= 10004AA0, MSP= 1005FF70, PSP= 10004AA0, R14(LR) = 0002220D
XPSR = 01000000: APSR = nzcvq, EPSR = 01000000, IPSR = 000 (NoException)
CFBP = 02000001, CONTROL = 02, FAULTMASK = 00, BASEPRI = 00, PRIMASK = 01

FPS0 = 00000000, FPS1 = 00000000, FPS2 = 00000000, FPS3 = 00000000
FPS4 = 00000000, FPS5 = 00000000, FPS6 = 00000000, FPS7 = 00000000
FPS8 = 00000000, FPS9 = 00000000, FPS10= 00000000, FPS11= 00000000
FPS12= 00000000, FPS13= 00000000, FPS14= 00000000, FPS15= 00000000
FPS16= 00000000, FPS17= 00000000, FPS18= 00000000, FPS19= 00000000
FPS20= 00000000, FPS21= 00000000, FPS22= 00000000, FPS23= 00000000
FPS24= 00000000, FPS25= 00000000, FPS26= 00000000, FPS27= 00000000
FPS28= 00000000, FPS29= 00000000, FPS30= 00000000, FPS31= 00000000
FPSCR= 02000000

Downloading file [.pio/build/SparkFun_RedBoard_Artemis_ATP/firmware.bin]...
J-Link: Flash download: Bank 0 @ 0x0000C000: 1 range affected (8192 bytes)
J-Link: Flash download: Total: 0.322s (Prepare: 0.060s, Compare: 0.180s, Erase: 0.022s, Program & Verify: 0.054s, Restore: 0.005s)
J-Link: Flash download: Program & Verify speed: 147 KB/s
O.K.

Reset delay: 0 ms
Reset type NORMAL: Resets core & peripherals via SYSRESETREQ & VECTRESET bit.
ResetTarget() start
JDEC PID 0x000000CF
Ambiq Apollo3 ResetTarget
Bootldr = 0x04000000
Secure Part.
Secure Chip. Bootloader needs to run which will then halt when finish.
CPU halted after reset. TryCount = 0x00000000
ResetTarget() end


Script processing completed.

============================================================================= [SUCCESS] Took 16.81 seconds =============================================================================
SEGGER J-Link GDB Server V7.20 Command Line Version

JLinkARM.dll V7.20 (DLL compiled Apr 28 2021 17:38:26)

Command line: -singlerun -if SWD -select USB -device AMA3B1KK-KBR -port 2331
-----GDB Server start settings-----
GDBInit file:                  none
GDB Server Listening port:     2331
SWO raw output listening port: 2332
Terminal I/O port:             2333
Accept remote connection:      yes
Generate logfile:              off
Verify download:               off
Init regs on start:            off
Silent mode:                   off
Single run mode:               on
Target connection timeout:     0 ms
------J-Link related settings------
J-Link Host interface:         USB
J-Link script:                 none
J-Link settings file:          none
------Target related settings------
Target device:                 AMA3B1KK-KBR
Target interface:              SWD
Target interface speed:        4000kHz
Target endian:                 little

Connecting to J-Link...
J-Link is connected.
Firmware: J-Link V11 compiled Jun  7 2021 15:48:52
Hardware: V11.00
S/N: 261003515
OEM: SEGGER-EDU
Feature(s): FlashBP, GDB
Checking target voltage...
Target voltage: 3.33 V
Listening on TCP/IP port 2331
Connecting to target...
Connected to target
Waiting for GDB connection...Reading symbols from /home/eng-nbb/projects/ucontroller/Apollo3/Serial_Test_1/.pio/build/SparkFun_RedBoard_Artemis_ATP/program...
PlatformIO Unified Debugger -> http://bit.ly/pio-debug
PlatformIO: debug_tool = jlink
PlatformIO: Initializing remote target...
Connected to 127.0.0.1
Reading all registers
Read 4 bytes @ address 0x0002119A (Data = 0xF7FFB90B)
Read 2 bytes @ address 0x0002119A (Data = 0xB90B)
0x0002119a in core_util_critical_section_exit ()
Reading 64 bytes @ address 0x00021180
Read 4 bytes @ address 0x000211A4 (Data = 0x100042A8)
Received monitor command: clrbp
Received monitor command: speed auto
Select auto target interface speed (2000 kHz)
Select auto target interface speed (2000 kHz)
Received monitor command: reset
Resetting target
Received monitor command: halt
Halting target CPU...
...Target halted (PC = 0x000008BE)
Resetting target
Downloading 16128 bytes @ address 0x00010000
Downloading 16000 bytes @ address 0x00013F00
Downloading 15968 bytes @ address 0x00017D80
Downloading 15920 bytes @ address 0x0001BBE0
Downloading 16016 bytes @ address 0x0001FA10
Downloading 15968 bytes @ address 0x000238A0
Downloading 16224 bytes @ address 0x00027700
Downloading 5476 bytes @ address 0x0002B660
Downloading 8 bytes @ address 0x0002CBC4
Downloading 5224 bytes @ address 0x0002CBD0
Writing register (PC = 0x   23ffc)
Loading section .text, size 0x1cbc4 lma 0x10000
Loading section .ARM.exidx, size 0x8 lma 0x2cbc4
Loading section .data, size 0x1468 lma 0x2cbd0
Start address 0x23ffc, load size 122932
Transfer rate: 15006 KB/sec, 12293 bytes/write.
Read 4 bytes @ address 0x00023FFC (Data = 0x490E480D)
Read 2 bytes @ address 0x00023FFC (Data = 0x480D)
Reading 64 bytes @ address 0x00026F00
Read 2 bytes @ address 0x00026F2C (Data = 0xB508)
Temporary breakpoint 1 at 0x26f2c: file /home/eng-nbb/.platformio/packages/framework-arduinoapollo3@2.1.0/cores/arduino/mbed-bridge/main.cpp, line 10.
PlatformIO: Initialization completed
(gdb) PlatformIO: Resume the execution to `debug_init_break = tbreak main`
PlatformIO: More configuration options -> http://bit.ly/pio-debug
Continuing.
Setting breakpoint @ address 0x00026F2C, Size = 2, BPHandle = 0x0001
Starting target CPU...
...Breakpoint reached @ address 0x00026F2C
Reading all registers
Removing breakpoint @ address 0x00026F2C, Size = 2
Read 4 bytes @ address 0x00026F2C (Data = 0xF000B508)

Temporary breakpoint 1, main ()
    at /home/eng-nbb/.platformio/packages/framework-arduinoapollo3@2.1.0/cores/arduino/mbed-bridge/main.cpp:10
10	  init();
(gdb) 

```
