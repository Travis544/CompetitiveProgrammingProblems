

opp={
 "H":"V",
 "V":"H"   
}


def cut(whoStart, toCut):
    result=[]
    half= 0
    constant=0
    other=0
    if whoStart=="H":
        constant=toCut[0]
        half=toCut[1]//2
        other=toCut[1]-half
        result.append((constant, half))
        result.append((constant, other))
    else:
        constant=toCut[1]
        half=toCut[0]//2
        other=toCut[0]-half
        result.append(( half, constant))
        result.append(( other, constant,))

    return result

# a piece: (breath by depth)
def cutBrownies( pieces, whoStart, count):
   
    toCheck=[]
    # print("-------------")
    # print("For "+whoStart)
    # print("Pieces")
    # print(pieces)
    # print("-------------")
    for piece in pieces:
        
        if piece[0]==2 and piece[1]==2:
           # winners.append(opp[whoStart])
           continue
        elif piece[1]==1 and whoStart=="H":
            continue
        elif piece[0]==1 and whoStart=="V":
            continue
        else:
            toCheck.append(piece)
   
    if len(toCheck)==0:
        return opp[whoStart]
    else:
        count=count+1
        possible=[]
        visited=[]
        #for i in range(len(toCheck)):
        put=[]
        for j in range(len(pieces)):
                if pieces[j]==toCheck[0]:
                    put=put+cut(whoStart, pieces[j])
                    put=put+pieces[j+1:]
                    if count<10:
                        if not put in visited:
                            possible.append(cutBrownies(put, opp[whoStart],count))
                            visited.append(put)
                            #print(put)
                    break
                else:
                    put.append(pieces[j])
                
        #print(whoStart)
        for pos in possible:
            if pos==whoStart:
                return whoStart
        
        return opp[whoStart]
    
#print(cutBrownies([(3,2)], "V" ,0))

num=int(input())
for i in range(num):
    compete=input().split(" ")
    if int(compete[0])<=0 or int(compete[1])<=0:
        print(compete[2]+" cannot win")
    else:
        res=cutBrownies([(int(compete[0]),int(compete[1]))], compete[2][0] ,0)
        if res!=compete[2][0]:
            print(compete[2]+" cannot win")
        else:
            print(compete[2]+" can win")