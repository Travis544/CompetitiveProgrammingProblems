n, k = (lambda x: int(x), input().split(" "))

knowHowToConstruct = list(map(lambda x: int(x), input().split(" ")))
query = list(map(lambda x: int(x),input().split()))

dp=[0]*361
dp[360] = 1


for angle in knowHowToConstruct:
    # start = 0 
    # end = 360
    dp[angle] = 1
    for i in range(len(dp)):
        if dp[i] == 1:
           res = (i + angle)%360
           dp[res] = 1

    
for q in query:
    if dp[q] == 1:
        print("YES")
    else:
        print("NO")



    
    
        
        


    # while(end > 0):
    #    res = end - angle
    #    dp[res] = 1
    
    # while(start <= 360):
    #     start = start+angle

    