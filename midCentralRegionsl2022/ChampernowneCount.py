n,k = map(int, input().split(" "))

currentRemainder = 1%k
count =0
if currentRemainder == 0:
    count = count+1

for i in range(2,n+1):
    converted = str(i)
    power = 10**len(converted)
    currentRemainder = (currentRemainder*power) + i
    
    currentRemainder = currentRemainder%k
    if currentRemainder == 0 :
        count = count + 1

print(count)
