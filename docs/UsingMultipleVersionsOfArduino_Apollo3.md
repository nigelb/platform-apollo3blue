# Using Multiple Versions of Arduino_Apollo3

## Install framework-arduinoapollo3@2.1.0

Locate your .platformio directory which it typically in your home directory:

    $> cd ~/.platformio
    ~/.platformio> cd packages
    ~/.platformio/packages> wget https://github.com/sparkfun/Arduino_Apollo3/releases/download/v2.1.0/Arduino_Apollo3.tar.gz
    ~/.platformio/packages> tar -xzf Arduino_Apollo3.tar.gz
    ~/.platformio/packages> mv Arduino_Apollo3 framework-arduinoapollo3@2.1.0

Create a the file `~/.platformio/packages/framework-arduinoapollo3@2.1.2/package.json` with the following contents:
```json
{
    "name": "framework-arduinoapollo3",
    "description": "An mbed-os enabled Arduino core for Ambiq Apollo3 based boards",
    "version": "2.1.0",
    "url": "https://github.com/sparkfun/Arduino_Apollo3"
}
```

## Install framework-arduinoapollo3@1.2.3

Locate your .platformio directory which it typically in your home directory:

    $> cd ~/.platformio
    ~/.platformio> cd packages
    ~/.platformio/packages> wget https://github.com/sparkfun/Arduino_Apollo3/archive/refs/tags/v1.2.3.tar.gz
    ~/.platformio/packages> tar -xzf v1.2.3.tar.gz
    ~/.platformio/packages> mv Arduino_Apollo3-1.2.3 framework-arduinoapollo3@1.2.3

Bump the version in the `~/.platformio/packages/framework-arduinoapollo3@1.2.3/package.json` file from

```json
{
    "name": "framework-arduinoapollo3",
    "description": "Arduino Wiring-based Framework (Apollo3 Core)",
    "version": "1.0.23",
    "url": "https://github.com/sparkfun/Arduino_Apollo3"
}
```

to:

```json
{
    "name": "framework-arduinoapollo3",
    "description": "Arduino Wiring-based Framework (Apollo3 Core)",
    "version": "1.2.3",
    "url": "https://github.com/sparkfun/Arduino_Apollo3"
}
```

# Create Projects

## Create Project 1
```bash
$> mkdir Serial_V1
$> cd Serial_V1
$> platformio init --board SparkFun_RedBoard_Artemis_ATP

The current working directory /home/user/projects/Serial_V1 will be used for the project.

The next files/directories have been created in /home/user/projects/Serial_V1
include - Put project header files here
lib - Put here project specific (private) libraries
src - Put project source files here
platformio.ini - Project Configuration File

Project has been successfully initialized! Useful commands:
`pio run` - process/build project from the current directory
`pio run --target upload` or `pio run -t upload` - upload firmware to a target
`pio run --target clean` - clean project (remove compiled files)
`pio run --help` - additional information
```

Add `platform_packages = framework-arduinoapollo3@1.2.3` to `platformio.ini`

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
board = SparkFun_RedBoard_Artemis_ATP
framework = arduino
platform_packages = framework-arduinoapollo3@1.2.3

```

Create program file `src/main.cpp`
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

## Create Project 2
```bash
$> mkdir Serial_V2
$> cd Serial_V2
$> platformio init --board SparkFun_RedBoard_Artemis_ATP

The current working directory /home/user/projects/Serial_V2 will be used for the project.

The next files/directories have been created in /home/user/projects/Serial_V2
include - Put project header files here
lib - Put here project specific (private) libraries
src - Put project source files here
platformio.ini - Project Configuration File

Project has been successfully initialized! Useful commands:
`pio run` - process/build project from the current directory
`pio run --target upload` or `pio run -t upload` - upload firmware to a target
`pio run --target clean` - clean project (remove compiled files)
`pio run --help` - additional information
```

Add `platform_packages = framework-arduinoapollo3@2.1.0` to `platformio.ini`

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
board = SparkFun_RedBoard_Artemis_ATP
framework = arduino
platform_packages = framework-arduinoapollo3@2.1.0

```

Create program file `src/main.cpp`
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

## Compile Project 1

Compile project:

    $> cd Serial_V1
    $>platformio run
    Processing SparkFun_RedBoard_Artemis_ATP (platform: apollo3blue; board: SparkFun_RedBoard_Artemis_ATP; framework: arduino)
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    CONFIGURATION: https://docs.platformio.org/page/boards/apollo3blue/SparkFun_RedBoard_Artemis_ATP.html
    PLATFORM: Apollo 3 Blue (0.0.2) > SparkFun RedBoard Artemis ATP
    HARDWARE: AMA3B1KK 48MHz, 384KB RAM, 960KB Flash
    PACKAGES: 
     - framework-arduinoapollo3 1.2.3 
     - toolchain-gccarmnoneeabi 1.90301.200702 (9.3.1)
    LDF: Library Dependency Finder -> http://bit.ly/configure-pio-ldf
    LDF Modes: Finder ~ chain, Compatibility ~ soft
    Found 0 compatible libraries
    Scanning dependencies...
    No dependencies
    Building in release mode
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/src/main.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/analog/ap3_analog.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/analog/ap3_analog_structures.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/ard_supers/IPAddress.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/ard_supers/Print.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/ard_supers/Stream.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/ard_supers/WMath.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/ard_supers/WString.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/ard_supers/avr/dtostrf.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/ard_supers/hooks.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/ard_supers/itoa.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/clock/ap3_clock_sources.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/debugging/ap3_debugging.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/gpio/ap3_gpio.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/gpio/ap3_gpio_structures.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/gpio/ap3_shift.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/initialization/ap3_initialization.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/iomaster/ap3_iomaster.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/iomaster/ap3_iomaster.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/main.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/timing/ap3_timing.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/uart/ap3_uart.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/FrameworkArduino/uart/ap3_uart_structures.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_adc.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_ble.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_ble_patch.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_ble_patch_b0.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_burst.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_cachectrl.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_clkgen.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_cmdq.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_ctimer.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_debug.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_flash.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_global.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_gpio.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_interrupt.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_iom.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_ios.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_itm.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_mcuctrl.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_mspi.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_pdm.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_pwrctrl.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_queue.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_reset.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_rtc.c.o
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libFrameworkArduino.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libFrameworkArduino.a
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_scard.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_secure_ota.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_security.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_stimer.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_sysctrl.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_systick.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_tpiu.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_uart.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_mcu/apollo3/hal/am_hal_wdt.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_devices/am_devices_button.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_devices/am_devices_led.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_utils/am_util_ble.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_utils/am_util_debug.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_utils/am_util_delay.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_utils/am_util_faultisr.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_utils/am_util_id.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_utils/am_util_regdump.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_utils/am_util_stdio.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_utils/am_util_string.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/apollo3_sdk_utils/am_util_time.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/variant/bsp/am_bsp.c.o
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libapollo3_sdk_devices.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libapollo3_sdk_devices.a
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/variant/bsp/am_bsp_pins.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/variant/config/variant.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/variant/startup/startup_gcc.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/EEPROM/EEPROM.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/PDM/PDM.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/RTC/RTC.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/Servo/Servo.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/SoftwareSerial/SoftwareSerial.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/SPI/SPI.cpp.o
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libapollo3_sdk_utils.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libapollo3_sdk_mcu.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libapollo3_sdk_utils.a
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/Wire/Wire.cpp.o
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libapollo3_sdk_mcu.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libvariant.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libvariant.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libRTC.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libRTC.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libEEPROM.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libEEPROM.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libServo.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libServo.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libWire.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libPDM.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libWire.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libPDM.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libSPI.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libSPI.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libSoftwareSerial.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libSoftwareSerial.a
    Linking .pio/build/SparkFun_RedBoard_Artemis_ATP/program
    Checking size .pio/build/SparkFun_RedBoard_Artemis_ATP/program
    Advanced Memory Usage is available via "PlatformIO Home > Project Inspect"
    RAM:   [===       ]  29.4% (used 115716 bytes from 393216 bytes)
    Flash: [          ]   0.8% (used 7404 bytes from 983040 bytes)
    arm-none-eabi-objcopy -O binary .pio/build/SparkFun_RedBoard_Artemis_ATP/program .pio/build/SparkFun_RedBoard_Artemis_ATP/firmware.bin
    ======================================================================= [SUCCESS] Took 1.39 seconds =======================================================================


## Compile Project 2

Compile project:

    $> cd Serial_V2
    $> platformio run
    Processing SparkFun_RedBoard_Artemis_ATP (platform: apollo3blue; board: SparkFun_RedBoard_Artemis_ATP; framework: arduino)
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Verbose mode can be enabled via `-v, --verbose` option
    CONFIGURATION: https://docs.platformio.org/page/boards/apollo3blue/SparkFun_RedBoard_Artemis_ATP.html
    PLATFORM: Apollo 3 Blue (0.0.2) > SparkFun RedBoard Artemis ATP
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
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonInit.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonInterrupt.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonMath.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonPulse.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/CommonTiming.cpp.o
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libvariant.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libvariant.a
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/HardwareSerial.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/Yield.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/core-implement/itoa.c.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/mbed_bridge/main.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/core-implement/CommonAnalog.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/core-implement/CommonPulse.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/EEPROM/EEPROM.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/PDM/PDM.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/RTC/RTC.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/Servo/Servo.cpp.o
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libSoftwareSerial.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libSoftwareSerial.a
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/SPI/SPI.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/Wire/Wire.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/WDT/WDT.cpp.o
    Compiling .pio/build/SparkFun_RedBoard_Artemis_ATP/BurstMode/BurstMode.cpp.o
    In file included from /home/nigelb/.platformio/packages/framework-arduinoapollo3@2.1.0/libraries/PDM/src/PDM.cpp:22:
    /home/nigelb/.platformio/packages/framework-arduinoapollo3@2.1.0/libraries/PDM/src/PDM.h:32:2: warning: #warning "Mic DATA pin not defined in variant. Using default." [-Wcpp]
       32 | #warning "Mic DATA pin not defined in variant. Using default."
          |  ^~~~~~~
    /home/nigelb/.platformio/packages/framework-arduinoapollo3@2.1.0/libraries/PDM/src/PDM.h:37:2: warning: #warning "Mic CLOCK pin not defined in variant. Using default." [-Wcpp]
       37 | #warning "Mic CLOCK pin not defined in variant. Using default."
          |  ^~~~~~~
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libPDM.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libPDM.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libWire.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libWire.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libmbed_bridge.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libmbed_bridge.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libBurstMode.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libEEPROM.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libBurstMode.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libRTC.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libEEPROM.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libRTC.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libSPI.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libServo.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libSPI.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libServo.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libWDT.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libWDT.a
    Archiving .pio/build/SparkFun_RedBoard_Artemis_ATP/libcore-implement.a
    Indexing .pio/build/SparkFun_RedBoard_Artemis_ATP/libcore-implement.a
    Linking .pio/build/SparkFun_RedBoard_Artemis_ATP/program
    Checking size .pio/build/SparkFun_RedBoard_Artemis_ATP/program
    arm-none-eabi-objcopy -O binary .pio/build/SparkFun_RedBoard_Artemis_ATP/program .pio/build/SparkFun_RedBoard_Artemis_ATP/firmware.bin
    Advanced Memory Usage is available via "PlatformIO Home > Project Inspect"
    RAM:   [=         ]   7.5% (used 29384 bytes from 393216 bytes)
    Flash: [=         ]  11.9% (used 117244 bytes from 983040 bytes)
    ======================================================================= [SUCCESS] Took 2.41 seconds =======================================================================


