



val=str(input())
length=len(val)
lq=int(input())

# create suffix array
suffixArr=[-1]*(length)
def createSuffixArray(string, index):
    if string=="" or index>len(suffixArr):
        return 
    suffixArr[index]=string
    t=index+1
    createSuffixArray(string[1:],t )
    


LCP={}
def findLCP(first, second):
        prev=suffixArr[first]
        curr=suffixArr[second]
        match=0
        for j in range(len(curr)):
            if j==len(prev):
                break
            if prev[j]==curr[j]:
                match+=1
            else:
                break
        LCP[(first, second)]=match


createSuffixArray(val, 0)

# print(suffixArr)
for i in range(lq):
    
    start,end=list(map(int, input().split(" ")))
    if not (start>len(val) or end>len(val) or start>end):
        if len(suffixArr)!=0:
                
            findLCP(start, end)
            print(LCP[(start, end)])


