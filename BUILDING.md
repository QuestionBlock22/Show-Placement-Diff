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

### Running

Open a terminal and run the following command:
```
py3 build_race.py

## or ##

python build_race.py

```