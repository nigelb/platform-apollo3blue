## Uploading
The device port is now automatically detected. However, one can also specify it manually by editing the `platformio.ini` file and adding the `upload_port` and `upload_speed` fields. For example starting with Starting with:

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
