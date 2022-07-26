# Apollo3 Targets
Here we document the custom targets.

```shell
$> pio run --list-targets
Environment                    Group     Name            Title                 Description
-----------------------------  --------  --------------  --------------------  ------------------------------------------------------------
SparkFun_RedBoard_Artemis_ATP  Advanced  compiledb       Compilation Database  Generate compilation database `compile_commands.json`
SparkFun_RedBoard_Artemis_ATP  General   clean           Clean
SparkFun_RedBoard_Artemis_ATP  General   cleanall        Clean All             Clean a build environment and installed library dependencies
SparkFun_RedBoard_Artemis_ATP  Platform  jlink_rtt       JLink RTT             Start the SEGGER Jlink RTT program.
SparkFun_RedBoard_Artemis_ATP  Platform  jlink_swo       JLink SWO             Start the SEGGER Jlink SWO program.
SparkFun_RedBoard_Artemis_ATP  Platform  svl_bootloader  Sparkfun SVL          Upload the Sparkfun SVL Bootloader.
SparkFun_RedBoard_Artemis_ATP  Platform  upload          Upload
```

## svl_bootloader
This target uploads the Sparkfun SVL bootloader onto your board.

```shell
$> pio run -v -t svl_bootloader 
Processing SparkFun_RedBoard_Artemis_ATP (platform: apollo3blue; board: SparkFun_RedBoard_Artemis_ATP; framework: arduino; upload_port: /dev/ttyUSB0)
-------------------------------------------------------------------------------------------------------------------------------------------------------
CONFIGURATION: https://docs.platformio.org/page/boards/apollo3blue/SparkFun_RedBoard_Artemis_ATP.html
PLATFORM: Apollo 3 Blue (0.0.2+sha.f85fff8) (git+https://github.com/user/platform-apollo3blue) > SparkFun RedBoard Artemis ATP
HARDWARE: AMA3B1KK 48MHz, 384KB RAM, 960KB Flash
DEBUG: Current (jlink) External (jlink)
PACKAGES: 
 - framework-arduinoapollo3 2.2.0+sha.771ce8f (git+https://github.com/sparkfun/Arduino_Apollo3#v2.2.0) 
 - toolchain-gccarmnoneeabi 1.90201.191206 (9.2.1)
LDF: Library Dependency Finder -> https://bit.ly/configure-pio-ldf
LDF Modes: Finder ~ chain, Compatibility ~ soft
Found 9 compatible libraries
Scanning dependencies...
No dependencies
Building in release mode
BeforeUpload(["svl_bootloader"], ["/home/user/.platformio/packages/framework-arduinoapollo3/tools/uploaders/svl/bootloader/gcc/artemis_module/bin/svl.bin"])
/home/user/.platformio/packages/framework-arduinoapollo3/tools/uploaders/asb/dist/linux/asb --bin /home/user/.platformio/packages/framework-arduinoapollo3/tools/uploaders/svl/bootloader/gcc/artemis_module/bin/svl.bin --load-address-blob 0x20000 --magic-num 0xCB -o /home/user/.platformio/packages/framework-arduinoapollo3/tools/uploaders/svl/bootloader/gcc/artemis_module/bin/svl.bin.ASB --version 0x0 --load-address-wired 0xC000 -i 6 --options 0x1 -b 115200 -port /dev/ttyUSB0 -r 2 -v
Header Size =  0x80
original app_size  0x328c ( 12940 )
load_address  0xc000 ( 49152 )
app_size  0x328c ( 12940 )
w0 = 0xcb00330c
Security Value  0x10
w2 =  0x10008080
addrWord =  0xc000
versionKeyWord =  0x0
child0/feature =  0xffffffff
child1 =  0xffffffff
crc =   0xc703da31
Writing to file  /home/user/.platformio/packages/framework-arduinoapollo3/tools/uploaders/svl/bootloader/gcc/artemis_module/bin/svl.bin.ASB_OTA_blob.bin
testing: /home/user/.platformio/packages/framework-arduinoapollo3/tools/uploaders/svl/bootloader/gcc/artemis_module/bin/svl.bin.ASB_OTA_blob.bin
Header Size =  0x60
app_size  0x330c ( 13068 )
Writing to file  /home/user/.platformio/packages/framework-arduinoapollo3/tools/uploaders/svl/bootloader/gcc/artemis_module/bin/svl.bin.ASB_Wired_OTA_blob.bin
Image from  0x0  to  0x330c  will be loaded at 0x20000
Connecting over serial port /dev/ttyUSB0...
Sending Hello.
Received response for Hello
Bootloader connected
Received Status
length = 0x58
version = 0x5
Max Storage = 0x4ffa0
Status = 0x2
State = 0x7
AMInfo = 
0x1
0xff2da3ff
0x55fff
0x1
0x4cd00005
0xffffffff
0xffffffff
0xffffffff
0xffffffff
0xffffffff
0xffffffff
0xffffffff
0xffffffff
0xffffffff
0xffffffff
0xffffffff
Sending OTA Descriptor = 0xfe000
Sending Update Command.
number of updates needed = 1
Sending block of size 0x336c from 0x0 to 0x336c
Sending Data Packet of length 8180
Sending Data Packet of length 4984
Sending Reset Command.
Tries = 0
Upload complete!
============================================================= [SUCCESS] Took 2.31 seconds =============================================================
```

## jlink_swo
This target launches the `JLinkSWOViewerCLExe` command from the jlink toolkit.


## jlink_rtt
This target launches the `JLinkRTTViewerExe` command from the jlink toolkit.



