# platform-apollo3blue
This is an experimental platform to allow the use of [SparkFun's Arduino framework](https://github.com/sparkfun/Arduino_Apollo3) in PlatformIO.

# How To Use This
As this is experimental, it requires a manual install.

# Supported Frameworks and Tools

Platform-apollo3blue now supports the following: 

1. Frameworks:
    * Arduino - [sparkfun/Arduino_Apollo3](https://github.com/sparkfun/Arduino_Apollo3)
        * [Core V1](https://github.com/sparkfun/Arduino_Apollo3/tree/v1)
        * [Core V2](https://github.com/sparkfun/Arduino_Apollo3)
    * Ambiq Suit SDK - [sparkfun/AmbiqSuiteSDK](https://github.com/sparkfun/AmbiqSuiteSDK.git)
2. Tools:
    * Segger [JLink](https://www.segger.com/products/debug-probes/j-link/) with [platformio](https://docs.platformio.org/en/latest/plus/debug-tools/jlink.html)
        * [Upload protocol](docs/platform-apollo3blue/UsingSeggerJLink.md#upload-firmware) 
        * [Debugger](docs/platform-apollo3blue/UsingSeggerJLink.md#debug-firmware)

To specify which framework and version to use, see [below](#specifying-the-version-of-sparkfunarduino_apollo3) or a more detailed [example](docs/platform-apollo3blue/UsingMultipleVersionsOfArduino_Apollo3.md).
    
# Quick Start
Here we document the quickest way to get started using `platform-apollo3blue`. 
Until all the necessary updates required to use platformio and platform-apollo3blue with [sparkfun/Arduino_Apollo3](https://github.com/sparkfun/Arduino_Apollo3) have made it into the [sparkfun/Arduino_Apollo3](https://github.com/sparkfun/Arduino_Apollo3) repository 
I am maintaining a fork of it [here](https://github.com/sparkfun/Arduino_Apollo3) with the required updates.

## 1. Install `platform-apollo3blue`
````
$ pio platform install git+https://github.com/nigelb/platform-apollo3blue
````

## 2. Select and Install a version of Arduino_Apollo3
The quickest and easiest way to install Arduino_Apollo3 is to create a project and specify the version as a git repo.

```
$ mkdir new_project
$ cd new_project
```

And then
### Core V2
```
$ pio init -b SparkFun_RedBoard_Artemis_ATP --ide vscode -O"platform_packages=framework-arduinoapollo3@https://github.com/nigelb/Arduino_Apollo3#v2.1.1_pio"
```

### Core V1
```
$ pio init -b SparkFun_RedBoard_Artemis_ATP --ide vscode -O"platform_packages=framework-arduinoapollo3@https://github.com/nigelb/Arduino_Apollo3#v1.2.1_pio"
```

# Manual install of sparkfun/Arduino_Apollo3
If you don't want to use my forked repo, or you want to be able to have concurrent projects that use core v1 and core v2
without having platformio reinstall Arduino_Apollo each time, you can manually install both version
of the cores.

See the [Manual Installation](docs/install/Manual.md) and [Using Multiple Versions of Arduino_Apollo3](docs/UsingMultipleVersionsOfArduino_Apollo3).

# More Information

1. [Verify Installation](docs/install/Verify.md) 
2. [Upload](docs/Install.Upload.md)
3. [`platformio.ini` customization options](docs/PlatformIO_ini_Options.md)
4. [Using a Segger JLink](docs/UsingSeggerJLink.md)