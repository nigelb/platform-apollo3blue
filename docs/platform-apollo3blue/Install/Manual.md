# Manual Installation of `sparkfun/Arduino_Apollo3``` 

## Install framework-arduinoapollo3@2.1.0

Locate your .platformio directory which it typically in your home directory:

    $> cd ~/.platformio
    ~/.platformio> cd packages
    ~/.platformio/packages> git clone --recurse-submodules --branch v2.1.0 https://github.com/sparkfun/Arduino_Apollo3.git framework-arduinoapollo3@2.1.0

Create the file `~/.platformio/packages/framework-arduinoapollo3@2.1.0/package.json` with the following contents:
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
    ~/.platformio/packages> git clone --recurse-submodules --branch v1.2.3 https://github.com/sparkfun/Arduino_Apollo3.git framework-arduinoapollo3@1.2.3

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
    
  
