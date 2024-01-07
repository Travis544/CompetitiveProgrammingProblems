# Safe Passage
nums=list(map(int, input().split(" ")))
nums=nums[1:]

nums.sort()

def devisePlan(peopleLeft):
    if(len(peopleLeft)==2):
        return max(peopleLeft[0], peopleLeft[1])
    if(len(peopleLeft)==3):
        return sum(peopleLeft)
    a,b=peopleLeft[:2]
    x,y=peopleLeft[-2:]
    abCrossbBackxyCrossaBack=(2*b)+a+y
    axCrossaBackayCrossaBack=(x+a)+(y+a)
    return min(axCrossaBackayCrossaBack, abCrossbBackxyCrossaBack)+devisePlan(peopleLeft[:-2])


print(devisePlan(nums))