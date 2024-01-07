from collections import deque

know, ask=list(map(int, input().split(" ")))
knowAngle=list(map(int,input().split(" ")))
poss=[False for _ in range(360)]

asks=list(map(int, input().split(" ")))

def populate():
    q=deque()
    for i in range(know):
        q.append(knowAngle[i])
    while len(q)>0:
        elem = q.pop()
        if poss[elem]:
            continue
        poss[elem]=True
        for val in knowAngle:
            sub=abs(elem-val)
            if not poss[sub]:
                q.append(sub)

            add=(elem+val)%360
            if not poss[add]:
                q.append(add)
                
populate()
for ask in asks:
    if poss[ask]:
        print("YES")
    else:
        print("NO")