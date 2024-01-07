t=int(input())
dp={}
dp[0]=1
dp[1]=2
dp[2]=3

def findNumberOfBinaryWithNo11(n):
    if n in dp:
        return dp[n]
    else:
       dp[n]=findNumberOfBinaryWithNo11(n-1)+findNumberOfBinaryWithNo11(n-2)
       return dp[n]


for i in range(t):
    num=int(input())
    print(findNumberOfBinaryWithNo11(num)%((10**9)+7))
    


