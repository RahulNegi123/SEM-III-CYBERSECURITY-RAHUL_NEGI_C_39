# working OK in IDLE 
import os
import platform
import sys
import builtins
import time
gameBOARD=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
holdWINNINGpos=2
nowRUNNING=0
gamingLIST=[]
endNOWDRAW=-1
flag=0
endNOWWON=1
endNOW=1
flag3=0
drawORnot=-1
Game=nowRUNNING
participant=1
holdPOS='X'
flag1=0
def checkEMPTY(x):    
    if(gameBOARD[x]==' '):    
        return True    
    else:    
        return False
def checkWON():    
    global Game    
    if(gameBOARD[1]==gameBOARD[2]and gameBOARD[2]==gameBOARD[3]and gameBOARD[1]!=' '):    
        Game = endNOWWON    
    elif(gameBOARD[4]==gameBOARD[5]and gameBOARD[5]==gameBOARD[6]and gameBOARD[4]!=' '):    
        Game=endNOWWON    
    elif(gameBOARD[7]==gameBOARD[8]and gameBOARD[8]==gameBOARD[9]and gameBOARD[7]!=' '):    
        Game=endNOWWON    
    elif(gameBOARD[1]==gameBOARD[4]and gameBOARD[4]==gameBOARD[7]and gameBOARD[1]!=' '):    
        Game=endNOWWON    
    elif(gameBOARD[2]==gameBOARD[5]and gameBOARD[5]==gameBOARD[8]and gameBOARD[2]!=' '):    
        Game=endNOWWON    
    elif(gameBOARD[3]==gameBOARD[6]and gameBOARD[6]==gameBOARD[9]and gameBOARD[3]!=' '):    
        Game=endNOWWON    
    elif(gameBOARD[1]==gameBOARD[5]and gameBOARD[5]==gameBOARD[9]and gameBOARD[5]!=' '):    
        Game=endNOWWON    
    elif(gameBOARD[3]==gameBOARD[5]and gameBOARD[5]==gameBOARD[7]and gameBOARD[5]!=' '):    
        Game=endNOWWON    
    elif(gameBOARD[1]!=' 'and gameBOARD[2]!=' 'and gameBOARD[3]!=' 'and gameBOARD[4]!=' 'and gameBOARD[5]!=' 'and gameBOARD[6]!=' 'and gameBOARD[7]!=' 'and gameBOARD[8]!=' 'and gameBOARD[9]!=' '):    
        Game=endNOWDRAW    
    else:            
        Game=nowRUNNING
def drawBOARD():    
    print(" %c | %c | %c"%(gameBOARD[1],gameBOARD[2],gameBOARD[3]))    
    print("___|___|___")    
    print(" %c | %c | %c"%(gameBOARD[4],gameBOARD[5],gameBOARD[6]))    
    print("___|___|___")    
    print(" %c | %c | %c"%(gameBOARD[7],gameBOARD[8],gameBOARD[9]))    
    print("   |   |   ")
print("\n\n-----------------Welcome to tic tac toe game------------------\n\n")
print("BOARD MARKING SCHEME\n\n")
print('_1_|_2_|_3_')
print('\n')
print('_4_|_5_|_6_')    
print('\n')    
print(' 7 | 8 | 9 ')
print("participant 1 will mark with X and   participant 2 with O\n")
print('\n\nGAME WILL START NOW, PLEASE WAIT FEW SECONDS\n\n\n')
time.sleep(3)    
while(Game==nowRUNNING):    
    os.system('cls')    
    drawBOARD()
    if(participant%2!=0):    
        print('participant 1 please play now : ')    
        holdPOS='X'    
    else:    
        print('participant 2 please play now : ')    
        holdPOS='O'    
    choice=int(input("Enter any position b/w [1-9] to mark : \n"))    
    if(checkEMPTY(choice)):    
        gameBOARD[choice]=holdPOS    
        participant=participant+1
        checkWON()    
os.system('cls')    
drawBOARD()    
if(Game==endNOWDRAW):    
    print('Game is DRAWN\n\n')    
elif(Game==endNOWWON):    
    participant=participant-1
    if(participant%2!=0):    
        print('Participant 1 Wins the match')    
    else:    
        print('Participant 2 Wins the match')
print('Thanks for playing, Do want to play Again?')
