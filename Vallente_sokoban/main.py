'''
NAME: JAMES LOURENCE T. VALLENTE
PROJECT: TERMINAL-BASED SOKOBAN GAME
SECTION: CMSC 12 T2-3L
'''
#IMPORT ESSENTIALS
from termcolor import colored
import platform
import os 
import time

#ARRAYS FOR STORING TIMES. EVERYTIME THE GAME OPENS, THE ARRAY GETS EMPTY.  
storeTIMESM1 = []                   #Storing 10x10 game mode  
storeTIMESM2 = []                   #Storing 15x15 game mode                
saveElapseArr = []                  #Storing sliced times for save-resume functions

#ADDITIONAL INITIALIZATIONS:
files1 = ["gt_ten_1.txt", "gt_ten_2.txt"]           #array for storing file names of 10x10 mode
cnt = 0                                             #index the file to be accessed
files2 = ["gf_fteen_1.txt", "gf_fteen_2.txt"]       #array for storing file names of 15x15 mode

#FUNCTIONS FOR TIME READING, ACCESSING, STORING IN AN ARRAY. 

#save time for mode 10x10
def saveTIMEM1(storeTIMESM1):
    fileHandler = open("saveTIMESM1.txt", "a")
    for line in storeTIMESM1:
        fileHandler.write(str(line) + "\n")
    fileHandler.close()

#acccessing the text file for 10x10 for times and storing it to an array
def readTIMEM1():
    storeTIMESM1 = []
    fileHandler = open("saveTIMESM1.txt", "r")
    for line in fileHandler:
         storeTIMESM1.append(line[:-1])
    fileHandler.close()
    return storeTIMESM1

#save time for mode 15x15
def saveTIMEM2(storeTIMESM2):
    fileHandler = open("saveTIMESM2.txt", "a")
    for line in storeTIMESM2:
        fileHandler.write(str(line) + "\n")
    fileHandler.close()

#acccessing the text file for 15x15 for times and storing it to an array
def readTIMEM2():
    storeTIMESM2 = []
    fileHandler = open("saveTIMESM2.txt", "r")
    for line in fileHandler:
         storeTIMESM2.append(line[:-1])
    fileHandler.close()
    return storeTIMESM2

#save time for save-resume functions
def saveElapse(saveElapseArr):
    fileHandler = open("saveElapse.txt", "a")
    for line in saveElapseArr:
        fileHandler.write(str(line) + "\n")
    fileHandler.close()

#accessing the text file for save-resume times and storing it to an array
def loadElapse():
    saveElapseArr = []
    fileHandler = open("saveElapse.txt", "r")
    for line in fileHandler:
         saveElapseArr.append(line[:-1])
    fileHandler.close()
    return saveElapseArr

#everytime a new game is saved, a text file containing timestamps for save-resume functions will be overwritten
def overwrite():
    fileHandler = open("saveElapse.txt", "w")
    fileHandler.write("")
    fileHandler.close()
    

#CLEAR THE TERMINAL EVERY MOVEVEMT
def sys_clr():
    if platform.system() == "Windows":
        os.system("cls")
    else: 
        os.system("clear")

#MAP ACCESSING, LOADING, AND PRINTING
  
#load/open map for 10x10 mode
def loadMap(cnt): 
    storeMap = []                           #lists of all lines
    subMap = []                             #for storing a line a list --> store this to storeMap = []
    fileHandle = open(files1[cnt], "r")

    for line in fileHandle:
        for item in line[:-1]:
            subMap.append(item)
        storeMap.append(subMap)
        subMap = []
        
    fileHandle.close()
    return storeMap

#load/open map for 15x15 mode
def loadMap2(cnt): 
    storeMap = [] 
    subMap = [] 
    fileHandle = open(files2[cnt], "r")

    for line in fileHandle:
        for item in line[:-1]:
            subMap.append(item)
        storeMap.append(subMap)
        subMap = []
        
    fileHandle.close()
    return storeMap

#load saved map during resume
def loadMap3(): 
    storeMap = [] 
    subMap = [] 
    fileHandle = open("saved.txt", "r")

    for line in fileHandle:
        for item in line[:-1]:
            subMap.append(item)
        storeMap.append(subMap)
        subMap = []
        
    fileHandle.close()
    return storeMap

#printing saved map during resume
def printMap2(storeMap):  
    for lst in storeMap[1:]:
        for conts in lst:
            if conts == "#":
                print(colored(conts, "red"), end=" ")
            elif conts == "P":
                print(colored(conts, "green"), end=" ")
            else:
                print(conts, end=" ")
        print()
        
#printing map for new games --> 10x10 and 15x15 mode
def printMap(storeMap):  
    for lst in storeMap:
        for conts in lst:
            if conts == "#":
                print(colored(conts, "red"), end=" ")
            elif conts == "P":
                print(colored(conts, "green"), end=" ")
            else:
                print(conts, end=" ")
        print()

#SAVING GAME MAPS TO A TEXT FILE

#first iteration for save 
def save(storeMap, code):
    fileHandler = open("saved.txt", "w")
    fileHandler.write(code + "\n")
    for lst in storeMap:
        for value in lst:
            fileHandler.write(value)
        fileHandler.write("\n")
    fileHandler.close()
        
    print("Progress saved succesfully!")
    cont = int(input("Press [0] to continue: "))
    exit()
    
#next save iteration
def save2(storeMap):
    fileHandler = open("saved.txt", "w")
    for lst in storeMap:
        for value in lst:
            fileHandler.write(value)
        fileHandler.write("\n")
    fileHandler.close()    
    print("Progress saved succesfully!")
    cont = int(input("Press [0] to continue: "))
    exit()
         
#MOVEMENT MECHANICS  [w-a-s-d] keys

#function for moving up "w" 
def moveUP(storeMap):
    for i in range(len(storeMap)):
        for j in range(len(storeMap[i])):
            if storeMap[i][j] == "P":
                if storeMap[i-1][j] != "#":
                    if storeMap[i-1][j] == "B":
                        if storeMap[i-2][j] == "-":
                            storeMap[i-1][j], storeMap[i-2][j] = storeMap[i-2][j], storeMap[i-1][j] #swap B and -
                            storeMap[i][j], storeMap[i-1][j] = storeMap[i-1][j], storeMap[i][j] #swap P and -
                            return storeMap
                        if storeMap[i-2][j] == "B":
                            return None
                        if storeMap[i-2][j] == "#":
                            return None
                        if storeMap[i-2][j] == "@":
                            if storeMap[i-3][j] != "@":
                                storeMap[i-2][j] = "*" #a box is in the destination
                                storeMap[i-1][j] = "-"
                                storeMap[i][j], storeMap[i-1][j] = storeMap[i-1][j], storeMap[i][j]
                                return storeMap
                            elif storeMap[i-3][j] == "@": #changes here
                                storeMap[i][j] = "-"
                                storeMap[i-1][j] = "P"
                                storeMap[i-2][j] = "*"
                                return storeMap
                    elif storeMap[i-1][j] == "-":
                        storeMap[i][j], storeMap[i-1][j] = storeMap[i-1][j], storeMap[i][j]
                        return storeMap    
                    elif storeMap[i-1][j] == "*": #changes here
                        if storeMap[i-2][j] != "#":
                            if storeMap[i-2][j] == "@":
                                storeMap[i][j] = "-"
                                storeMap[i-1][j] = "O"
                                storeMap[i-2][j] = "*"
                                return storeMap
                if storeMap[i-1][j] == "@":
                    storeMap[i-1][j] = "O" #player is in the destinaton
                    storeMap[i][j] = "-"
                    return storeMap
                
                if storeMap[i-1][j] == "*":
                    if storeMap[i-2][j] != "#":
                        storeMap[i][j] = "-"
                        storeMap[i-2][j] = "B"
                        storeMap[i-1][j] = "O"
                        return storeMap
                    
            elif storeMap[i][j] == "O":
                if storeMap[i-2][j] != "#":
                    if storeMap[i-1][j] == "B":
                        storeMap[i-2][j] = "B"
                        storeMap[i][j] = "@"
                        storeMap[i-1][j] = "P"
                        return storeMap
                    elif storeMap[i-1][j] == "*": #changes here
                        storeMap[i][j] = "@"
                        storeMap[i-1][j] = "O"
                        storeMap[i-2][j] = "B"
                        return storeMap
                    else:
                        storeMap[i][j] = "@"
                        storeMap[i-1][j] = "P"
                        return storeMap
                elif storeMap[i-2][j] == "#":
                    if storeMap[i-1][j] == "-":
                        storeMap[i-1][j] = "P"
                        storeMap[i][j] = "@"

#function for moving down "s"                                                            
def moveDOWN(storeMap):
    for i in range(len(storeMap)):
        for j in range(len(storeMap[i])):
            if storeMap[i][j] == "P":
                if storeMap[i+1][j] != "#":
                    if storeMap[i+1][j] == "B":
                        if storeMap[i+2][j] == "-":
                            storeMap[i+1][j], storeMap[i+2][j] = storeMap[i+2][j], storeMap[i+1][j] #swap B and -
                            storeMap[i][j], storeMap[i+1][j] = storeMap[i+1][j], storeMap[i][j] #swap P and -
                            return storeMap
                        if storeMap[i+2][j] == "B":
                            return None
                        if storeMap[i+2][j] == "#":
                            return None
                        if storeMap[i+2][j] == "@":
                            if storeMap[i+3][j] != "@":
                                storeMap[i+2][j] = "*" #a box is in the destination
                                storeMap[i+1][j] = "P"
                                storeMap[i][j] = "-"
                                return storeMap
                            elif storeMap[i+3][j] == "@": 
                                storeMap[i][j] = "-"
                                storeMap[i+1][j] = "P"
                                storeMap[i+2][j] = "*"
                                return storeMap
                    elif storeMap[i+1][j] == "-":
                        storeMap[i][j], storeMap[i+1][j] = storeMap[i+1][j], storeMap[i][j]
                        return storeMap 
                    elif storeMap[i+1][j] == "*": 
                        if storeMap[i+2][j] != "#":
                            if storeMap[i+2][j] == "@":
                                storeMap[i][j] = "-"
                                storeMap[i+1][j] = "O"
                                storeMap[i+2][j] = "*"
                                return storeMap
                            elif storeMap[i+2][j] == "-":
                                storeMap[i][j] = "-"
                                storeMap[i+1][j] = "O"
                                storeMap[i+2][j] = "B"
                                return storeMap
                            elif storeMap[i+2][j] == "B":
                                return None
                                
                if storeMap[i+1][j] == "@":
                    storeMap[i+1][j] = "O" #player is in the destinaton
                    storeMap[i][j] = "-"
                    return storeMap
                
                if storeMap[i+1][j] == "*": 
                    if storeMap[i+2][j] != "#":
                        storeMap[i][j] = "-"
                        storeMap[i+2][j] = "*"
                        storeMap[i+1][j] = "O"
                        return storeMap
            
            
            elif storeMap[i][j] == "O":
                if storeMap[i+2][j] != "#":
                    if storeMap[i+1][j] == "B":
                        if storeMap[i+2][j] != "@":
                            storeMap[i+2][j] = "B"
                            storeMap[i][j] = "@"
                            storeMap[i+1][j] = "P"
                            return storeMap 
                    if storeMap[i+1][j] == "B":
                        if storeMap[i+2][j] == "@":
                            storeMap[i+2][j] = "*"
                            storeMap[i][j] = "@"
                            storeMap[i+1][j] = "P"
                            return storeMap 
                    elif storeMap[i+1][j] == "*": 
                        storeMap[i][j] = "@"
                        storeMap[i+1][j] = "O"
                        storeMap[i+2][j] = "B"
                        return storeMap
                    else:
                        storeMap[i][j] = "@"
                        storeMap[i+1][j] = "P" 
                        return storeMap

#function for moving right "d"                  
def moveRIGHT(storeMap):
    for i in range(len(storeMap)):
        for j in range(len(storeMap[i])):
            if storeMap[i][j] == "P":
                if storeMap[i][j+1] != "#":
                    if storeMap[i][j+1] == "B":
                        if storeMap[i][j+2] == "-":
                            storeMap[i][j+1], storeMap[i][j+2] = storeMap[i][j+2], storeMap[i][j+1] #swap B and -
                            storeMap[i][j], storeMap[i][j+1] = storeMap[i][j+1], storeMap[i][j] #swap P and -
                            return storeMap
                        if storeMap[i][j+2] == "B":
                            return None
                        if storeMap[i][j+2] == "#":
                            return None
                        if storeMap[i][j+2] == "@":
                            storeMap[i][j+2] = "*" #a box is in the destination
                            storeMap[i][j+1] = "-"
                            storeMap[i][j], storeMap[i][j+1] = storeMap[i][j+1], storeMap[i][j]
                            return storeMap
                    elif storeMap[i][j+1] == "-":
                        storeMap[i][j], storeMap[i][j+1] = storeMap[i][j+1], storeMap[i][j]
                        return storeMap 
                    
                if storeMap[i][j+1] == "@":
                    storeMap[i][j+1] = "O" #player is in the destinaton
                    storeMap[i][j] = "-"
                    return storeMap
                
                if storeMap[i][j+1] == "*":
                    if storeMap[i][j+2] != "#":
                        storeMap[i][j] = "-"
                        storeMap[i][j+2] = "B"
                        storeMap[i][j+1] = "O"
                        return storeMap
            
            
            elif storeMap[i][j] == "O":
                if storeMap[i][j+2] != "#":
                    if storeMap[i][j+1] == "B":
                        storeMap[i][j+2] = "B"
                        storeMap[i][j] = "@"
                        storeMap[i][j+1] = "P"
                        return storeMap  
                    else:
                        storeMap[i][j] = "@"
                        storeMap[i][j+1] = "P"
                        return storeMap 
 
#function for moving down "a"                     
def moveLEFT(storeMap):
    for i in range(len(storeMap)):
        for j in range(len(storeMap[i])):
            if storeMap[i][j] == "P":
                if storeMap[i][j-1] != "#":
                    if storeMap[i][j-1] == "B":
                        if storeMap[i][j-2] == "-":
                            storeMap[i][j-1], storeMap[i][j-2] = storeMap[i][j-2], storeMap[i][j-1] #swap B and -
                            storeMap[i][j], storeMap[i][j-1] = storeMap[i][j-1], storeMap[i][j] #swap P and -
                            return storeMap
                        if storeMap[i][j-2] == "B":
                            return None
                        if storeMap[i][j-2] == "#":
                            return None
                        if storeMap[i][j-2] == "@":
                            storeMap[i][j-2] = "*" #a box is in the destination
                            storeMap[i][j-1] = "-"
                            storeMap[i][j], storeMap[i][j-1] = storeMap[i][j-1], storeMap[i][j]
                            return storeMap
                    elif storeMap[i][j-1] == "-":
                        storeMap[i][j], storeMap[i][j-1] = storeMap[i][j-1], storeMap[i][j]
                        return storeMap 
                    
                if storeMap[i][j-1] == "@":
                    storeMap[i][j-1] = "O" #player is in the destinaton
                    storeMap[i][j] = "-"
                    return storeMap
                
                if storeMap[i][j-1] == "*":
                    if storeMap[i][j-2] != "#":
                        storeMap[i][j] = "-"
                        storeMap[i][j-2] = "B"
                        storeMap[i][j-1] = "O"
                        return storeMap
            
            
            elif storeMap[i][j] == "O":
                if storeMap[i][j-2] != "#":
                    if storeMap[i][j-1] == "B":
                        storeMap[i][j-2] = "B"
                        storeMap[i][j] = "@"
                        storeMap[i][j-1] = "P"
                        return storeMap  
                    else:
                        storeMap[i][j] = "@"
                        storeMap[i][j-1] = "P" 
                        return storeMap
                if storeMap[i][j-1] == "-":
                    storeMap[i][j] = "@"
                    storeMap[i][j-1] = "P"
                    return storeMap

#w-a-s-d keys validations and function calls       
def wasdKey(keyInput, storeMap): 
    if keyInput == "w":
        moveUP(storeMap)

    elif keyInput == "s":
        moveDOWN(storeMap)
        
    elif keyInput == "d":
        moveRIGHT(storeMap)
    
    elif keyInput == "a":
        moveLEFT(storeMap)
        
#PRINTING SCREENS FOR SUCCESSFUL PLAY

#winscreen for 10x10
def winScreen(startTIME, endTIME, storeTIMESM1):
    print()
    print(colored("Congratulations! You win the game", "blue"))
    elapsed = int(endTIME - startTIME)
    storeTIMESM1.append(elapsed)
    saveTIMEM1(storeTIMESM1)
    print("Time spent:", elapsed, "seconds")
    print()
    viewHS = input("Enter [1] to view highest score, [0] to exit: ")
    if viewHS == "1":
        storeTIMESM1 = readTIMEM1()
        storeTIMESM1.sort()
        print("-" * 47)
        print("HIGHEST SCORE IN 10X10 MODE:", storeTIMESM1[0], "seconds")
        for i in range(len(storeTIMESM1)):
            if storeTIMESM1[i] == str(elapsed):
                print(colored("You are on the position number", "yellow"), end=" ")
                print(colored(i+1, "yellow"))
                print("-" * 47)
                break
    elif viewHS == "0":
        exit()
    exit()
    
#winscreen for 15x15
def winScreen2(startTIME, endTIME, storeTIMESM2):
    print()
    print(colored("Congratulations! You win the game", "blue"))
    elapsed = int(endTIME - startTIME)
    storeTIMESM2.append(elapsed)
    saveTIMEM2(storeTIMESM2)
    print("Time spent:", elapsed, "seconds")
    print()
    viewHS = input("Enter [1] to view highest score, [0] to exit: ")
    if viewHS == "1":
        storeTIMESM2 = readTIMEM2()
        storeTIMESM2.sort()
        print("-" * 47)
        print("HIGHEST SCORE IN 15x15 MODE:", storeTIMESM2[0], "seconds")
        for i in range(len(storeTIMESM2)):
            if storeTIMESM2[i] == str(elapsed):
                print(colored("You are on the position number", "yellow"), end=" ")
                print(colored(i+1, "yellow"))
                print("-" * 47)
                break
    elif viewHS == "0":
        exit()
    exit()

#winscreen for save-resume-finish mechanics (10x10 mode)
def winScreen3(): 
    print()
    print(colored("Congratulations! You win the game", "blue"))
    saveElapseArr = loadElapse()                #load the array from text file
    timeSum = 0
    for tme in saveElapseArr:                   #summing all times
        timeSum = timeSum + int(tme)
    print("Time spent:", timeSum, "seconds")
    sumArr = []
    sumArr.append(timeSum)
    saveTIMEM1(sumArr)
    print()
    viewHS = input("Enter [1] to view highest score, [0] to exit: ")
    if viewHS == "1":
        storeTIMESM1 = readTIMEM1()
        storeTIMESM1.sort()
        print("-" * 47)
        print("HIGHEST SCORE IN 10x10 MODE:", storeTIMESM1[0], "seconds")
        for i in range(len(storeTIMESM1)):
            if storeTIMESM1[i] == str(timeSum):
                print(colored("You are on the position number", "yellow"), end=" ")
                print(colored(i+1, "yellow"))
                print("-" * 47)
                break
    elif viewHS == "0":
        exit()
    exit()

#winscreen for save-resume-finish mechanics (15x15 mode)
def winScreen4(): 
    print()
    print(colored("Congratulations! You win the game", "blue"))
    saveElapseArr = loadElapse()                #load the array from text file
    timeSum = 0
    for tme in saveElapseArr:                   #summing all times
        timeSum = timeSum + int(tme)
    print("Time spent:", timeSum, "seconds")
    sumArr = []
    sumArr.append(timeSum)
    saveTIMEM2(sumArr)
    print()
    viewHS = input("Enter [1] to view highest score, [0] to exit: ")
    if viewHS == "1":
        storeTIMESM2 = readTIMEM2()
        storeTIMESM2.sort()
        print("-" * 47)
        print("HIGHEST SCORE IN 15x15 MODE:", storeTIMESM2[0], "seconds")
        for i in range(len(storeTIMESM2)):
            if storeTIMESM2[i] == str(timeSum):
                print(colored("You are on the position number", "yellow"), end=" ")
                print(colored(i+1, "yellow"))
                print("-" * 47)
                break
    elif viewHS == "0":
        exit()
    exit()
    
#PLAYING GUIDE / FUNCTIONALITIES
def mechanics():
    print(colored("PLAYING GUIDE", "blue"))
    print
    print("CHARACTERS    ['B' : BOX | '#' : WALL | '-' : SPACE | 'P' : PLAYER]")
    print("OTHERS        ['@' : DESTINATION | 'O'  : P is in @ | '*' : B is in @]")
    print("MOVEMENT KEYS ['W' : UP | 'S' : DOWN | 'A' : LEFT | 'D' : RIGHT] ")
    print()
    
#INSTRUCTIONS AND MECHANICS 
def start_new():
    print()
    print(colored("Games Modes", "blue"))
    print("[1] 10 x 10 grid")
    print("[2] 15 x 15 grid")
    print()
    choice = int(input("Enter a game mode from above: "))
    choose_mode(choice)  
    
#CONTROLS: CHECKING THE INPUT FOR MOVEMENT MECHANICS
#controls for 10x10 node
def controls(startTIME): 
    
    storeMap = loadMap(cnt)
    lvl = True
    while lvl:
        sys_clr()
        mechanics()
        print()
        print("MODE: 10X10 | LEVEL: 1")
        print()
        printMap(storeMap)
        countB = 0
        for i in storeMap:
            for j in i:
                if j == "B":
                    countB += 1
        if countB > 0:
            print()
            print(colored("[1] SAVE AND EXIT", "yellow")) 
            print(colored("[0] EXIT ONLY", "yellow"))
            print("- " * 10)       
            keyInput = input(colored("Enter a key: ", "yellow"))
            if keyInput == "1":
                code = "alvl1"          #code for accessing the mode and level
                overwrite()             #deletes the previewsly saved timestamps
                endTIME = time.time()
                elapse = int(endTIME - startTIME)
                saveElapseArr.append(elapse)
                saveElapse(saveElapseArr)
                save(storeMap, code)
                return None
            elif keyInput == "0":
                print()
                print(colored("Thanks for playing! Goodbye", "blue"))
                exit()
            wasdKey(keyInput, storeMap)
        elif countB == 0:

            lvl = False

    storeMap = loadMap(cnt+1)
    lvl = True
    while lvl:
        sys_clr()
        mechanics()
        print()
        print("MODE: 10X10 | LEVEL: 2")
        print()
        printMap(storeMap)
        countB = 0
        for i in storeMap:
            for j in i:
                if j == "B":
                    countB += 1
        if countB > 0:  
            print()
            print(colored("[1] SAVE AND EXIT", "yellow")) 
            print(colored("[0] EXIT ONLY", "yellow"))
            print("- " * 10)         
            keyInput = input(colored("Enter a key: ", "yellow"))
            if keyInput == "1":
                code = "alvl2"                      #code for accessing the mode and level
                overwrite()
                endTIME = time.time()
                elapse = int(endTIME - startTIME)
                saveElapseArr.append(elapse)
                saveElapse(saveElapseArr)
                save(storeMap, code)
                return None
            elif keyInput == "0":
                print()
                print(colored("Thanks for playing! Goodbye", "blue"))
                exit()
            wasdKey(keyInput, storeMap)
        elif countB == 0:
            endTIME = time.time()
            winScreen(startTIME, endTIME, storeTIMESM1)
            lvl = False
        
        
    winScreen()

#controls for 15x15 mode
def controls2(startTIME): 
    storeMap = loadMap2(cnt)
    lvl = True
    while lvl:
        sys_clr()
        mechanics()
        print()
        print("MODE: 15X15          LEVEL: 1")
        print()
        printMap(storeMap)
        countB = 0
        for i in storeMap:
            for j in i:
                if j == "B":
                    countB += 1
        if countB > 0: 
            print()
            print(colored("[1] SAVE AND EXIT", "yellow")) 
            print(colored("[0] EXIT ONLY", "yellow"))
            print("- " * 15)          
            keyInput = input(colored("Enter a key: ", "yellow"))
            if keyInput == "1":
                code = "blvl1" #code for accessing the mode and level
                overwrite()
                endTIME = time.time()
                elapse = int(endTIME - startTIME)
                saveElapseArr.append(elapse)
                saveElapse(saveElapseArr)
                save(storeMap, code)
                return None
            elif keyInput == "0":
                print()
                print(colored("Thanks for playing! Goodbye", "blue"))
                exit()
            wasdKey(keyInput, storeMap)
        elif countB == 0:
            lvl = False

    storeMap = loadMap2(cnt+1)
    lvl = True
    while lvl:
        sys_clr()
        mechanics()
        print()
        print("MODE: 15X15          LEVEL: 2")
        print()
        printMap(storeMap)
        countB = 0
        for i in storeMap:
            for j in i:
                if j == "B":
                    countB += 1
        if countB > 0: 
            print()
            print(colored("[1] SAVE AND EXIT", "yellow")) 
            print(colored("[0] EXIT ONLY", "yellow"))
            print("- " * 15)          
            keyInput = input(colored("Enter a key: ", "yellow"))
            if keyInput == "1":
                code = "blvl2" #code for accessing the mode and level
                overwrite()
                endTIME = time.time()
                elapse = int(endTIME - startTIME)
                saveElapseArr.append(elapse)
                saveElapse(saveElapseArr)
                save(storeMap, code)
                return None
            elif keyInput == "0":
                print()
                print(colored("Thanks for playing! Goodbye", "blue"))
                exit()
            wasdKey(keyInput, storeMap)
        elif countB == 0:
            endTIME = time.time()
            winScreen2(startTIME, endTIME, storeTIMESM2)
            lvl = False
    winScreen2()        


#CONTROLS: ACCESSING LAST SAVED GAME
def return_last(storeMap, startTIME):
    sys_clr()
    from_code = ""
    for chars in storeMap[0]:
        from_code = from_code + chars
    
    if from_code == "alvl1":
        lvl = True
        while lvl:
            sys_clr()
            mechanics()
            print()
            print("MODE: 10X10 | LEVEL: 1")
            print()
            printMap2(storeMap)
            countB = 0
            for i in storeMap:
                for j in i:
                    if j == "B":
                        countB += 1
            if countB > 0:
                print()
                print(colored("[1] SAVE AND EXIT", "yellow")) 
                print(colored("[0] EXIT ONLY", "yellow"))
                print("- " * 10)       
                keyInput = input(colored("Enter a key: ", "yellow"))
                if keyInput == "1":
                    endTIME = time.time()                        #stop the time when the game is saved
                    elapse = int(endTIME - startTIME)
                    saveElapseArr.append(elapse)
                    saveElapse(saveElapseArr)
                    save2(storeMap)
                    return None
                elif keyInput == "0":
                    print()
                    print(colored("Thanks for playing! Goodbye", "blue"))
                    exit()
                wasdKey(keyInput, storeMap)
            elif countB == 0:
                lvl = False
                
        storeMap = loadMap(cnt+1)
        lvl = True
        while lvl:
            sys_clr()
            mechanics()
            print()
            print("MODE: 10X10 | LEVEL: 2")
            print()
            printMap(storeMap)
            countB = 0
            for i in storeMap:
                for j in i:
                    if j == "B":
                        countB += 1
            if countB > 0:  
                print()
                print(colored("[1] SAVE AND EXIT", "yellow")) 
                print(colored("[0] EXIT ONLY", "yellow"))
                print("- " * 10)         
                keyInput = input(colored("Enter a key: ", "yellow"))
                if keyInput == "1":
                    code = "alvl2"                                  #code for accessing the mode and level
                    endTIME = time.time()
                    elapse = int(endTIME - startTIME)
                    saveElapseArr.append(elapse)
                    saveElapse(saveElapseArr)
                    save(storeMap, code)
                    return None
                elif keyInput == "0":
                    print()
                    print(colored("Thanks for playing! Goodbye", "blue"))
                    exit()
                wasdKey(keyInput, storeMap)
            elif countB == 0:
                winScreen3()
                lvl = False
    elif from_code == "alvl2":
        lvl = True
        while lvl:
            sys_clr()
            mechanics()
            print()
            print("MODE: 10X10 | LEVEL: 2")
            print()
            printMap2(storeMap)
            countB = 0
            for i in storeMap:
                for j in i:
                    if j == "B":
                        countB += 1
            if countB > 0:  
                print()
                print(colored("[1] SAVE AND EXIT", "yellow")) 
                print(colored("[0] EXIT ONLY", "yellow"))
                print("- " * 10)         
                keyInput = input(colored("Enter a key: ", "yellow"))
                if keyInput == "1":
                    endTIME = time.time()
                    elapse = int(endTIME - startTIME)
                    saveElapseArr.append(elapse)
                    saveElapse(saveElapseArr)
                    save2(storeMap)
                    return None
                elif keyInput == "0":
                    print()
                    print(colored("Thanks for playing! Goodbye", "blue"))
                    exit()
                wasdKey(keyInput, storeMap)
            elif countB == 0:
                endTIME = time.time()
                elapse = int(endTIME - startTIME)
                saveElapseArr.append(elapse)
                saveElapse(saveElapseArr)
                winScreen3()
                lvl = False
    elif from_code == "blvl1":
        lvl = True
        while lvl:
            sys_clr()
            mechanics()
            print()
            print("MODE: 15X15          LEVEL: 1")
            print()
            printMap2(storeMap)
            countB = 0
            for i in storeMap:
                for j in i:
                    if j == "B":
                        countB += 1
            if countB > 0: 
                print()
                print(colored("[1] SAVE AND EXIT", "yellow")) 
                print(colored("[0] EXIT ONLY", "yellow"))
                print("- " * 15)          
                keyInput = input(colored("Enter a key: ", "yellow"))
                if keyInput == "1":
                    endTIME = time.time()
                    elapse = int(endTIME - startTIME)
                    saveElapseArr.append(elapse)
                    saveElapse(saveElapseArr)
                    save2(storeMap)
                    return None
                elif keyInput == "0":
                    print()
                    print(colored("Thanks for playing! Goodbye", "blue"))
                    exit()
                wasdKey(keyInput, storeMap)
            elif countB == 0:
                lvl = False

        storeMap = loadMap2(cnt+1)
        lvl = True
        while lvl:
            sys_clr()
            mechanics()
            print()
            print("MODE: 15X15          LEVEL: 2")
            print()
            printMap(storeMap)
            countB = 0
            for i in storeMap:
                for j in i:
                    if j == "B":
                        countB += 1
            if countB > 0: 
                print()
                print(colored("[1] SAVE AND EXIT", "yellow")) 
                print(colored("[0] EXIT ONLY", "yellow"))
                print("- " * 15)          
                keyInput = input(colored("Enter a key: ", "yellow"))
                if keyInput == "1":
                    code = "blvl2" 
                    endTIME = time.time()
                    elapse = int(endTIME - startTIME)
                    saveElapseArr.append(elapse)
                    saveElapse(saveElapseArr)
                    save(storeMap, code)
                    return None
                elif keyInput == "0":
                    print()
                    print(colored("Thanks for playing! Goodbye", "blue"))
                    exit()
                wasdKey(keyInput, storeMap)
            elif countB == 0:
                winScreen4()
                lvl = False   
                
    elif from_code == "blvl2":     
        lvl = True
        while lvl:
            sys_clr()
            mechanics()
            print()
            print("MODE: 15X15          LEVEL: 2")
            print()
            printMap2(storeMap)
            countB = 0
            for i in storeMap:
                for j in i:
                    if j == "B":
                        countB += 1
            if countB > 0: 
                print()
                print(colored("[1] SAVE AND EXIT", "yellow")) 
                print(colored("[0] EXIT ONLY", "yellow"))
                print("- " * 15)          
                keyInput = input(colored("Enter a key: ", "yellow"))
                if keyInput == "1":
                    endTIME = time.time()
                    elapse = int(endTIME - startTIME)
                    saveElapseArr.append(elapse)
                    saveElapse(saveElapseArr)
                    save2(storeMap)
                    return None
                elif keyInput == "0":
                    print()
                    print(colored("Thanks for playing! Goodbye", "blue"))
                    exit()
                wasdKey(keyInput, storeMap)
            elif countB == 0:
                endTIME = time.time()
                elapse = int(endTIME - startTIME)
                saveElapseArr.append(elapse)
                saveElapse(saveElapseArr)
                winScreen4()
                lvl = False 

#LOADING THE MODE AND DISPLAYING CONTROLS            
def choose_mode(choice):
    print()
    if choice == 1:
        startTIME = time.time()
        controls(startTIME)             #opens a text file of grid 10*10 #call function (inside the function, call fist level, then second level)
    elif choice == 2:
        startTIME = time.time()
        controls2(startTIME)            #opens a text file of grid 15*15 #call function (inside the function, call fist level (3 boxes), then second level (6boxes))
    else:
        print(colored("Invalid Choice. Try again", "red"))
        start_new()
           
#DISPLAYING HIGH SCORES AT MENU
def highscores():
    sys_clr()
    print()
    print("- " * 24)
    print()
    
    print(colored("HIGH SCORES", "yellow"))
    storeTIMESM1 = readTIMEM1()
    storeTIMESM1.sort()
    print("HIGHEST SCORE IN 10x10 MODE:", storeTIMESM1[0], "seconds")
    
    storeTIMESM2 = readTIMEM2()
    storeTIMESM2.sort()
    print("HIGHEST SCORE IN 15x15 MODE:", storeTIMESM2[0], "seconds")
    print()
    print("- " * 24)
    print()
    mainMENU(storeMap)
 
#MAIN MENU/ START    
def mainMENU(storeMap):
    print(colored("MAIN MENU", "blue"))
    print("[0] View Highscores")
    print("[1] Start a new game")
    print("[2] Return from last saved")
    print("[3] Exit")
    print()
    first_option = int(input("Enter an option: ")) #option for first main menu
    
    #conditions after choosing an option
    if first_option == 1:
        start_new()
    elif first_option == 2:
        storeMap = loadMap3()
        startTIME = time.time()
        return_last(storeMap, startTIME)
    elif first_option == 3:
        print(colored("Thanks for playing! Goodbye", "blue"))
        exit()
    elif first_option == 0:
        highscores()
    else: 
        print(colored("Invalid option. Try again.", "red"))
        print()
        mainMENU()
        
#WELCOME NOTES
def welcome(storeMap):
    sys_clr()
    print("- "*24)
    print()
    print(colored("WELCOME TO SOKOBAN GAME!", "yellow"))
    print()
    print(colored("To continue, please pick an option below.", "yellow"))
    print()
    print("- "*24)
    print()
    mainMENU(storeMap)

#------ MAIN ------#
#calling functions/start
storeMap = loadMap(cnt)
welcome(storeMap)




        
        