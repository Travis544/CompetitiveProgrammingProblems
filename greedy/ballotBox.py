

def determineBallot(cityPops, ballot):
    # ballot = ballot - len(cityPops)
    ballotGiven = []
    popPerBallot = []
 
    for i in range(len(cityPops)):
        if cityPops[i] > 0:
            ballot =  ballot -1
        ballotGiven.append(1)
        popPerBallot.append(cityPops[i])
   
    while(ballot>0):

        index = popPerBallot.index(max(popPerBallot))
        # print("INDEX")
        # print(index)
        # print(max(popPerBallot))
        num = cityPops[index]
        newBallotGiven  = ballotGiven[index]+1
        ballot = ballot - 1
        ballotGiven[index] = newBallotGiven
        newNum = None
        if num%newBallotGiven == 0: 
            newNum = num/newBallotGiven
        else:
            newNum = int(num/newBallotGiven)+1

        popPerBallot[index] = newNum
       
    # print(ballotGiven)
    return max(popPerBallot)


ans = []
while(True):
    cities, ballot = map(lambda x: int(x), input().split(" "))
    if cities == -1 and ballot == -1:
        break

    cityPops = []
    for i in range(cities):
        cityPop = int(input())
        cityPops.append(cityPop)
    
    blankLine = input()
    val = determineBallot(cityPops, ballot)
    ans.append(val)
    


for an in ans:
    print(int(an))





