num=int(input())
vectors=[]
for i in range(num):
    vector=tuple(map(int, input().split(" ")))
    vectors.append(vector)
    
    

count=0

# res=[]
# def findZeros(currentTotal, vectors):
#     if len(vectors)==0:
#         return
#     if currentTotal==None:
#         for i in range(len(vectors)):
#             for j in range(len(vectors)):
#                 if i!=j:
#                     sum=(vectors[i][0]+vectors[j][0], vectors[i][1]+vectors[j][1])
#                     if sum[0]==0 and sum[1]==0:
#                         res.append(sum)
#                     newV=[]
#                     for k in range(len(vectors)):
#                         if(k!=j and k!=i):
#                             newV.append(vectors[k])
            
#                     findZeros(sum, newV)        
#     else:
#         for i in range(len(vectors)):
#             sum=(currentTotal[0]+vectors[i][0], currentTotal[1]+vectors[i][1])
#             newV= vectors.copy()
#             newV.pop(i)
#             if sum[0]==0 and sum[1]==0:
#                 res.append(sum)
#             findZeros(sum, newV)


from itertools import chain, combinations

def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

dp=dict()
def addUp(current):
    sum=current[0][0]
    sum2=current[0][1]
    if tuple(current[:-1]) in dp:
           sum,sum2= dp[tuple(current[:-1])]
           return (sum+current[-1][0], sum+current[-1][1])
    else:
        for c in current[1:]:
            sum=sum+c[0]
            sum2=sum2+c[1]
        dp[tuple(current)]=(sum,sum2)
    return (sum, sum2)
        
        

def findZeros():
    count=0   
    powerse=list(powerset(vectors))
    for current in  powerse:
        if len(current)>0:
            s=addUp(current)
            if s[0]==0 and s[1]==0:
                count=count+1
    return count    

print(findZeros())
