import queue

rows, columns = list(map(lambda x: int(x), input().split(" ")))
maze = []
entrances = []
dotCounts = 0

for i in range(rows):
    c = list(input())
    maze.append(c)
    # for cell in c:
    
    # if i == 0 or i == rows-1:
        # search for entrance
    for cIndex in range(len(c)):
        if c[cIndex] == ".":
            dotCounts = dotCounts+1

        if not c[cIndex] == "X" and not c[cIndex] == "." and not c[cIndex] == " ":
            entrances.append((i, cIndex))


def checkBound(i, j, visited):
    if (i, j) in visited:
        return False

    if i >= 0 and i <= rows-1 and j >= 0 and j <= columns-1:
        if not maze[i][j] == "." and not maze[i][j] == " ":
            return False
        if maze[i][j] == ".":
            visited[(i, j)] = True
        elif maze[i][j] == " ":
            visited[(i, j)] = False

        return True
    else:
        return False

visited = dict()


def bfs(entrance):
    q = queue.Queue()
    q.put(entrance)
   
    visited[(entrance[0], entrance[1])] = False
    dotEaten = 0
    while not q.empty():
        i, j = q.get()
        if checkBound(i+1, j, visited):
            toAdd = (i+1, j)
            q.put(toAdd)

        if checkBound(i-1, j, visited):
            toAdd = (i-1, j)
            q.put(toAdd)

        if checkBound(i, j-1, visited):
            toAdd = (i, j-1)
            q.put(toAdd)

        if checkBound(i, j+1, visited):
            toAdd = (i, j+1)
            q.put(toAdd)

        if maze[i][j] == ".":
            dotEaten = dotEaten + 1


    return dotEaten






# dotEatenForAll = []
# visitedForAll = []
minimum = 0
totalDotsVisited = 0 
for entrance in entrances:
    dotEaten = bfs(entrance)

    if dotEaten>0:
        minimum = minimum +1
        totalDotsVisited = totalDotsVisited+ dotEaten
    # dotEatenForAll.append(dotEaten)
    # visitedForAll.append(visited)
print(minimum, dotCounts - totalDotsVisited)



