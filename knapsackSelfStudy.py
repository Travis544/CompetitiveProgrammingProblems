

from operator import length_hint


def knapsack(itemWeights, itemValues, capacity):
    dp = []
    for _ in range(len(itemWeights)):
        forEachItemAndAfterDP = [-1]*(capacity+1)
        forEachItemAndAfterDP[0] = 0
        dp.append(forEachItemAndAfterDP) 
        print(dp)
    def findKnapsack(currentItem, capacity):
        if currentItem == -1:
            return 0

        print(capacity)
        if (dp[currentItem][capacity] > -1):
            return dp[currentItem][capacity]
        else:
            dontTake = findKnapsack(currentItem-1, capacity)
            if capacity >= itemWeights[currentItem]:
                take = findKnapsack(currentItem-1, capacity-itemWeights[currentItem]) + itemValues[currentItem]
                maxVal = max(take, dontTake)
                dp[currentItem][capacity] = maxVal
                return maxVal
            else:
                dp[currentItem][capacity] = dontTake
                return dontTake

    def findItems(length, maxCapacity):
        items = []
        currentCapacity = maxCapacity
        for i in reversed(range(length)):
            if i == 0:
                if dp[i][currentCapacity] > 0:
                    items.append(0)
            elif (dp[i][currentCapacity] != dp[i-1][currentCapacity]):
                items.append(i)
                currentCapacity = currentCapacity - itemWeights[i]
        return items

    findKnapsack(len(itemValues)-1, capacity)
    return findItems(len(itemValues), capacity)


     

# capacity = 5
# itemWeights = [5, 5, 5]
# itemValues = [1, 10 , 100]
# print(knapsack(itemWeights, itemValues, capacity))


capacity = 6
itemWeights = [4, 3 ,2, 1]
itemValues = [5, 4 , 3, 2]
print(knapsack(itemWeights, itemValues, capacity))


