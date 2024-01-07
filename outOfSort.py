n,m,a,c, x0= map(lambda x: int(x), input().split(" "))

sequence = []
def func(a, xPrev, c, m):
   return (a*xPrev+c)%m

def sequenceGenerator():
    prev = x0
    for i in range(n):
        calculation = func(a,prev, c, m)
        sequence.append(calculation)
        prev = calculation


def binarySearch(toSearch):
    left = 0 
    right = n-1
    # print(currHeight)
    # print(obstacles)
    # print("CHECKING")
    # print(toSearch)
    while(left<=right):
        midPoint = int((left+right)//2)
        
        # print(midPoint)
        if sequence[midPoint] == toSearch:
            return True
        elif sequence[midPoint] < toSearch:
            left = midPoint+1
        elif sequence[midPoint] > toSearch:
            right = midPoint-1

    return False


count = 0

sequenceGenerator()
# print(sequence)
for val in sequence:
    isFound = binarySearch(val)
    if isFound:
        count = count+1

print(count)