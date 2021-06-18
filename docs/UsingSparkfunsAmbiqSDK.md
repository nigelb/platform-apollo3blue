# Using Sparkfun's AmbiqSuiteSDK

## Install framework-ambiqsuitesdkapollo3-sfe@2.4.2

Locate your .platformio directory which it typically in your home directory:

    $> cd ~/.platformio
    ~/.platformio> cd packages
    ~/.platformio> wget https://github.com/sparkfun/AmbiqSuiteSDK/archive/refs/tags/v2.5.1.zip
    ~/.platformio> unzip v2.5.1.zip
    ~/.platformio> mv AmbiqSuiteSDK-2.5.1 framework-ambiqsuitesdkapollo3@2.5.1

Create the file `~/.platformio/packages/framework-ambiqsuitesdkapollo3@2.5.1/package.json` with the following contents:

```json
{
    "name": "framework-ambiqsuitesdkapollo3-sfe",
    "description": "SparkFun's AmbiqSuiteSDK repository.",
    "version": "2.5.1",
    "url": "https://github.com/sparkfun/AmbiqSuiteSDK"
}
```

## Create A Project
```bash
$> mkdir AmbiqSuiteSDK_Test
$> cd AmbiqSuiteSDK_Test
$> platformio init --board SparkFun_RedBoard_Artemis_ATP

The current working directory /home/user/projects/AmbiqSuiteSDK_Test will be used for the project.

The next files/directories have been created in /home/user/projects/AmbiqSuiteSDK_Test
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

Add `platform_packages = framework-ambiqsuitesdkapollo3@2.5.1` to `platformio.ini`



