# platform-apollo3blue
This is an experimantal platform to allow the use of [SparkFun's Arduino framework](https://github.com/sparkfun/Arduino_Apollo3) in PlatformIO.

# How To Use This
As this is experimental, it requires a manual install.

## Install
Locate your .platformio directory which it typically in your home directory:

    $> cd .platformio

Clone [SparkFun's Arduino framework](https://github.com/sparkfun/Arduino_Apollo3):

    ~/.platformio> cd packages
    ~/.platformio>/packages> git clone --recurse-submodules https://github.com/sparkfun/Arduino_Apollo3.git framework-arduinoapollo3

Create a `package.json` file in the directory you just cloned `.platformio/packages/framework-arduinoapollo3/` with the following contents:

```json
{
    "name": "framework-arduinoapollo3",
    "description": "Arduino Wiring-based Framework (Apollo3 Core)",
    "version": "2.0.2",
    "url": "https://github.com/sparkfun/Arduino_Apollo3"
}
```

Checkout [platform-apollo3blue](https://github.com/nigelb/platform-apollo3blue):

    ~> cd ~/.platformio
    ~/.platformio> cd platforms
    ~/.platformio/platforms> git clone https://github.com/nigelb/platform-apollo3blue.git apollo3blue
    ~/.platformio/platforms> cd apollo3blue
    ~/.platformio/platforms/apollo3blue> git checkout --track origin/Core_V2
    
## Verify the Install
You should have a number of Artemis boards show up in your board list:

    $> platformio boards

    .
    .
    .
    
    Platform: apollo3blue
    ================================================================================
    ID                             MCU       Frequency    Flash     RAM    Name
    -----------------------------  --------  -----------  --------  -----  ------------------------------
    SparkFun_Artemis_Module        AMA3B1KK  48MHz        937.50KB  348KB  SparkFun Artemis Module
    SparkFun_Thing_Plus            AMA3B1KK  48MHz        937.50KB  348KB  SparkFun Artemis Thing Plus
    SparkFun_RedBoard_Artemis      AMA3B1KK  48MHz        937.50KB  348KB  SparkFun RedBoard Artemis
    SparkFun_RedBoard_Artemis_ATP  AMA3B1KK  48MHz        937.50KB  348KB  SparkFun RedBoard Artemis ATP
    SparkFun_Artemis_Nano          AMA3B1KK  48MHz        937.50KB  348KB  SparkFun RedBoard Artemis Nano
    
    .
    .
    .    
Or query the platform directly:

    $> platformio platform show apollo3blue
    
    apollo3blue ~ Apollo 3 Blue
    ===========================
    The Apollo MCU Family is an ultra-low power, highly integrated microcontroller platform based on Ambiq Micro’s patented Sub-threshold Power Optimized Technology (SPOT™) and designed for battery-powered and portable, mobile devices.
    
    Version: 0.0.1
    Repository: https://github.com/nigelb/platform-apollo3blue.git
    Vendor: https://www.ambiqmicro.com/mcu/
    License: Apache-2.0
    Frameworks: arduino
    
    Packages
    --------
    
    Package toolchain-gccarmnoneeabi
    --------------------------------
    Type: toolchain
    Requirements: >=1.7
    Installed: Yes
    Version: 1.70201.0
    Original version: 7.2.1
    Description: gcc-arm-embedded
    
    Package framework-arduinoapollo3
    --------------------------------
    Type: framework
    Requirements: ~1.0.20
    Installed: Yes
    Version: 1.0.20
    Original version: None
    Description: Arduino Wiring-based Framework (Apollo3 Core)
    
    Boards
    ------
    ID                             MCU       Frequency    Flash     RAM    Name
    -----------------------------  --------  -----------  --------  -----  ------------------------------
    SparkFun_Artemis_Module        AMA3B1KK  48MHz        937.50KB  348KB  SparkFun Artemis Module
    SparkFun_Artemis_Nano          AMA3B1KK  48MHz        937.50KB  348KB  SparkFun RedBoard Artemis Nano
    SparkFun_Edge                  AMA3B1KK  48MHz        937.50KB  348KB  SparkFun Edge
    SparkFun_Edge2                 AMA3B1KK  48MHz        937.50KB  348KB  SparkFun Edge2
    SparkFun_RedBoard_Artemis      AMA3B1KK  48MHz        937.50KB  348KB  SparkFun RedBoard Artemis
    SparkFun_RedBoard_Artemis_ATP  AMA3B1KK  48MHz        937.50KB  348KB  SparkFun RedBoard Artemis ATP
    SparkFun_Thing_Plus            AMA3B1KK  48MHz        937.50KB  348KB  SparkFun Artemis Thing Plus


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
    

The we can create our test file `src/SparkFun_Artemis_Nano.cpp` with the contents:

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
~/SparkFun_Artemis_Nano> platformio run -v
Processing SparkFun_Artemis_Nano (platform: apollo3blue; board: SparkFun_Artemis_Nano; framework: arduino)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
CONFIGURATION: https://docs.platformio.org/page/boards/apollo3blue/SparkFun_Artemis_Nano.html
PLATFORM: Apollo 3 Blue 0.0.1 > SparkFun RedBoard Artemis Nano
HARDWARE: AMA3B1KK 48MHz, 348KB RAM, 937.50KB Flash
PACKAGES: toolchain-gccarmnoneeabi 1.70201.0 (7.2.1), framework-arduinoapollo3 1.0.20
LDF: Library Dependency Finder -> http://bit.ly/configure-pio-ldf
LDF Modes: Finder ~ chain, Compatibility ~ soft
Found 0 compatible libraries
Scanning dependencies...
No dependencies
Building in release mode
Compiling .pio/build/SparkFun_Artemis_Nano/src/SparkFun_Artemis_Nano.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/ard_supers/avr/dtostrf.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/ard_supers/hooks.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/ard_supers/itoa.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/clock/ap3_clock_sources.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/debugging/ap3_debugging.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/gpio/ap3_gpio.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/gpio/ap3_gpio_structures.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/gpio/ap3_shift.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/initialization/ap3_initialization.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/iomaster/ap3_iomaster.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/main.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/timing/ap3_timing.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/uart/ap3_uart.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/FrameworkArduino/uart/ap3_uart_structures.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_adc.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_ble.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_ble_patch.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_ble_patch_b0.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_burst.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_cachectrl.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_clkgen.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_cmdq.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_ctimer.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_debug.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_flash.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_global.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_gpio.c.o
Archiving .pio/build/SparkFun_Artemis_Nano/libFrameworkArduino.a
Indexing .pio/build/SparkFun_Artemis_Nano/libFrameworkArduino.a
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_interrupt.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_iom.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_ios.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_itm.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_mcuctrl.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_mspi.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_pdm.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_pwrctrl.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_queue.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_reset.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_rtc.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_scard.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_secure_ota.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_security.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_stimer.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_sysctrl.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_systick.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_tpiu.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_uart.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/apollo3_sdk/apollo3/hal/am_hal_wdt.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/variant/bsp/am_bsp.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/variant/bsp/am_bsp_pins.c.o
Compiling .pio/build/SparkFun_Artemis_Nano/variant/config/variant.cpp.o
Compiling .pio/build/SparkFun_Artemis_Nano/variant/startup/startup_gcc.c.o
Archiving .pio/build/SparkFun_Artemis_Nano/libapollo3_sdk.a
Indexing .pio/build/SparkFun_Artemis_Nano/libapollo3_sdk.a
Archiving .pio/build/SparkFun_Artemis_Nano/libvariant.a
Indexing .pio/build/SparkFun_Artemis_Nano/libvariant.a
Linking .pio/build/SparkFun_Artemis_Nano/program
Checking size .pio/build/SparkFun_Artemis_Nano/program
Advanced Memory Usage is available via "PlatformIO Home > Project Inspect"
DATA:    [          ]   1.7% (used 6140 bytes from 356352 bytes)
PROGRAM: [          ]   0.7% (used 6808 bytes from 960000 bytes)
arm-none-eabi-objcopy -O binary .pio/build/SparkFun_Artemis_Nano/program .pio/build/SparkFun_Artemis_Nano/firmware.bin
======================================================================= [SUCCESS] Took 3.46 seconds =======================================================================

```
  
## Uploading
Find the Serial port for your connected device. In thsi example it is on `/dev/ttyUSB0`.
Edit the `platformio.ini` file and add the `upload_port` and `upload_speed` fields. Starting with:

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
upload_port = /dev/ttyUSB0
upload_speed = 115200
```

Then we can upload the firmware:
```bash
~/SparkFun_Artemis_Nano> platformio run -t upload -v
Processing SparkFun_Artemis_Nano (platform: apollo3blue; board: SparkFun_Artemis_Nano; framework: arduino; upload_port: /dev/ttyUSB0; upload_speed: 115200)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CONFIGURATION: https://docs.platformio.org/page/boards/apollo3blue/SparkFun_Artemis_Nano.html
PLATFORM: Apollo 3 Blue 0.0.1 > SparkFun RedBoard Artemis Nano
HARDWARE: AMA3B1KK 48MHz, 348KB RAM, 937.50KB Flash
PACKAGES: toolchain-gccarmnoneeabi 1.70201.0 (7.2.1), framework-arduinoapollo3 1.0.20
LDF: Library Dependency Finder -> http://bit.ly/configure-pio-ldf
LDF Modes: Finder ~ chain, Compatibility ~ soft
Found 0 compatible libraries
Scanning dependencies...
No dependencies
Building in release mode
Advanced Memory Usage is available via "PlatformIO Home > Project Inspect"
DATA:    [===       ]  31.7% (used 113092 bytes from 356352 bytes)
PROGRAM: [=         ]   5.4% (used 51708 bytes from 960000 bytes)
text       data     bss     dec     hex filename
  51572     136  112956  164664   28338 .pio/build/SparkFun_Artemis_Nano/program
AVAILABLE: svl
CURRENT: upload_protocol = svl
/home/user/.platformio/packages/framework-arduinoapollo3/tools/artemis/linux/artemis_svl /dev/ttyUSB0 -b 115200 -f .pio/build/SparkFun_Artemis_Nano/firmware.bin -v


Artemis SVL Bootloader

phase:  setup
        cleared startup blip
        Got SVL Bootloader Version: 3
        Sending 'enter bootloader' command

phase:  bootload
        have 51708 bytes to send in 26 frames
        sending frame #1, length: 2048
        sending frame #2, length: 2048
        sending frame #3, length: 2048
        sending frame #4, length: 2048
        sending frame #5, length: 2048
        sending frame #6, length: 2048
        sending frame #7, length: 2048
        sending frame #8, length: 2048
        sending frame #9, length: 2048
        sending frame #10, length: 2048
        sending frame #11, length: 2048
        sending frame #12, length: 2048
        sending frame #13, length: 2048
        sending frame #14, length: 2048
        sending frame #15, length: 2048
        sending frame #16, length: 2048
        sending frame #17, length: 2048
        sending frame #18, length: 2048
        sending frame #19, length: 2048
        sending frame #20, length: 2048
        sending frame #21, length: 2048
        sending frame #22, length: 2048
        sending frame #23, length: 2048
        sending frame #24, length: 2048
        sending frame #25, length: 2048
        sending frame #26, length: 508

         Upload complete
================================================================================ [SUCCESS] Took 9.46 seconds ================================================================================
```
