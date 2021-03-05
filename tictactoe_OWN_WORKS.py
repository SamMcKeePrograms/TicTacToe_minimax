import tictactoe3 as ttt
import copy
import pygame
import time



O = ttt.O
X = ttt.X
EMPTY = ttt.EMPTY
player = X
gameOver = False

posToCoord = {"1":"0 0", "2":"0 1", "3":"0 2",
              "4":"1 0", "5":"1 1", "6":"1 2",
              "7":"2 0", "8":"2 1", "9":"2 2"}


board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

def getPlayerCoordFromPos(pos):
    temp = list(posToCoord.get(str(pos)).split(" "))
    move = []
    move.append(int(temp[0]))
    move.append(int(temp[1]))
    return move

def printBoard(board):

    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if(board[i][j] == EMPTY):
                print("_ ", end="")
            else:
                print(board[i][j]+" ", end="")
        print()

def result(board, action):
    if(action == None):
        print("None")
    else:
        pass#print(action)
    
    actionsList = ttt.actions(board)
    resultBoard = copy.deepcopy(board)

    i = action[0]
    j = action[1]
    action = [i,j]
    
    if action in actionsList:
        i, j = action
        resultBoard[i][j] = ttt.player(board)
    
    return resultBoard
printBoard(board)
userPlayer = ""

while not gameOver:
    #gameOver = ttt.terminal(board)
    print("Player: "+player)
    if player == X and not ttt.terminal(board):
        print("*****Player Move*****")
        move = None
        validMove = False
        while not validMove:
                
            player = O
            move = int(input("Move: "))
            #print(ttt.actions(board))
            #print(getPlayerCoordFromPos(move))
            if getPlayerCoordFromPos(move) in ttt.actions(board):
                validMove = True
            else:
                print("Invalid Move Selected, try again")
        #print(str(type(ttt.result)))
        board = result(board, getPlayerCoordFromPos(move))
        player = O
        
    elif(player == O and not ttt.terminal(board)):
        print("*****AI MOVE****")
        move = ttt.minimax(board)
        print("Move: ")
        print(move)
        board = result(board, move)
        player = X
    
            
    #print(player)
    print()
    printBoard(board)
    gameOver = ttt.terminal(board)

win = ttt.winner(board)
print("Winner: "+str(win))

    
        
    
   
