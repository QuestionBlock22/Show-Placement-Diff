# Show Everyone's Placement Difference From the Previous Race (QB22)

# Inject @
# PAL:    807f530c
# NTSC-U: 807eace4
# NTSC-J: 807f4978
# NTSC-K: 807e36cc

.set region, '' # Fill with P, E, J, or K in the quotes to assemble for a particular region.
.if (region == 'P' || region == 'p')
    .set setTextboxMessage, 0x8063dcbc
    .set raceDataBase, 0x809c28d8 # Resolves to 809c7d28 (Racedata::spInstance)
    .set sectionMgrBase, 0x809c1e38 # Only the lower-half is used. The full address is here for reference purposes. (SectionMgr::spInstance)
.elseif (region == 'E' || region == 'e')
    .set setTextboxMessage, 0x8060c89c
    .set raceDataBase, 0x809c7098
    .set sectionMgrBase, 0x809bd508
.elseif (region == 'J' || region == 'j')
    .set setTextboxMessage, 0x8063d328
    .set raceDataBase, 0x809c3878
    .set sectionMgrBase, 0x809c0e98
.elseif (region == 'K' || region == 'k')
    .set setTextboxMessage, 0x8062bfd4
    .set raceDataBase, 0x809b4298
    .set sectionMgrBase, 0x809b0478
.else
    .err
.endif

# Original instruction:
mr r30, r3

# Only compare if it is the first race.
lis r11, raceDataBase@h
lwz r12, -raceDataBase@l (r11)

# Check current game mode and if it's the first race. Battle mode is not supported at the moment.
mr r8, r11                                                  # Backup the upper half of Racedata.
lwz r0, 0xB70 (r12)                                         # racedata -> racesScenario -> settings -> gameMode
cmpwi r0, 0                                                 # Check if the current game mode is Grand Prix.
beq gameModeGP
lwz r12, sectionMgrBase@l (r11)
lwz r11, 0x98 (r12)
lwz r0, 0x60 (r11)                                          # sectionMgr -> sectionParams -> vsRaceNumber
cmpwi r0, 1
beq end
b processPositions

gameModeGP:
lbz r0, 0xB8C (r12)                                         # racedata -> racesScenario -> settings -> raceNumber
cmpwi r0, 0
beq end

processPositions:
# Get the current player ID and their previous position.
lwz r11, -raceDataBase@l (r8)
mulli r0, r31, 240
addi r6, r11, 40
add r8, r6, r0
lbz r12, 0xE1 (r8)                                          # racedata -> racesScenario -> players -> previousPosition

# Compare the player's placement from the previous race with the current race.
cmpw r24, r12
blt raceDiffImprove
bgt raceDiffRegress
li r5, 0x5e2
b getPaneName
raceDiffImprove:
li r5, 0x5e3
b getPaneName
raceDiffRegress:
li r5, 0x5e4

# Save the address to the pane name string.
getPaneName:
bl callFunc

position_compare:
    .asciz "position_compare"
    .align 2

# Draw the graphic. (Register 3 argument already present so there's no need for register move.)
callFunc:
mflr r4
lis r11, setTextboxMessage@h
li r6, 0
ori r11, r11, setTextboxMessage@l
mtctr r11
bctrl

end:
