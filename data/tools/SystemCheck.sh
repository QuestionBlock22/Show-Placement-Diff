#!/bin/bash

# Set variables
ERR_WIIMM="Wiimm's SZS Tools could not be found. Please install Wiimm's SZS Tools from (https://szs.wiimm.de/download.html)."

clear

# Check Wiimm's SZS Tools install.
if ls "/wszst/wszst"; then
    :
    clear
elif ls "/usr/local/bin/wszst"; then
    :
    clear
else
    echo "$ERR_WIIMM"
    exit
fi