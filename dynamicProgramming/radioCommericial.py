n, cost = list(map(lambda x: int(x), input().split(" ")))

commercials = list(map(lambda x: int(x), input().split(" ")))

transformed = []
for comm in commercials:
   res = comm - cost
   transformed.append(res)


# dp = dict()

currMax = transformed[0]
currSum = transformed[0]
for i in range(1, len(transformed)):
    currSum = max(currSum + transformed[i], transformed[i])

    currMax= max(currSum, currMax)

print(currMax)



