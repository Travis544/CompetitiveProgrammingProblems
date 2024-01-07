
#WALRUS WEIGHTS

nWeights = int(input())
weights = []
for i in range(nWeights):
    weight = int(input())
    weights.append(weight)

cache = [0]*2001
def dp():
    # for w in weights:
    #     cache[w] = 1  
    for w in weights:
        for i in reversed(range(len(cache))):
            if cache[i] == 1:
                sum = w + i
             
                if sum<=2000:
                    cache[sum] = 1

        cache[w] = 1
    
dp()


closetToThousandOver = None
closetToThousandUnder = None
for i in range(1000, len(cache)):
    if cache[i] == 1:
       closetToThousandOver = i
       break

for i in reversed(range(0, 1001)):
    if cache[i] == 1:
       closetToThousandUnder = i
       break



if closetToThousandOver is None:
    print(closetToThousandUnder)
elif closetToThousandUnder is None:
    print(closetToThousandOver)
else:
    diff = abs(1000- closetToThousandOver)
    diffTwo = abs(1000- closetToThousandUnder)

    if diff > diffTwo: 
        print(closetToThousandUnder)
    elif diff<= diffTwo:
        print(closetToThousandOver)

