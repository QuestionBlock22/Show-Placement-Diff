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
lwz r5, 0xB70 (r12)                                         # racedata -> racesScenario -> settings -> gameMode
cmpwi r5, 7                                                 # Check if the current game mode is Friend Rooms.
beq gameModeFriendRoom
bgt end
cmpwi r5, 0                                                 # Check if the current game mode is Grand Prix.
beq gameModeGP
lwz r12, sectionMgrBase@l (r11)
lwz r11, 0x98 (r12)
lwz r4, 0x60 (r11)                                          # sectionMgr -> sectionParams -> vsRaceNumber
cmpwi r4, 1
beq end
b processPositions

gameModeGP:
lbz r4, 0xB8C (r12)                                         # racedata -> racesScenario -> settings -> raceNumber
cmpwi r4, 0
beq end
b processPositions

gameModeFriendRoom:
lwz r12, sectionMgrBase@l (r11)
lwz r11, 0x98 (r12)
lwz r4, 0x2d0 (r11)                                         # sectionMgr -> sectionParams -> onlineParams -> onlineRaceNumber
cmpwi r4, 0
beq end

processPositions:
# Get the current player ID and their previous position.
lwz r11, -raceDataBase@l (r8)
mulli r0, r31, 240
addi r6, r11, 40
add r8, r6, r0

# Compare game modes again. If the current game mode is Friend Rooms OR Grand Prix, make sure to compare the race number based on the hexadecimal system, otherwise compare based on the decimal system.
cmpwi r5, 7
cmpwi cr1, r5, 0
cror 4*cr0+eq, 4*cr0+eq, 4*cr1+eq                            # if (scenario.settings.gameMode == MODE_FRIEND_ROOM || scenario.settings.gameMode == MODE_GRAND_PRIX)
beq getHexRaceNumber

# Compare decimal race number (VS).
cmpwi r4, 2
bne loadFinalPosition
b loadPreviousPosition

# Compare hexadecimal race number (GP, FROOM).
getHexRaceNumber:
cmpwi r4, 1
bne loadFinalPosition

loadPreviousPosition:
lbz r12, 0xE1 (r8)                                          # racedata -> racesScenario -> players[12] -> previousPosition
b comparePlacements

loadFinalPosition:
lbz r12, 0xE0 (r8)                                          # racedata -> racesScenario -> players[12] -> finalPosition

# Compare the player's placement from the previous race with the current race.
comparePlacements:
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

# Draw the graphic.
callFunc:
mflr r4
lis r11, setTextboxMessage@h
li r6, 0
ori r11, r11, setTextboxMessage@l
mtctr r11
bctrl

end: