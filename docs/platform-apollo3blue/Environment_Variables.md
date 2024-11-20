# `platformApollo3` Environment Variables
The following environment variables can be used to change the behaviour of the platform.

# `PLATFORMIO_UPLOAD_PROTOCOL`
Setting the environment variable `PLATFORMIO_UPLOAD_PROTOCOL` overrides the `upload_protocol`
used to program a firmware to a device.

Example:

```text
$> PLATFORMIO_UPLOAD_PROTOCOL=jlink pio run -t upload
Processing test_imu (platform: apollo3blue; board: SparkFun_MicroMod_Artemis_Processor; framework: arduino)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option

WARNING! UPLOAD_PROTOCOL has been overridden by the environment variable PLATFORMIO_UPLOAD_PROTOCOL and set to: jlink

CONFIGURATION: https://docs.platformio.org/page/boards/apollo3blue/SparkFun_MicroMod_Artemis_Processor.html
PLATFORM: Apollo 3 Blue (0.0.2+sha.154b27c) > SparkFun MicroMod Artemis Processor
HARDWARE: AMA3B1KK 48MHz, 384KB RAM, 960KB Flash
DEBUG: Current (jlink) External (jlink)
PACKAGES: 
 - framework-arduinoapollo3 @ 2.2.1+sha.XXXXXXX 
 - toolchain-gccarmnoneeabi @ 1.90201.191206 (9.2.1)
 .
 .
 .
```
