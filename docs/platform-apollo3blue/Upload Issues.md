Upload Issues
=============

I thought I would document all the ways in which I have remedied uploading issues with the SVL uploader.

Relevant issues and pull requests:

* [sparkfun/Apollo3_Uploader_SVL#4](https://github.com/sparkfun/Apollo3_Uploader_SVL/issues/4)
* [sparkfun/Apollo3_Uploader_SVL#6](https://github.com/sparkfun/Apollo3_Uploader_SVL/pull/6)
* [sparkfun/Arduino_Apollo3#94](https://github.com/sparkfun/Arduino_Apollo3/issues/94)
* [nigelb/platform-apollo3blue#17](https://github.com/nigelb/platform-apollo3blue/issues/17)


Upload Speed
============
As pointer out by @cadeo111 [here](https://github.com/nigelb/platform-apollo3blue/issues/17#issuecomment-1062971881) sometimes changing the upload speed can fix the issue.

Add `upload_speed=115200` to your platform.ini file.


Linux Driver
============
As pointed out by @oclyke [here](https://github.com/sparkfun/Arduino_Apollo3/issues/94#issuecomment-560456716) some linux distros have old drivers for the CH340C USB to Serial chip used on these Artemis boards. 
An up-to-date driver can be found here:
* https://github.com/juliagoda/CH341SER


Modified Port Settings
======================
I often use the linux command `screen` to communicate with the boards after uploading.
On my Linux system the `screen` program would modify the system setting for the port such that on subsequent connections`the DTR pin would not be asserted to reset the MCU.
Initially the only way I had to fix this was to unplug and replug the board.
Once I figured out what the issue was I could fix the system setting for the port with the following command:

```
$> stty -F /dev/ttyUSB0 hupcl
```

I also made a [pull request](https://github.com/sparkfun/Apollo3_Uploader_SVL/pull/6) for the uploader, so that it would be able to fix the port settings as well


Corrupted/Overwritten SVL Bootloader
========================
I have on occasion managed to corrupt/overwrite the SVL bootloader. 
It can be re-flashed with [Arduino](https://learn.sparkfun.com/tutorials/designing-with-the-sparkfun-artemis/troubleshooting).

