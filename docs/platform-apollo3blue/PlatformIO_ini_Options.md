# platform.ini Options
Here we document the options you can change in your `platform.ini` file.

## All platforms
### GCC --Specs=

Lets you change the --specs parameter that is passed to the compiler.
Examples:

    board_build.specs = nano.specs

Or:

    board_build.specs = nosys.specs

### Linker Script

#### Custom Linker Script

Lets you specify the location (relative to the project directory) of your custom linker script.
For example, if you had your custom linker script in `<PROJECT_DIR>/linker/my_linker_script.ld`:

    board_build.linker_script = linker/my_linker_script.ld

### Upload Address
#### Background

The address that the program is loaded to in the MCU's flash must match what is specified in the linker file.

When the linker script [`tools/uploaders/svl/0x10000.ld`](https://github.com/sparkfun/Apollo3_Uploader_SVL/blob/54a37d5009fd8bb4e5c9770cabd4bed984ac7c98/0x10000.ld) is used:
```
MEMORY
{
  FLASH (rx) : ORIGIN = 0x00010000, LENGTH = 0x000F0000
  RAM_NVIC (rwx) : ORIGIN = 0x10000000, LENGTH = 0x100
  RAM (rwx) : ORIGIN = (0x10000000 + 0x100), LENGTH = (384K - (0x100))
}
.
.
.
```
The upload address is automatically set to `0x10000` to match the address from the line `FLASH (rx) : ORIGIN = 0x00010000`.

When the linker script [`tools/uploaders/asb/0xC000.ld`](https://github.com/sparkfun/Apollo3_Uploader_ASB/blob/454fc619ce9371016f7bbdbb875aed2e197ea1ce/0xC000.ld) is used:
```
MEMORY
{
  FLASH (rx) : ORIGIN = 0x0000C000, LENGTH = 0x000F4000
  RAM_NVIC (rwx) : ORIGIN = 0x10000000, LENGTH = 0x100
  RAM (rwx) : ORIGIN = (0x10000000 + 0x100), LENGTH = (384K - (0x100))
}
.
.
.
```
The upload address is automatically set to `0xC000` to match the address from the line `FLASH (rx) : ORIGIN = 0x0000C000`.

#### Custom Upload Address

Used with the `asb` and `jlink` upload protocols, this lets you specify the location in the FLASH that the program
is loaded into. Typically, this is used if you are using a modified linker script.

To specify a custom upload address of `0x20000` in your `platform.ini` file:

    board_build.upload.address = 0x20000

### Variants
#### Custom Variants Directory
Lets you specify a project specific variants directory. The default value id `$PROJECT_DIR/variants`:

    board_build.variants_dir = myvariant

### JLink
#### Extra Commander Script Commands
The normal JLink commander upload script looks like this: 
```
h
loadbin .pio/build/dev/firmware.bin, 0x10000
r
q
```
If we want to insert extra commands we can add them on either side of the `loadbin`
command with the following options.

##### Pre Upload Commands
You can add extra commands before the `loadbin` with the following:

    board_build.jlink.extra_commands.pre_program = savebin .pio/build/dev/firmware.bin.bak 0x10000 0x50000

which would yield a commander script:
```
h
savebin .pio/build/dev/firmware.bin.bak 0x10000 0x50000
loadbin .pio/build/dev/firmware.bin, 0x10000
r
q
```
Which would download the firmware that is already on the device to the file `.pio/build/dev/firmware.bin.bak`.
Commands available for the J-Link Commander can be found [here](https://wiki.segger.com/J-Link_Commander).

##### Post Upload Commands
You can add extra commands after the `loadbin` with the following:

    board_build.jlink.extra_commands.post_program = erase 0x2E000 0x2E400

which would yield a commander script:
```
h
loadbin .pio/build/dev/firmware.bin, 0x10000
erase 0x2E000 0x2E400
r
q
```
Which would erase the flash range 0x2E000 to 0x2E400.
Commands available for the J-Link Commander can be found [here](https://wiki.segger.com/J-Link_Commander).

## Platform: `ambiqsdk-sfe`
These options are only available in the `ambiqsdk-sfe` platform.

### Compiler Standard

Lets you change the `-std` parameter that is passed to the compiler.
For example the default is:

    board_build.standard = c99

Or you can change this:

    board_build.standard = gnu99

## Other Targets

### Target: `jlink_swo`

#### SWO Clock Speed

Lets you change the `-swofreq` passed to JLinkSWOViewer.
The default SWO clock speed is 12000000, to change it: 

    board_debug.swo_freq=1000000
