
class TubeState():
    def __init__(self, state, n, moves, moveCount ):
        self.state = state
        self.n = n
        self.moveCount = moveCount
        self.moves = moves
    

    

    def makeMove(self, take, add):
        index = n-1
        temp = "X"
        for c in reversed(range(0, n)):
            if not (self.state[take][c] == 0):
                temp = self.state[take][c]
                index = c
                break
            
        
        self.state[take][index] = 0
        # tupToList =  list(self.state[take])
        # tupToList[n-1] = 0
        # self.state[take] = tuple(tupToList)

        

        # tupToList =  list(self.state[add])
        # tupToList[n-1] = temp
        # self.state[add] =  tuple(tupToList)
        index = 0
        for c in self.state[add]:
            if c == 0:
                break
                
            index = index+1

        self.state[add][index] = temp
   
        self.moves.append([take+1, add+1])
        self.moveCount = self.moveCount+1
        
    def isColorState(self):
        # satisfy = 0
        for s in self.state:
            prev = s[0]
            for t in s:
                if not t == prev:
                    return False

                prev = t
                
        return True




    


n = int(input())
state = []
for i in range(n+1):
    b,m,t = map(int, input().split(" "))
    state.append([b,m,t])

initialTubeState = TubeState(state, n, [], 0 )
def findNeighbor(tubeState, visited):

 
    # print("FINDING NEIGHBOR FOR", tubeState.state)
    neighbors = []
    # for each tube
    for i in range(n+1):
        if tubeState.state[i][n-1] != 0:
            continue
        # for each 
        for j in range(n+1):
            
            if i == j or sum(tubeState.state[j]) == 0 :
                continue
            else:
                
                newTubeState = TubeState(list(map(list, tubeState.state)), n, list(map(list, tubeState.moves)), tubeState.moveCount)
                newTubeState.makeMove(j, i)
                # if str(tubeState.state) == "[[2, 2, 2], [1, 1, 1], [3, 0, 0], [3, 3, 0]]":
                #     print("XXXXXXXXXXXXXXXXXXXx", newTubeState.state)
                
                if newTubeState.moveCount > (20*n):
                    # print(newTubeState.moveCount)
                    # print("EXCEED MVOE COUNT")
                    
                    continue

                elif not str(newTubeState.state) in visited:
                    # 
                    # if str(tubeState.state) == "[[2, 2, 2], [1, 1, 1], [3, 0, 0], [3, 3, 0]]":
                    #     print("XXXXXXXXXXXXXXXXXXXx", newTubeState.state)
                    neighbors.append(newTubeState)
                    visited[str(newTubeState.state)] = True
                # else:
                #     if str(newTubeState.state) == "[[2, 2, 2], [1, 1, 1], [3, 0, 0], [3, 3, 0]]":
                #         print("ALREADY VISITED")
                #         print(newTubeState.state)
                #         print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx")
                        
    # print(visited)
    return neighbors

                
def bfs():
    visited = dict()
    stack = [initialTubeState]
    while len(stack) > 0:
       tubeState : TubeState =  stack.pop(0)
    #    print("CONSIDERING", tubeState.state)
    #    print("FOUND")
    #    print(tubeState.state)
       if tubeState.isColorState():
           print(len(tubeState.moves))
           for move in tubeState.moves:
               print(move[0],move[1])
           break
        #    return

       else:
           neighbors = findNeighbor(tubeState, visited)
        #    print("NEIGHBOR")
           for neighbor in neighbors:
                
                # if neighbor.state == "[[2, 2, 2], [1, 1, 1], [3, 0, 0], [3, 3, 0]]":
                #     print("FOUND")
                # print(neighbor.state)
                # print(neighbor.moves)
             
                stack.append(neighbor)
        #    print("______________________-")
            
# state, n, moves, moveCount 
# testTube = TubeState([[1,1,1], [0,0,0], [2,2,2], [3,3,3]], 3, [],0)
# print(testTube.isColorState())


# testTube = TubeState([[2,2,2], [1,1,1], [0,0,0], [3,3,3]], 3, [],0)
# print(testTube.isColorState())

bfs()

