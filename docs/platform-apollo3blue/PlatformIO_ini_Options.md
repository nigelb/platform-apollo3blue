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

### Core V2

The Arduino_Apollo3 v2 distribution comes with two linker scripts, one to load the firmware at `0xC000` and the other 
to load the firmware at `0x10000`. With `board_build.linker_script` left unspecified the default is `0x10000`. 
To change this one can specify:

    board_build.framework.arduino.v2.linker_script = 0xC000.ld

Or the default:

    board_build.framework.arduino.v2.linker_script = 0x10000.ld

### Core V1
The Arduino_Apollo3 v1 distribution also comes with two linker scripts, one to load the firmware at `0xC000` and the other 
to load the firmware at `0x10000`. With `board_build.linker_script` left unspecified the default is `artemis_sbl_svl_app.ld`. 
To change this one can specify:

    board_build.framework.arduino.v1.linker_script = 0xC000.ld

Or the default:

    board_build.framework.arduino.v1.linker_script = artemis_sbl_svl_app.ld

## Upload Address
