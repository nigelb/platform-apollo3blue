# platform.ini Options
Here we document the options you can change in your `platform.ini` file.

## GCC --Specs=

Lets you change the --specs parameter that is passed to the compiler.
Examples:

    board_build.specs = nano.specs

Or:

    board_build.specs = nosys.specs

## Linker Script

### Custom Linker Script

Lets you specify the location (relative to the project directory) of your custom linker script.
For example, if you had your custom linker script in `<PROJECT_DIR>/linker/my_linker_script.ld`:

    board_build.linker_script = linker/my_linker_script.ld

## Upload Address
### Background

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

### Custom Upload Address

Used with the `asb` and `jlink` upload protocols, this lets you specify the location in the FLASH that the program
is loaded into. Typically, this is used if you are using a modified linker script.

To specify a custom upload address of `0x20000` in your `platform.ini` file:

    board_build.upload.address = 0x20000

