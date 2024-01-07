    
# Recurrence relation: 
# let f(i) be the length of the longest subsequence from element with indices 0 to i
# f(i) = 0<=j<i if arr[j]<arr[i], max(f(j)+1)
def longestIncreasingSubSeq(sequence):
    dp=[]
    for i in range(len(sequence)):
        temp=[]
        temp.append(sequence[i])
        dp.append([1,temp] )
    
    for i in range(1, len(sequence)):
        for j in range(0, i):
            if int(sequence[i])>int(sequence[j]):
                if int(dp[j][0])+1>= dp[i][0]:
                    dp[i][0]=dp[j][0]+1
                    temp=dp[j][1].copy()
                    temp.append(sequence[i])
                    dp[i][1]=temp
    return dp


globalMax=0
sequences=[]

sequences=[]
while True:
    val=input()
    if val=="0":
        break
    sequences.append(val) 

for sequence in sequences:
    sequence=sequence.split(" ")
    n=sequence 
    sequence=sequence[1:]
    res=longestIncreasingSubSeq(sequence)
    max=0
    seq=None
    for i in range(len(res)):
        if res[i][0]>max:
            max=res[i][0]
            seq=res[i][1]
    possibleMax=[]
    possibleMax.append(seq)
    for i in range(len(res)):
        if res[i][0]==max:
            seq=res[i][1]
            possibleMax.append(seq)
    index=0
    min=None
    for i in range(len(possibleMax)):
        if min is None or possibleMax[i][len(possibleMax[i])-1]<min:
            min=possibleMax[i][len(possibleMax[i])-1]
            index=i

    seq.insert(0,str(len(seq)) )
        
    print(' '.join(seq)) 