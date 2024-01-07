n, l, h = map(lambda x: int(x), input().split(" "))
profits = [0]
prefixSum = [0]*(n+1)
for i in range(n):
   num = int(input())
   profits.append(num)

for i in range(1, n+1):
    prefixSum[i] = prefixSum[i-1] + profits[i]


minCount = None
maxCount = None
#for each segment division
for i in range(l,h+1):

    # print("AT SEGMENT SIZE ", i)
    # for each starting day
    for j in range(0, i):

        # print("STARTING AT ", j)
        profitCount = 0 

        restSize = (n+1)-(j+1)

        startingProfit = prefixSum[j]
        if startingProfit > 0 :
            profitCount = profitCount + 1

        segmentLength = restSize//i
        # if (segmentLength == 0):
        #     continue
        # else:
        segmentIndex = j+1
        for k in range(0, segmentLength):
            # print("SEGMENT INDEX", segmentIndex)
            profit = prefixSum[segmentIndex+i-1] - prefixSum[segmentIndex-1]
            if profit> 0:
                profitCount = profitCount +1
            
            segmentIndex = segmentIndex+i
        
        if segmentIndex < n+1:
            profit = prefixSum[n] - prefixSum[segmentIndex-1]
            if profit> 0:
                profitCount = profitCount +1
        # print("SEGMENT INDEX", segmentIndex)ss
        if minCount == None or profitCount<minCount:
            minCount = profitCount

        if maxCount == None or profitCount>maxCount:
            maxCount = profitCount


print(minCount, maxCount)
            
            
    








