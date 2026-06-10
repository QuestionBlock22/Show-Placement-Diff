## Building

Only the modified files are included in this repository. To include the dependencies for this code in your own files while preserving any additional modifiications you made, the following files must be copied to the root of the **"data"** folder.


### All Regions
```
Race.szs
Font.szs*
```

### North America (RMCE01)

```
Race_U.szs
Race_Q.szs
Race_M.szs
```

### Europe/Australia (RMCP01)
```
Race_E.szs
Race_F.szs
Race_S.szs
Race_G.szs
Race_I.szs
```

### Japan (RMCJ01)
```
Race_J.szs
```

### South Korea (RMCK01)
```
Race_K.szs
Font_K.szs
```
***1. Except NTSC-K***

***2. Note:*** *The build script will automatically copy and rename "Race.szs" into "Race_R.szs" for the South Korean region.*

### Dependencies
* [Wiimm's SZS Tools](https://szs.wiimm.de/download.html)
-- (Unpacking and packing of yaz0 archives.)
* [Python 3](https://www.python.org/downloads/)
-- (Required to run the script on non-Unix environments)
* **Optional:** [wuj5](https://www.github.com/stblr/wuj5) 
-- (For compiling "position_12players.json5" into a brlyt file.)

### Mark Files as Executable

Depending on your operating system, you may need to mark relevant files as executable. On most Linux distros, it's as simple as right clicking the file, going to "Properties," and then, in the permissions section, checking the box that says "Make executable."

However, on some distros and macOS, this GUI option does not exist.

In order to run the script, the following needs to be made executable first:
```
Main script:

  build_race.py
```

Run the following command to make this file executable:

```
chmod 755 "build_race.py"
```

### Running

Open a terminal and run the following command:
```
python build_race.py

## or ##

./build_race.py

```
