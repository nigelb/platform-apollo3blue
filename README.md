# platform-apollo3blue
This is an experimental platform to allow the use of [SparkFun's Arduino framework](https://github.com/sparkfun/Arduino_Apollo3) in PlatformIO.

# How To Use This
As this is experimental, it requires a manual install.

# Supported Versions of [sparkfun/Arduino_Apollo3](/sparkfun/Arduino_Apollo3)
The master branch now supports both the Core_V2 and the Core_V1 versions. 

platform-apollo3blue now supports the following 

1. Frameworks:
    * Arduino - [sparkfun/Arduino_Apollo3](https://github.com/sparkfun/Arduino_Apollo3)
        * [Core V1](https://github.com/sparkfun/Arduino_Apollo3/tree/v1)
        * [Core V2]([Core V1](https://github.com/sparkfun/Arduino_Apollo3))
    * Ambiq Suit SDK - [sparkfun/AmbiqSuiteSDK](https://github.com/sparkfun/AmbiqSuiteSDK.git)
2. Tools:
    * Segger [JLink](https://www.segger.com/products/debug-probes/j-link/) or [platformio](https://docs.platformio.org/en/latest/plus/debug-tools/jlink.html)
        * [Upload protocol](docs/platform-apollp3blue/docs/platform-apollo3blue/UsingSeggerJLink.md#upload-firmware) 
        * [Debugger](docs/platform-apollp3blue/docs/platform-apollo3blue/UsingSeggerJLink.md#debug-firmware)

To specify which framework and version to use, see [below](#specifying-the-version-of-sparkfunarduino_apollo3) or a more detailed [example](docs/platform-apollo3blue/UsingMultipleVersionsOfArduino_Apollo3.md).
    
## Install
Locate your .platformio directory which it typically in your home directory:

    $> cd .platformio

Clone [SparkFun's Arduino framework](https://github.com/sparkfun/Arduino_Apollo3):

    ~/.platformio> cd packages
    ~/.platformio>/packages> git clone --recurse-submodules --branch v2.1.0 https://github.com/sparkfun/Arduino_Apollo3.git framework-arduinoapollo3@2.1.0

Create a `package.json` file in the directory you just cloned `.platformio/packages/framework-arduinoapollo3@2.1.0/` with the following contents:

```json
{
    "name": "framework-arduinoapollo3",
    "description": "An mbed-os enabled Arduino core for Ambiq Apollo3 based boards",
    "version": "2.1.0",
    "url": "https://github.com/sparkfun/Arduino_Apollo3"
}
```

Checkout [platform-apollo3blue](https://github.com/nigelb/platform-apollo3blue):

    ~> cd ~/.platformio
    ~/.platformio> cd platforms
    ~/.platformio/platforms> git clone https://github.com/nigelb/platform-apollo3blue.git apollo3blue
    
    
## Verify the Install
You should have a number of Artemis boards show up in your board list:

    $> platformio boards

    .
    .
    .
    
	Platform: apollo3blue
	==================================================================================================================
	ID                                   MCU       Frequency    Flash    RAM    Name
	-----------------------------------  --------  -----------  -------  -----  -------------------------------------
	SparkFun_Artemis_Development_Kit     AMA3B1KK  48MHz        960KB    384KB  SparkFun Artemis Development Kit
	SparkFun_Artemis_Module              AMA3B1KK  48MHz        960KB    384KB  SparkFun Artemis Module
	SparkFun_Thing_Plus                  AMA3B1KK  48MHz        960KB    384KB  SparkFun Artemis Thing Plus
	SparkFun_Edge                        AMA3B1KK  48MHz        960KB    384KB  SparkFun Edge
	SparkFun_Edge2                       AMA3B1KK  48MHz        960KB    384KB  SparkFun Edge2
	SparkFun_Thing_Plus_expLoRaBLE       AMA3B1KK  48MHz        960KB    384KB  SparkFun LoRa Thing Plus - expLoRaBLE
	SparkFun_MicroMod_Artemis_Processor  AMA3B1KK  48MHz        960KB    384KB  SparkFun MicroMod Artemis Processor
	SparkFun_RedBoard_Artemis            AMA3B1KK  48MHz        960KB    384KB  SparkFun RedBoard Artemis
	SparkFun_RedBoard_Artemis_ATP        AMA3B1KK  48MHz        960KB    384KB  SparkFun RedBoard Artemis ATP
	SparkFun_Artemis_Nano                AMA3B1KK  48MHz        960KB    384KB  SparkFun RedBoard Artemis Nano
    
    .
    .
    .    
Or query the platform directly:

    $> platformio platform show apollo3blue

    apollo3blue ~ Apollo 3 Blue
    ===========================
    The Apollo MCU Family is an ultra-low power, highly integrated microcontroller platform based on Ambiq Micro’s patented Sub-threshold Power Optimized Technology (SPOT™) and designed for battery-powered and portable, mobile devices.
    
    Version: 0.0.2
    Repository: https://github.com/nigelb/platform-apollo3blue.git
    License: Apache-2.0
    Frameworks: ambiqsdk-sfe, arduino
    
    Packages
    --------
    
    Package toolchain-gccarmnoneeabi
    --------------------------------
    Type: toolchain
    Requirements: >=1.9
    Installed: Yes
    Version: 1.90301.200702
    Original version: 9.3.1
    Description: GNU toolchain for Arm Cortex-M and Cortex-R processors
    
    Package framework-arduinoapollo3
    --------------------------------
    Type: framework
    Requirements: 2.1.0
    Installed: Yes
    Version: 2.1.0
    Original version: None
    Description: An mbed-os enabled Arduino core for Ambiq Apollo3 based boards
    
    Package framework-ambiqsuitesdkapollo3-sfe
    ------------------------------------------
    Type: framework
    Requirements: 2.4.2
    Installed: Yes
    Version: 2.4.2
    Original version: None
    Description: SparkFun's AmbiqSuiteSDK repository.
    
    Package tool-jlink
    ------------------
    Type: uploader
    Requirements: ^1.63208.0
    Installed: Yes
    Version: 1.72000.0
    Original version: 7.20.0
    Description: Software and Documentation Pack for SEGGER J-Link debug probes
    
    Boards
    ------
    ID                                   MCU       Frequency    Flash    RAM    Name
    -----------------------------------  --------  -----------  -------  -----  -------------------------------------
    SparkFun_Artemis_Development_Kit     AMA3B1KK  48MHz        960KB    384KB  SparkFun Artemis Development Kit
    SparkFun_Artemis_Module              AMA3B1KK  48MHz        960KB    384KB  SparkFun Artemis Module
    SparkFun_Edge                        AMA3B1KK  48MHz        960KB    384KB  SparkFun Edge
    SparkFun_Edge2                       AMA3B1KK  48MHz        960KB    384KB  SparkFun Edge2
    SparkFun_MicroMod_Artemis_Processor  AMA3B1KK  48MHz        960KB    384KB  SparkFun MicroMod Artemis Processor
    SparkFun_RedBoard_Artemis            AMA3B1KK  48MHz        960KB    384KB  SparkFun RedBoard Artemis
    SparkFun_RedBoard_Artemis_ATP        AMA3B1KK  48MHz        960KB    384KB  SparkFun RedBoard Artemis ATP
    SparkFun_Redboard_Artemis_Nano       AMA3B1KK  48MHz        960KB    384KB  SparkFun RedBoard Artemis Nano
    SparkFun_Thing_Plus                  AMA3B1KK  48MHz        960KB    384KB  SparkFun Artemis Thing Plus
    SparkFun_Thing_Plus_expLoRaBLE       AMA3B1KK  48MHz        960KB    384KB  SparkFun LoRa Thing Plus - expLoRaBLE



## Create a project
We can now create a project and compile the source:

    ~> mkdir SparkFun_Artemis_Nano
    ~> cd SparkFun_Artemis_Nano
    ~/SparkFun_Artemis_Nano> platformio init --board SparkFun_Artemis_Nano
    
    The current working directory /home/user/SparkFun_Artemis_Nano will be used for the project.

    The next files/directories have been created in /home/user/SparkFun_Artemis_Nano
    include - Put project header files here
    lib - Put here project specific (private) libraries
    src - Put project source files here
    platformio.ini - Project Configuration File
    
    Project has been successfully initialized! Useful commands:
    `pio run` - process/build project from the current directory
    `pio run --target upload` or `pio run -t upload` - upload firmware to a target
    `pio run --target clean` - clean project (remove compiled files)
    `pio run --help` - additional information

### Specifying the version of sparkfun/Arduino_Apollo3
After we have initialized the project the `platform.ini` file is:

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

[env:SparkFun_Artemis_Nano]
platform = apollo3blue
board = SparkFun_Artemis_Nano
framework = arduino
```

To specify which version of sparkfun/Arduino_Apollo3 to use we need to add a `platform_packages` directive:

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

[env:SparkFun_Artemis_Nano]
platform = apollo3blue
board = SparkFun_Artemis_Nano
framework = arduino
platform_packages = framework-arduinoapollo3@2.1.0
```

Then we can create our test file `src/SparkFun_Artemis_Nano.cpp` with the contents:

```cxx
#include "Arduino.h"

void setup()
{
    Serial.begin(115200);
    Serial.println("Hello World!");
};

void loop()
{
};
```

Then we can compile:

```
~/SparkFun_Artemis_Nano> platformio run
Processing SparkFun_Artemis_Nano (platform: apollo3blue; board: SparkFun_Artemis_Nano; framework: arduino)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
CONFIGURATION: https://docs.platformio.org/page/boards/apollo3blue/SparkFun_Artemis_Nano.html
PLATFORM: Apollo 3 Blue (0.0.2) > SparkFun RedBoard Artemis Nano
HARDWARE: AMA3B1KK 48MHz, 384KB RAM, 960KB Flash
PACKAGES: 
 - framework-arduinoapollo3 2.1.0 
 - toolchain-gccarmnoneeabi 1.90301.200702 (9.3.1)
LDF: Library Dependency Finder -> http://bit.ly/configure-pio-ldf
LDF Modes: Finder ~ chain, Compatibility ~ soft
Found 0 compatible libraries
Scanning dependencies...
No dependencies
Building in release mode
Compiling .pio/build/SparkFun_Artemis_Nano/src/main.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/variant/config/pins.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/variant/variant.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/bridge/pins.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-api/api/Common.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-api/api/IPAddress.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-api/api/PluggableUSB.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-api/api/Print.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-api/api/Stream.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-api/api/String.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-implement/CommonAnalog.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-implement/CommonDigital.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-implement/CommonInit.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-implement/CommonInterrupt.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-implement/CommonMath.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-implement/CommonPulse.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-implement/CommonTiming.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-implement/HardwareSerial.cpp.o
Archiving .pio/build/SparkFun_Artemis_Nano/libvariant.a
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-implement/Yield.cpp.o
Indexing .pio/build/SparkFun_Artemis_Nano/libvariant.a
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/core-implement/itoa.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/mbed_bridge/main.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/core-implement/CommonAnalog.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/core-implement/CommonPulse.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/EEPROM/EEPROM.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/PDM/PDM.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/RTC/RTC.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/Servo/Servo.cpp.o
Archiving .pio/build/SparkFun_Artemis_Nano/libSoftwareSerial.a
Indexing .pio/build/SparkFun_Artemis_Nano/libSoftwareSerial.a
Compiling .pio/build/SparkFun_Artemis_Nano/SPI/SPI.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/Wire/Wire.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/WDT/WDT.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/BurstMode/BurstMode.cpp.o
In file included from /home/nigelb/.platformio/packages/framework-arduinoapollo3@2.1.0/libraries/PDM/src/PDM.cpp:22:
/home/nigelb/.platformio/packages/framework-arduinoapollo3@2.1.0/libraries/PDM/src/PDM.h:32:2: warning: #warning "Mic DATA pin not defined in variant. Using default." [-Wcpp]
   32 | #warning "Mic DATA pin not defined in variant. Using default."
      |  ^~~~~~~
/home/nigelb/.platformio/packages/framework-arduinoapollo3@2.1.0/libraries/PDM/src/PDM.h:37:2: warning: #warning "Mic CLOCK pin not defined in variant. Using default." [-Wcpp]
   37 | #warning "Mic CLOCK pin not defined in variant. Using default."
      |  ^~~~~~~
Archiving .pio/build/SparkFun_Artemis_Nano/libmbed_bridge.a
Indexing .pio/build/SparkFun_Artemis_Nano/libmbed_bridge.a
Archiving .pio/build/SparkFun_Artemis_Nano/libEEPROM.a
Archiving .pio/build/SparkFun_Artemis_Nano/libServo.a
Indexing .pio/build/SparkFun_Artemis_Nano/libEEPROM.a
Indexing .pio/build/SparkFun_Artemis_Nano/libServo.a
Archiving .pio/build/SparkFun_Artemis_Nano/libRTC.a
Indexing .pio/build/SparkFun_Artemis_Nano/libRTC.a
Archiving .pio/build/SparkFun_Artemis_Nano/libPDM.a
Indexing .pio/build/SparkFun_Artemis_Nano/libPDM.a
Archiving .pio/build/SparkFun_Artemis_Nano/libWire.a
Indexing .pio/build/SparkFun_Artemis_Nano/libWire.a
Archiving .pio/build/SparkFun_Artemis_Nano/libSPI.a
Indexing .pio/build/SparkFun_Artemis_Nano/libSPI.a
Archiving .pio/build/SparkFun_Artemis_Nano/libcore-implement.a
Archiving .pio/build/SparkFun_Artemis_Nano/libWDT.a
Indexing .pio/build/SparkFun_Artemis_Nano/libcore-implement.a
Indexing .pio/build/SparkFun_Artemis_Nano/libWDT.a
Archiving .pio/build/SparkFun_Artemis_Nano/libBurstMode.a
Indexing .pio/build/SparkFun_Artemis_Nano/libBurstMode.a
Linking .pio/build/SparkFun_Artemis_Nano/program
arm-none-eabi-objcopy -O binary .pio/build/SparkFun_Artemis_Nano/program .pio/build/SparkFun_Artemis_Nano/firmware.bin
Checking size .pio/build/SparkFun_Artemis_Nano/program
Advanced Memory Usage is available via "PlatformIO Home > Project Inspect"
RAM:   [=         ]   7.5% (used 29384 bytes from 393216 bytes)
Flash: [=         ]  11.9% (used 117248 bytes from 983040 bytes)
======================================================================= [SUCCESS] Took 2.42 seconds =======================================================================

```
  
## Uploading
The device port is now automatically detected. However, one can also specifiy it manually by editing the `platformio.ini` file and adding the `upload_port` and `upload_speed` fields. For example starting with Starting with:

```ini
;PlatformIO Project Configuration File
;
;   Build options: build flags, source filter
;   Upload options: custom upload port, speed and extra flags
;   Library options: dependencies, extra library storages
;   Advanced options: extra scripting
;
; Please visit documentation for the other options and examples
; https://docs.platformio.org/page/projectconf.html

[env:SparkFun_Artemis_Nano]
platform = apollo3blue
board = SparkFun_Artemis_Nano
framework = arduino
platform_packages = framework-arduinoapollo3@2.1.0
```

and endng up with:
```ini
;PlatformIO Project Configuration File
;
;   Build options: build flags, source filter
;   Upload options: custom upload port, speed and extra flags
;   Library options: dependencies, extra library storages
;   Advanced options: extra scripting
;
; Please visit documentation for the other options and examples
; https://docs.platformio.org/page/projectconf.html

[env:SparkFun_Artemis_Nano]
platform = apollo3blue
board = SparkFun_Artemis_Nano
framework = arduino
platform_packages = framework-arduinoapollo3@2.1.0
upload_port = /dev/ttyUSB0
upload_speed = 115200
```

Then we can upload the firmware:
```bash
~/SparkFun_Artemis_Nano> platformio run -t upload -v
Processing SparkFun_Artemis_Nano (platform: apollo3blue; board: SparkFun_Artemis_Nano; framework: arduino)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
CONFIGURATION: https://docs.platformio.org/page/boards/apollo3blue/SparkFun_Artemis_Nano.html
PLATFORM: Apollo 3 Blue (0.0.2) > SparkFun RedBoard Artemis Nano
HARDWARE: AMA3B1KK 48MHz, 384KB RAM, 960KB Flash
PACKAGES: 
 - framework-arduinoapollo3 2.1.0 
 - toolchain-gccarmnoneeabi 1.90301.200702 (9.3.1)
LDF: Library Dependency Finder -> http://bit.ly/configure-pio-ldf
LDF Modes: Finder ~ chain, Compatibility ~ soft
Found 0 compatible libraries
Scanning dependencies...
No dependencies
Building in release mode
Checking size .pio/build/SparkFun_Artemis_Nano/program
Advanced Memory Usage is available via "PlatformIO Home > Project Inspect"
RAM:   [=         ]   7.5% (used 29384 bytes from 393216 bytes)
Flash: [=         ]  11.9% (used 117248 bytes from 983040 bytes)
Configuring upload protocol...
AVAILABLE: asb, svl
CURRENT: upload_protocol = svl
Looking for upload port...

Warning! Please install `99-platformio-udev.rules`. 
More details: https://docs.platformio.org/page/faq.html#platformio-udev-rules

Auto-detected: /dev/ttyUSB0
Uploading .pio/build/SparkFun_Artemis_Nano/firmware.bin


Artemis SVL Bootloader
Script version 1.7

Phase:	Setup
	Cleared startup blip
	Got SVL Bootloader Version: 5
	Sending 'enter bootloader' command

Phase:	Bootload
	have 122480 bytes to send in 60 frames
	Sending frame #1, length: 2048
	Sending frame #2, length: 2048
	Sending frame #3, length: 2048
	Sending frame #4, length: 2048
	Sending frame #5, length: 2048
	Sending frame #6, length: 2048
	Sending frame #7, length: 2048
	Sending frame #8, length: 2048
	Sending frame #9, length: 2048
	Sending frame #10, length: 2048
	Sending frame #11, length: 2048
	Sending frame #12, length: 2048
	Sending frame #13, length: 2048
	Sending frame #14, length: 2048
	Sending frame #15, length: 2048
	Sending frame #16, length: 2048
	Sending frame #17, length: 2048
	Sending frame #18, length: 2048
	Sending frame #19, length: 2048
	Sending frame #20, length: 2048
	Sending frame #21, length: 2048
	Sending frame #22, length: 2048
	Sending frame #23, length: 2048
	Sending frame #24, length: 2048
	Sending frame #25, length: 2048
	Sending frame #26, length: 2048
	Sending frame #27, length: 2048
	Sending frame #28, length: 2048
	Sending frame #29, length: 2048
	Sending frame #30, length: 2048
	Sending frame #31, length: 2048
	Sending frame #32, length: 2048
	Sending frame #33, length: 2048
	Sending frame #34, length: 2048
	Sending frame #35, length: 2048
	Sending frame #36, length: 2048
	Sending frame #37, length: 2048
	Sending frame #38, length: 2048
	Sending frame #39, length: 2048
	Sending frame #40, length: 2048
	Sending frame #41, length: 2048
	Sending frame #42, length: 2048
	Sending frame #43, length: 2048
		Retrying...
	Sending frame #43, length: 2048
	Sending frame #44, length: 2048
	Sending frame #45, length: 2048
	Sending frame #46, length: 2048
	Sending frame #47, length: 2048
	Sending frame #48, length: 2048
	Sending frame #49, length: 2048
	Sending frame #50, length: 2048
	Sending frame #51, length: 2048
	Sending frame #52, length: 2048
	Sending frame #53, length: 2048
	Sending frame #54, length: 2048
	Sending frame #55, length: 2048
	Sending frame #56, length: 2048
	Sending frame #57, length: 2048
	Sending frame #58, length: 2048
	Sending frame #59, length: 2048
	Sending frame #60, length: 1648

	Upload complete

	Nominal bootload bps: 41819.66
======================================================================= [SUCCESS] Took 3.39 seconds =======================================================================
```
