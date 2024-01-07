import math
class SparseTable:
    def __init__(self, arr, func, isOverlapFriendly, isMin, isMax): 
        self.n =len(arr)
        self.func = func
        self.isOverlapFriendly = isOverlapFriendly
        self.isMin = isMin
        self.isMax = isMax
        #Maximum power of 2 needed: floor(log2(n))
        self.P = math.floor(math.log(self.n)/math.log(2))
        self.dp = []
        #Index table, index associated with value in sparse table.
        self.it = []
        for _ in range(self.P+1):
            row = []
            row2= []
            for i in range(self.n):
                row.append(0)
                row2.append(0)
            self.dp.append(row)
            self.it.append(row2)

        for i in range(self.n):
            self.dp[0][i]= arr[i]
            self.it[0][i] = i
        

        # Fast base2 log lookup table. i =2, tell you what log2(2) is
        self.log2 = [0]*(self.n+1)
        for i in range(2, self.n+1):
            self.log2[i] = self.log2[i//2] +1
      
        self.buildSparseTable()

    # build min sparse table, but we can change min to something else as well.
    def buildSparseTable(self):
        for p in range(1, self.P+1):
            for j in range(0,self.n):
                #<< is left shift, essentially calculating 1 multiple by 2 j times.
                jPlus2ToThePthPower = j+(1<<p)
                if jPlus2ToThePthPower > self.n:
                    break
                #split the current i,j cell representing [j,j+2^i] to [j, j+2^(i-1), j+2^(i-1), j+2^i]
                jPlus2ToThePthMinusOnePower =j+(1<<(p-1))
                leftInterval = self.dp[p-1][j]
                rightInterval = self.dp[p-1][jPlus2ToThePthMinusOnePower]
                self.dp[p][j] = self.func(leftInterval, rightInterval)

                # Update index table, only useful for min and max range query table
                if(self.isOverlapFriendly):
                    update = self.determineUpdate(leftInterval, rightInterval)
                    if (update):
                        self.it[p][j] = self.it[p-1][j]
                    else:
                        self.it[p][j] = self.it[p-1][jPlus2ToThePthMinusOnePower]

        

    def determineUpdate(self, leftInterval, rightInterval):
        if self.isMin:
            return leftInterval<=rightInterval
        elif self.isMax:
            return leftInterval>= rightInterval

    def queryOverlapFriendly(self,left, right):
        length = right - left + 1
        p = self.log2[length]
        # 2^p
        k = 1<<p
        return self.func(self.dp[p][left], self.dp[p][right-k+1])

    #only for overlap friendly function
    def queryIndex(self, left, right):
        length = right - left + 1
        p = self.log2[length]
        # 2^p
        k = 1<<p
        leftInterval = self.dp[p][left]
        rightInterval = self.dp[p][right-k+1]
        update = self.determineUpdate(leftInterval, rightInterval)
        if update:
            return self.it[p][left]
        else:
            return self.it[p][right-k+1]

 
    # divide query range into discrete ranges of powers of 2.
    def queryNonOverlapFriendly(self,left, right):
        curr = None
        while left<=right:
            length = right - left + 1
            p = self.log2[length]
            if curr == None:
                curr = self.dp[p][left]
            else:
                curr = self.func(curr, self.dp[p][left])
            left = left+ (1<<p)
        return curr


        

n, d = list(map(lambda x: int(x), input().split(" ")))

def round(a):
    last = a%10
    multiplier = 10
    # if length>1:
    #     multiplier = 10
    if last>=5:
        return a+(10-last)
    else:
        return a-last

prices = list(map(lambda x: int(x),  input().split(" ")))
prices.insert(0,0)
# print(prices)
def func(a,b):
    return a+b

sumSparseTable = SparseTable(prices, func , False, False, False )

dp = []
for i in range(n+1):
    row = []
    for j in range(d+1):
        if  i ==0 :
            row.append(0)
        else:
            row.append(None)
    dp.append(row)

for i in range(n+1):
   dp[i][0]= round(sumSparseTable.queryNonOverlapFriendly(0,i))


prefixSum = [0]*(n+1)
prefixSum[0]= prices[0]
for i in range(1,n+1):
    prefixSum[i]=prefixSum[i-1]+prices[i]

#Iteratively build dp table
for i in range(1, n+1):
    #For each number of divider
    for j in range(1, d+1):
        minimum = None
        # for k in range(1, i+1):

        dp[i-1][j-1]
        for k in range(0,i):
            # print(i-k+1, i)
            # sumOfRest = sumSparseTable.queryNonOverlapFriendly(k+1, i)
            sumOfRest = prefixSum[i]-prefixSum[k+1-1]
            # sumOfRest = round(sumOfRest)
          
            # print(k,j)
            minAtThatPoint =dp[k][j-1]
            total = round(sumOfRest+minAtThatPoint)
            # print("______________________--")
            # print(sumOfRest)
            # print(minAtThatPoint)
            # print(total)
            # print(total)
            # print(minAtThatPoint)
            if minimum == None or total<minimum:
                minimum = total
        # print("____")
        # print(minimum)
        # print(i,j)
        dp[i][j] = minimum
        # print(dp)



# print(dp)
minimum = None
for i in range(d+1):
    val = round(dp[n][i])
    if minimum == None:
        minimum = val
    elif val < minimum:
        minimum = val
        
print(minimum)