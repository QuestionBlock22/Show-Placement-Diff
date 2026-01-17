import os
from sys import platform
import subprocess
import shutil

print ("Doing system check.")

if platform == "win32":
    subprocess.call ("tools\SystemCheck.bat")
else:
    subprocess.call ("tools/SystemCheck.sh")

print ("System check passed.")

Eng_NA = "Race_U"
Eng_EU = "Race_E"
Fra_NA = "Race_Q"
Fra_EU = "Race_F"
Esp_NA = "Race_M"
Esp_EU = "Race_S"
Ger = "Race_G"
Ita = "Race_I"
Jpn = "Race_J"
Kor = "Race_K"
BMG_Loc = "message/Race.bmg"

# Extract and rebuild Race and Font files.
if os.path.isfile("Race_R.szs") is True:
    if os.path.isfile("Race.szs") is True:
        os.remove("Race.szs")
    os.rename("Race_R.szs", "Race.szs")
    print ("Found Korean Race archive. Renamed for convenience.")

subprocess.run(["wszst", "extract", "Race.szs"])
shutil.copyfile("position_12players.brlyt", "Race.d/result/blyt/position_12players.brlyt")
os.remove("Race.szs")
subprocess.run(["wszst", "create", "Race.d"])
shutil.rmtree("Race.d")

# Loop on error.
def handleError():
    main()

# Region-specific operations

region = input("Input the letters P, E, J or K for your region.\n")

def main():
    if region == "E":
        subprocess.run(["wszst", "extract", f"{Eng_NA}.szs", f"{Fra_NA}.szs", f"{Esp_NA}.szs"])
        shutil.copyfile("text/NTSC-U/English/Race.bmg", f"{Eng_NA}.d/{BMG_Loc}")
        shutil.copyfile("text/NTSC-U/French/Race.bmg", f"{Fra_NA}.d/{BMG_Loc}")
        shutil.copyfile("text/NTSC-U/Spanish/Race.bmg", f"{Esp_NA}.d/{BMG_Loc}")
        os.remove(f"{Eng_NA}.szs")
        os.remove(f"{Fra_NA}.szs")
        os.remove(f"{Esp_NA}.szs")
        subprocess.run(["wszst", "create", f"{Eng_NA}.d", f"{Fra_NA}.d", f"{Esp_NA}.d"])
        shutil.rmtree(f"{Eng_NA}.d")
        shutil.rmtree(f"{Fra_NA}.d")
        shutil.rmtree(f"{Esp_NA}.d")
        buildFont()
    elif region == "P":
        subprocess.run(["wszst", "extract", f"{Eng_EU}.szs", f"{Esp_EU}.szs", f"{Fra_EU}.szs", f"{Ita}.szs", f"{Ger}.szs"])
        shutil.copyfile("text/PAL/English/Race.bmg", f"{Eng_EU}.d/{BMG_Loc}")
        shutil.copyfile("text/PAL/French/Race.bmg", f"{Fra_EU}.d/{BMG_Loc}")
        shutil.copyfile("text/PAL/Spanish/Race.bmg", f"{Esp_EU}.d/{BMG_Loc}")
        shutil.copyfile("text/PAL/Italian/Race.bmg", f"{Ger}.d/{BMG_Loc}")
        shutil.copyfile("text/PAL/German/Race.bmg", f"{Ita}.d/{BMG_Loc}")
        os.remove(f"{Eng_EU}.szs")
        os.remove(f"{Esp_EU}.szs")
        os.remove(f"{Fra_EU}.szs")
        os.remove(f"{Ger}.szs")
        os.remove(f"{Ita}.szs")
        subprocess.run(["wszst", "create", f"{Eng_EU}.d", f"{Fra_EU}.d", f"{Esp_EU}.d", f"{Ger}.d", f"{Ita}.d"])
        shutil.rmtree(f"{Eng_EU}.d")
        shutil.rmtree(f"{Fra_EU}.d")
        shutil.rmtree(f"{Esp_EU}.d")
        shutil.rmtree(f"{Ger}.d")
        shutil.rmtree(f"{Ita}.d")
        buildFont()
    elif region == "J":
        subprocess.run(["wszst", "extract", f"{Jpn}.szs"])
        shutil.copyfile("text/NTSC-J/Japanese/Race.bmg", f"{Jpn}.d/{BMG_Loc}")
        os.remove(f"{Jpn}.szs")
        subprocess.run(["wszst", "create", f"{Jpn}.d"])
        shutil.rmtree(f"{Jpn}.d")
        buildFont()
    elif region == "K":
        shutil.copyfile ("Race.szs", "Race_R.szs")
        subprocess.run(["wszst", "extract", f"{Kor}.szs"])
        shutil.copyfile("text/NTSC-K/Korean/Race.bmg", f"{Kor}.d/{BMG_Loc}")
        os.remove(f"{Kor}.szs")
        subprocess.run(["wszst", "create", f"{Kor}.d"])
        shutil.rmtree(f"{Kor}.d")
        buildFont()

    else:
        print ("Invalid character(s) entered. Please try again.")
        handleError()

    print ("\n Operation completed successfully.")

# Operate on the font file.
def buildFont():
    if region == "K":
        subprocess.run(["wszst", "extract", "Font_K.szs"])
        shutil.copyfile ("tt_kart_extension_font.brfnt", "Font_K.d/tt_kart_extension_font.brfnt")
        os.remove("Font_K.szs")
        subprocess.run(["wszst", "create", "Font_K.d"])
        shutil.rmtree("Font_K.d")
    else:
        subprocess.run(["wszst", "extract", "Font.szs"])
        shutil.copyfile("tt_kart_extension_font.brfnt", "Font.d/tt_kart_extension_font.brfnt")
        os.remove("Font.szs")
        subprocess.run(["wszst", "create", "Font.d"])
        shutil.rmtree("Font.d")
    return

main()