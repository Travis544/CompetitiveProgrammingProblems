
length=input()
length=int(length)
coordinates=[list(map(int, input().split(' '))) for i in range(length)]
count=0
STEPS = [
        (-2018,0),
        (-1680,-1118),
        (-1680,1118),
        (-1118,-1680),
        (-1118,1680),
        (0,-2018),
        (0,2018),
        (1118,-1680),
        (1118,1680),
        (1680,-1118),
        (1680,1118),
        (2018,0)
    ]

points=set()
counter=0
for i in range(len(coordinates)):
    x=coordinates[i][0]
    y=coordinates[i][1]
    for j in range(len(STEPS)):
        a,b=STEPS[j]
        if (x+a, y+b) in points:
            counter+=1
    points.add((x,y))
    
print(counter)