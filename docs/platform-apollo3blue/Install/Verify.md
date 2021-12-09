## Verify the Install
You should have a number of Artemis boards show up in your board list:

    $> platformio boards

    .
    .
    .
    
	Platform: apollo3blue
	==================================================================================================================
	ID                                   MCU       Frequency    Flash    RAM    Name
	-----------------------------------  --------  -----------  -------  -----  -------------------------------------
	SparkFun_Artemis_Development_Kit     AMA3B1KK  48MHz        960KB    384KB  SparkFun Artemis Development Kit
	SparkFun_Artemis_Module              AMA3B1KK  48MHz        960KB    384KB  SparkFun Artemis Module
	SparkFun_Thing_Plus                  AMA3B1KK  48MHz        960KB    384KB  SparkFun Artemis Thing Plus
	SparkFun_Edge                        AMA3B1KK  48MHz        960KB    384KB  SparkFun Edge
	SparkFun_Edge2                       AMA3B1KK  48MHz        960KB    384KB  SparkFun Edge2
	SparkFun_Thing_Plus_expLoRaBLE       AMA3B1KK  48MHz        960KB    384KB  SparkFun LoRa Thing Plus - expLoRaBLE
	SparkFun_MicroMod_Artemis_Processor  AMA3B1KK  48MHz        960KB    384KB  SparkFun MicroMod Artemis Processor
	SparkFun_RedBoard_Artemis            AMA3B1KK  48MHz        960KB    384KB  SparkFun RedBoard Artemis
	SparkFun_RedBoard_Artemis_ATP        AMA3B1KK  48MHz        960KB    384KB  SparkFun RedBoard Artemis ATP
	SparkFun_Artemis_Nano                AMA3B1KK  48MHz        960KB    384KB  SparkFun RedBoard Artemis Nano
    
    .
    .
    .    
Or query the platform directly:

    $> platformio platform show apollo3blue

    apollo3blue ~ Apollo 3 Blue
    ===========================
    The Apollo MCU Family is an ultra-low power, highly integrated microcontroller platform based on Ambiq Micro’s patented Sub-threshold Power Optimized Technology (SPOT™) and designed for battery-powered and portable, mobile devices.
    
    Version: 0.0.2
    Repository: https://github.com/nigelb/platform-apollo3blue.git
    License: Apache-2.0
    Frameworks: ambiqsdk-sfe, arduino
    
    Packages
    --------
    
    Package toolchain-gccarmnoneeabi
    --------------------------------
    Type: toolchain
    Requirements: >=1.9
    Installed: Yes
    Version: 1.90301.200702
    Original version: 9.3.1
    Description: GNU toolchain for Arm Cortex-M and Cortex-R processors
    
    Package framework-arduinoapollo3
    --------------------------------
    Type: framework
    Requirements: 2.1.1
    Installed: Yes
    Version: 2.1.1
    Original version: None
    Description: An mbed-os enabled Arduino core for Ambiq Apollo3 based boards
    
    Package framework-ambiqsuitesdkapollo3-sfe
    ------------------------------------------
    Type: framework
    Requirements: 2.4.2
    Installed: Yes
    Version: 2.4.2
    Original version: None
    Description: SparkFun's AmbiqSuiteSDK repository.
    
    Package tool-jlink
    ------------------
    Type: uploader
    Requirements: ^1.63208.0
    Installed: Yes
    Version: 1.72000.0
    Original version: 7.20.0
    Description: Software and Documentation Pack for SEGGER J-Link debug probes
    
    Boards
    ------
    ID                                   MCU       Frequency    Flash    RAM    Name
    -----------------------------------  --------  -----------  -------  -----  -------------------------------------
    SparkFun_Artemis_Development_Kit     AMA3B1KK  48MHz        960KB    384KB  SparkFun Artemis Development Kit
    SparkFun_Artemis_Module              AMA3B1KK  48MHz        960KB    384KB  SparkFun Artemis Module
    SparkFun_Edge                        AMA3B1KK  48MHz        960KB    384KB  SparkFun Edge
    SparkFun_Edge2                       AMA3B1KK  48MHz        960KB    384KB  SparkFun Edge2
    SparkFun_MicroMod_Artemis_Processor  AMA3B1KK  48MHz        960KB    384KB  SparkFun MicroMod Artemis Processor
    SparkFun_RedBoard_Artemis            AMA3B1KK  48MHz        960KB    384KB  SparkFun RedBoard Artemis
    SparkFun_RedBoard_Artemis_ATP        AMA3B1KK  48MHz        960KB    384KB  SparkFun RedBoard Artemis ATP
    SparkFun_Redboard_Artemis_Nano       AMA3B1KK  48MHz        960KB    384KB  SparkFun RedBoard Artemis Nano
    SparkFun_Thing_Plus                  AMA3B1KK  48MHz        960KB    384KB  SparkFun Artemis Thing Plus
    SparkFun_Thing_Plus_expLoRaBLE       AMA3B1KK  48MHz        960KB    384KB  SparkFun LoRa Thing Plus - expLoRaBLE

