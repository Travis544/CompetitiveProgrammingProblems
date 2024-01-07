


def printAnswer(dp, length, weight, wts):
    res=[]
    temp=weight
    for i in reversed(range(length)):
        if i==0:
            if dp[0][temp]>0:
                res.append(0)
        if dp[i][temp]!=dp[i-1][temp]:
            res.append(i)
            temp=temp-wts[i]
    return res



result=[]
while True:
    val=input()
    if val=='' or val==None:
        break
    weight, length=list(map (int, val.split(' ')))
    wts=[]
    v=[]
    for i in range(length):
        item= list(map(int, input().split(' '))) 
        wts.append(item[1])
        v.append(item[0])
    dp=[]
    for i in range(length):
        dp.append([-1]*(weight+1))
    for i in range(length):
        for w in range(weight+1):
            if w>=wts[i]:
                chosenItemValue=v[i]
                other=0
                dontChose=0
                if i-1<=0:
                    dontChose=0
                    other=0
                else:
                    dontChose=dp[i-1][w]
                    other=dp[i-1][w-wts[i]]
                dp[i][w]=max(chosenItemValue+other, dontChose)
            else:
                if i==0:
                    dp[i][w]=0
                else: 
                    dp[i][w]=dp[i-1][w]
    result.append(printAnswer(dp, length,weight,wts))
    
    
for res in result: 
    print(len(res))
    print(*res)
            
