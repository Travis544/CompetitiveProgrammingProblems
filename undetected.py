




def doesIntersect(circle1, circle2):
    # bigX,smallX,bigY,smallY=None, None,None,None
    # if circle1[0]>=circle2[0]:
    #     bigX=circle1
    #     smallX=circle2
    # elif circle1[0]<circle2[0]:
    #     bigX=circle2
    #     smallX=circle1
        
    # if circle1[1]>=circle2[1]:
    #     bigY=circle1
    #     smallY=circle2
    # elif circle1[1]<circle2[1]:
    #     bigY=circle2
    #     smallY=circle1
    
    # hIntersect=False
    # YIntersect=False
    # if (smallX[0]+smallX[2])>=(bigX[0]-bigX[2]):
    #     hIntersect=True
    # if (smallY[0]+smallY[2])>=(bigY[0]-bigY[2]):
    #     YIntersect=True
    
    center_dist = ((circle1[0] - circle2[0]) ** 2 + (circle1[1]- circle2[1]) ** 2) ** 0.5
    return center_dist <= circle1[2] + circle2[2]
        
    # return hIntersect and YIntersect
       
def coverWholeField(intersections):
    minX=200
    maxX=0
    for intersection in intersections: 
        if intersection[0]<minX:
            minX= intersection[0]
        
        if intersection[1]>maxX:
            maxX= intersection[1]
    
    #print( max(0,minX), min(200, maxX),)
    if min(200, maxX)-max(0,minX)==200:
        return True
    else:
        return False
    

circles=[]
num=int(input())
isDone=False
# print(doesIntersect((36,228,58), (88,170,42)))
for i in range(num):
    circle=tuple(map(int, input().split(" ")))
  
    if not isDone:
        toCheck=[]
        toCheck.append(circle)
    # print(circle)
        #print(circles)
        matchCount=1
        
        while matchCount>0:
            matched=[]
            for c in circles:
                if not c in toCheck:
                    for check in toCheck:
                        if doesIntersect(c, check):
                            matched.append(c)
                            break
            toCheck=toCheck+matched
            matchCount=len(matched)
                    
        horizontalDistances=[]
        for ch in toCheck:
            horizontalDistances.append((ch[0]-ch[2], ch[0]+ch[2]))
        #print(toCheck)
        
        if coverWholeField(horizontalDistances):
            print(len(circles))
            isDone=True
        else:
            circles.append(circle)
        
        
