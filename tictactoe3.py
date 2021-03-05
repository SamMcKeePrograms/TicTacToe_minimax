import copy

count = 0

X = "X"
O = "O"
EMPTY = None

posDictionary = {"0, 0":"1", "0, 1":"2", "0, 2":"3", "1, 0":"4",
                 "1, 1":"5", "1, 2":"6", "2, 0":"7", "2, 1":"8",
                 "2, 2":"9"}

def getPlayerFromPos(pos, board):
    strVersion = str(pos)
    #print(strVersion)
    strVersion = strVersion[:-1]
    #print(strVersion)
    strVersion = strVersion[1:]
    #print(strVersion)
    posArr = posDictionary.get(strVersion)
    return posArr

def initial_state():
    """
    Returns starting state of the board.
    """
    #print("initial_state being ran")
    return [[EMPTY, X, EMPTY],
            [EMPTY,EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    #print("q") 
    count = 0
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if(board[i][j] != EMPTY):
                count += 1
    if(count % 2 == 0):
        return X
    else:
        return O

def actions(board):
    #print("t") 
    actionsList = []


    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if(board[i][j] == EMPTY):
                actionsList.append([i,j])

    return actionsList

def result(board, action):
    global count
    count += 1
    #print(str(count))
    #print("s")
    #print("Move: ")
    #print(action)
    #str(action)
    #print(str(type(board)))
    #print(str(type(action)))

    if(action == None):
        print("None")
    else:
        pass#print(action)
    
    actionsList = actions(board)
    resultBoard = copy.deepcopy(board)

    isValidMove = False

    #i = action[0]
    #j = action[1]
    #action = [i,j]


    for i in range(0,len(actionsList)):
        if(actionsList[i] == action):
            isValidMove = True
            break
    if(isValidMove):
        i = action[0]
        j = action[1]
        #print("i: "+str(i)+" j: "+str(j))
        resultBoard[i][j] = player(board)
#    if action in actionsList:
#        i = action[0]
#        j = action[1]
#        #print("i: "+str(i)+" j: "+str(j))
#        resultBoard[i][j] = player(board)
    
    return resultBoard

def winner(board):
    #print("d") 
    scores = [0,0,0,0,0,0,0,0]

    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if(board[i][j] != EMPTY):
                cost = (1 if board[i][j] == X else -1 if board[i][j] == O else 0)
                temp = int(getPlayerFromPos((i,j),board))
                #row1 score[0]
                if(temp == 1 or temp == 2 or temp == 3):
                    scores[0]+= cost
                #row2 score[1]
                if(temp == 4 or temp == 5 or temp == 6):
                    scores[1] += cost
                #row3 score[2]
                if(temp == 7 or temp == 8 or temp ==  9):
                    scores[2] += cost
                #col1 score[3]
                if(temp == 1 or temp == 4 or temp == 7):
                    scores[3] += cost
                #col2 score[4]
                if(temp == 2 or temp == 5 or temp == 8):
                    scores[4] += cost
                #col3 score[5]
                if(temp == 3 or temp == 6 or temp == 9):
                   scores[5] += cost
                #d1 score[6]
                if(temp == 1 or temp == 5 or temp == 9):
                    scores[6] += cost
                #d2 score[7]
                if(temp == 3 or temp == 5 or temp == 7):
                    scores[7] += cost
    xx = max(scores)
    oo = min(scores)
    #print  (scores)
    if(xx == oo):
        return None
    elif(xx == 3):
        return X
    elif(oo == -3):
        return O
    else:
        return None


def terminal(board):
    #print("c")
    if(winner(board) != None or actions(board) == []):
        return True
    else:
        return False

def utility(board):
    #print("b")
    winnerResult = winner(board)

    if(winnerResult == X):
        return 1
    elif(winnerResult == O):
        return -1
    else:
        return 0

def explore(board):
    #print("a")
    maxPlayer = None
    if(player(board) == X):
        maxPlayer = True
    else:
        maxPlayer = False
        
    if(terminal(board) == True):
        return utility(board)

    if(maxPlayer):
        actionsList = actions(board)
        maxEval = -999
        for child in actionsList:
            util = explore(result(board, child))
            #maxEval = max(maxEval, util)
            if(maxEval < util):
                maxEval = util
            
        return maxEval
    else:
        minEval = 999
        actionsList = actions(board)
        for child in actionsList:
            util = explore(result(board, child))
            #minEval = min(minEval, util)
            if(minEval > util):
                minEval = util
        return minEval

def minimax(board):
    
    #print("A")
    movesScores = []
    maxMinPlayer = (1 if player(board) == X else -1 if player(board) == O else 0)
    actionsList = actions(board)

    tieMove = None
    loseMove = None
    noMoves = False
    #for i in range(0,len(board)):
        #for j in range(0,len(board[i])):
            #if(board[i][j] == EMPTY):
                #return [1,1]

    if(terminal(board)):
        return None
    #print(actionsList)
    for action in actionsList:
        #print(action)
        tempBoard = copy.deepcopy(board)
        resultBoard = result(tempBoard, action)
        evaluation = explore(resultBoard)
        movesScores.append([evaluation, action])


    for results in movesScores:
        i,j = results[1]
        tupleAction = (i,j)
        if(results[0] == maxMinPlayer):
            return results[1]
        elif(results[0] == 0):
            tieMove = results[1]
        else:
            loseMove = results[1]

    if(tieMove != None):
        return tieMove
    elif(loseMove != None):
        return loseMove
    else:
        return None
#print(initial_state())
#print(result(initial_state(), (1,1)))
#print(minimax(initial_state()))
