@echo off
cls

:: Check Wiimm's SZS Tools and Wiimm's ISO Tools install
IF EXIST "C:\Program Files (x86)\Wiimm\SZS" (
    cls
) ELSE IF EXIST ".\wszst\wszst.exe" (
    cls
)
    echo "Wiimm's SZS Tools could not be found. Please install Wiimm's SZS Tools from (https://szs.wiimm.de/download.html)."
    EXIT /B
)

:end