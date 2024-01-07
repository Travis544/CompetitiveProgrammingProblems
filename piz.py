from imghdr import what
import math
n=int(input())
res=[]
for i in range(n):
    val=input()
    val=list(map(int, val.split(" ")))
    res.append(val)


for i in range(len(res)):
    seq = []
    angle=res[i][2]+(res[i][3])/60+(res[i][4])/3600
    n=res[i][1]
    print(str(n)+" SS")
    # print(angle)
    for k in range(n):
        
        while k * angle >= 360:
            angle=(k * angle) - 360
        seq += [k * angle]
        
    whatIsLeft=0
    if (n-1)*angle<360:
        whatIsLeft=(360-((n-1)*angle))
        
    seq.sort()
    print(seq)
    
    biggest_difference = 0
    for j in range(len(seq) - 1):
        if biggest_difference <= seq[j + 1] - seq[j]:
            biggest_difference = seq[j + 1] - seq[j]
    print(str(biggest_difference)+" sss")
    
    value=max(biggest_difference, whatIsLeft)
    print(str(value)+" value")
    # print(str(value)+"sfaf")
    print(res[i][0] ** 2 * math.pi *(value/360))
