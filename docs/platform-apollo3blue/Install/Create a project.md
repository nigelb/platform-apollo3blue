
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

If we want to specify a version other than the latest version of sparkfun/Arduino_Apollo3 to use we need to add a `platform_packages` directive:

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
  