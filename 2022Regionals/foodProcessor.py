
import math

def calculateTime(startSize, targetSize, rate):
    val = math.log2(startSize/targetSize)*rate
    if val < 0:
        raise Exception()

    return math.log(startSize/targetSize, 2)*rate
    

s, t, n = map(int, input().split(" "))


startChoices= []
bladeDict = dict()
blades = []
for i in range(n):
    maxPiece, rate =  map(int, input().split(" "))
    if t>= maxPiece:
        # if t== maxPiece:
        #     raise Exception()
        continue
    
    if maxPiece in bladeDict:
        if bladeDict[maxPiece] > rate:
            # raise Exception()
            bladeDict[maxPiece] = rate
    else:
        bladeDict[maxPiece] = rate
    
startingBladeMinRate =[None]
choice = None
for key in bladeDict: 
    maxPiece = key
    rate = bladeDict[key]
    if maxPiece >= s:
        if startingBladeMinRate[0] == None or rate<=startingBladeMinRate[0]:
            # if not startingBladeMinRate[0] == None:
            #     raise Exception()
            startingBladeMinRate[0] = rate
            choice = (maxPiece, rate)
    else:
        blades.append((maxPiece, rate))

if choice == None :
    print(-1)
else:
    blades.append(choice)
    blades.sort(reverse=True)

    bladesToSearch = [(blades[0][0], blades[0][1])]
    prevMin = blades[0][1]
    for i in range(1, len(blades)): 
        if prevMin <= blades[i][1]:
            continue
        else:
            bladesToSearch.append(blades[i])
            prevMin = blades[i][1]

    # print(bladesToSearch)

    def find():
        minTime = 0
        curS = s
        for i in range(0, len(bladesToSearch)):
            maxPiece, rate = bladesToSearch[i]
            # if maxPiece < curS:
            #     break

            if i+1 == len(bladesToSearch):
                minTime = minTime + calculateTime(curS, t, rate)
                
            else:
                maxPiece2, rate2 = bladesToSearch[i+1]
                minTime = minTime + calculateTime(curS, maxPiece2, rate)
                curS = maxPiece2

        
        c = int(minTime)
        if c == minTime:
            print(c)
        else:
            print(minTime)

    find()
    

# if len(startChoices==0):
#     print(-1)
# else:
#     minTime = 0
#     for i in range(len(startChoices)):
#         maxPiece, rate = startChoices[i]
#         for blade in blades:
#             maxPiece2, rate2 = blade
#             if rate2 >= rate:
#                 continue
#             else:
#                minTime=  minTime + calculateTime(s, maxPiece2, rate)
                



