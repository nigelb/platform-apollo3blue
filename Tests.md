# EEPROM
## Example2_AllFunctions
### Arduino IDE
```
T%⸮5⸮Examples
Time to erase all EEPROM: 15ms

8 bit tests
Write byte time: 21ms
Write identical byte to same location (should be ~1): 1ms
Location 929 should be 200: 200

Location 930 should be 23: 23


16 bit tests
Location 369 should be 3411: 3411

Location 371 should be -366: -366


32 bit tests
Size of int: 4
Location 612 should be -245000: -245000

Location 616 should be 400123: 400123

Location 986 should be -341002: -341002

Location 990 should be 241544: 241544

Size of float: 4
Location 405 should be -7.350000: -7.350000

Location 409 should be 5.220000: 5.220000


64 bit tests
Size of double: 8
Time to record 64-bits: 24ms
Location 203 should be -290.348572: -290.348572
Location 211 should be 384.957336: 384.957336
Edge of EEPROM 1016 should be 917.141602: 917.141602
Rewrite of 1016 should be 254.887695: 254.887695

String test
Location 394 string should read 'How are you today?': How are you today?

Flash Contents:
0xFFFFFFFF 0xFFFFFFFF 0xFFFFFFFF 0xFFFFFFFF 0xFFFFFFFF 0xFFFFFFFF 0xFFFFFFFF 0xFFFFFFFF 
```
### PlatformIO
```
|QQ%⸮5⸮Examples
Time to erase all EEPROM: 15ms

8 bit tests
Write byte time: 21ms
Write identical byte to same location (should be ~1): 1ms
Location 368 should be 200: 200

Location 369 should be 23: 23


16 bit tests
Location 843 should be 3411: 3411

Location 845 should be -366: -366


32 bit tests
Size of int: 4
Location 800 should be -245000: -245000

Location 804 should be 400123: 400123

Location 701 should be -341002: -341002

Location 705 should be 241544: 241544

Size of float: 4
```
Then the program hangs.
# PDM
## Example3_FullConfigure
### Arduino IDE
```
⸮*⸮ɭչ⸮PDM Example
PDM Initialized
Settings:
PDM Clock (Hz):              6000000
Decimation Rate:                  64
Effective Sample Freq.:        46875
FFT Length:                     4096

FFT Resolution: 11.444 Hz
Loudest frequency: 400         
Loudest frequency: 1201         
Loudest frequency: 1144         
Loudest frequency: 1167         
Loudest frequency: 1476         
Loudest frequency: 1556         
Loudest frequency: 1602         
Loudest frequency: 1613         
Loudest frequency: 1602         
Loudest frequency: 1602         
Loudest frequency: 1625         
Loudest frequency: 1613         
Loudest frequency: 1602         
Loudest frequency: 1579         
Loudest frequency: 1544         
Loudest frequency: 1110         
Loudest frequency: 1052         
Loudest frequency: 949         
Loudest frequency: 938         
Loudest frequency: 1327         
Loudest frequency: 1361         
Loudest frequency: 1384         
Loudest frequency: 1567         
Loudest frequency: 1556         
Loudest frequency: 1544         
Loudest frequency: 1533         
Loudest frequency: 1533         
Loudest frequency: 1522         
Loudest frequency: 1453         
Loudest frequency: 1407         
Loudest frequency: 1373         
Loudest frequency: 1327         
Loudest frequency: 1258         
Loudest frequency: 1270         
Loudest frequency: 1270         
Loudest frequency: 11524         
Loudest frequency: 881         
Loudest frequency: 1384         
Loudest frequency: 1762         
Loudest frequency: 18264         
Loudest frequency: 560         
Loudest frequency: 537         
Loudest frequency: 400 
```
### PlatformIO
```
|*⸮ɭչ⸮PDM Example
PDM Initialized
Settings:
PDM Clock (Hz):              6000000
Decimation Rate:                  64
Effective Sample Freq.
```
At this point the code hangs.

# RTC
## Example2_RTCwithSleep
### Arduino IDE
```
*⸮ɭչ⸮RTC Example
It is now 19:46:10.00 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.00 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.00 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.01 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.01 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.02 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.02 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.03 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.03 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.04 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.04 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.05 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.05 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.06 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.06 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.07 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.07 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.08 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.08 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.09 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.09 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.10 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.10 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.11 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.11 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.11 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.12 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.13 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.13 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.14 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.14 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.15 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.15 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.16 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.16 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.17 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.17 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.18 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.18 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.19 12/09/19 Day of week: 1 = Monday
It is now 19:46:10.19 12/09/19 Day of week: 1 = Monday
```

### PlatformIO
```
|*⸮ɭչ⸮RTC Example
It is now 22:47:11.00 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.00 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.01 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.01 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.01 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.02 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.02 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.03 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.03 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.04 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.04 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.05 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.05 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.06 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.06 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.07 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.07 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.08 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.08 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.09 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.09 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.10 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.10 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.11 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.11 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.12 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.12 12/13/19 Day of week: 5 = Friday
It is now 22:47:11.13 12/13/19 Day of week: 5 = Friday
```
Seems to Work fine