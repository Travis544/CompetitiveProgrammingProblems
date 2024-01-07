pairNum = int(input())
row1 = list(map(lambda x: int(x), input().split(" ")))
row2 = list(map(lambda x: int(x), input().split(" ")))


freqDict = dict()
allRow = row1+row2
for val in row1:
    if val in freqDict:
        freqDict[val] = freqDict[val]+1
    else:
        freqDict[val]  = 1

optimizedStart = 0
for key in freqDict:
    if freqDict[key] == 1:
        optimizedStart = max(optimizedStart, key)

# row1 = list(filter(lambda x: x>optimizedStart, row1))
# row2 = list(filter(lambda x: x>optimizedStart, row2))
# searchSpace = list(set(allRow))

row1Length = len(row1)
row2Length = len(row2)
def checkAllPairMatch(m):
 
    isPairedRow1 = checkIfPaired(m,row1, row1Length)
    isPairedRow2 = checkIfPaired(m,row2, row2Length)
    return isPairedRow1 and isPairedRow2


def checkIfPaired(m,row, length):
    target = -1
  
    for i in range(0, length):
        if row[i]<=m:
            continue
        elif target == -1:
            target= row[i]
            continue
        
        elif not target == row[i]:
            return False
        else:
            target = -1
      
    if not target == -1:
        return False

    return True



# Searching by all possible weight value so you don't have to sort it!!!!!
def binarySearch():
    left = optimizedStart
    right = 10**9
    while left<=right:
        midPoint = (left+right)//2
        
        allPairMatch = checkAllPairMatch(midPoint)
        if allPairMatch:
            right = midPoint-1
        else: 
            left = midPoint+1

    return left

maxWeight = binarySearch()
print(maxWeight)