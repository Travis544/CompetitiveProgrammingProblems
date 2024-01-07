
powerOf3=[0]*9
powerOf3[0] =1
for i in range(1, len(powerOf3)):
    powerOf3[i] = powerOf3[i-1]*3


hashmap = dict()
hashmap[2] = dict()
hashmap[1] = dict()
board = [0]*9


def checkWin(board, player):
    
    if board[0] == player and board[1] == player and board[2] == player:
        return True

    if board[3] == player and board[4] == player and board[5] == player:
        return True
    
    if board[6] == player and board[7] == player and board[8] == player:
        return True

    if board[0] == player and board[3] == player and board[6] == player:
        return True

    if board[1] == player and board[4] == player and board[7] == player:
        return True

    if board[2] == player and board[5] == player and board[8] == player:
        return True

    if board[0] == player and board[4] == player and board[8] == player:
        return True
    
    if board[2] == player and board[4] == player and board[6] == player:
        return True

def generateKey(board):
    total = 0 
    for i in range(len(board)):
        baseThreeValue = powerOf3[i]
        decimalValue = board[i]*baseThreeValue
        total = total+decimalValue

    return total

def countWins(key, player):
    if not key in hashmap[player]:
        opp = 3-player

        if checkWin(board, player):
            hashmap[player][key] = 1
            hashmap[opp][key] = 0
            return
        
        if checkWin(board, opp):
            hashmap[opp][key] = 1
            hashmap[player][key] = 0
            return
    
        totalPlayer = 0
        totalOpp = 0
        for i in range(len(board)):
            if board[i] == 0:
                board[i] = player
                newKey = key + player*powerOf3[i]
                countWins(newKey, opp)
                val = hashmap[player][newKey]
                valOpp = hashmap[opp][newKey]
            
                totalPlayer = totalPlayer + val
                totalOpp = totalOpp + valOpp
                board[i] = 0

        hashmap[player][key] = totalPlayer
        hashmap[opp][key] = totalOpp



countWins(0,1)
num = int(input())

for i in range(num):
    inputBoard = input()
    convertedBoard = [0]*9
    for i in range(len(inputBoard)):
        if inputBoard[i] == "X":
            convertedBoard[i] = 1
        elif inputBoard[i] == ".":
            convertedBoard[i] = 0
        elif inputBoard[i] == "O":
            convertedBoard[i] = 2
    
    key = generateKey(convertedBoard)
  
    if not key in hashmap[1] and not key in hashmap[2]:
        print(-1,-1)
    else:
        print(hashmap[1][key], hashmap[2][key])
    