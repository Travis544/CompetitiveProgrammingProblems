# rotations = []

# def rotateString(string, rotationCount, length):
#     if rotationCount == length-1:
#         return False
#     else:
#         toAdd = string[1:length] + string[0]
#         rotations.append(toAdd)
#         rotateString(toAdd, rotationCount+1, length)

# def cyclicSubstring(t):
#     for rotation in rotations:
#         if t in rotation:
#             return True
#         else:
#             return False

def cyclicSubstring(t, string, rotationCount, length):
    if t in string+string:
        return True
    else:
        return False
    # if rotationCount == length:
    #     return False
    # else:
       
    #     if t in string:
    #         return True
    #     newString = string[1:length] + string[0]
    #     return cyclicSubstring(t, newString, rotationCount+1, length)



cache = dict()

def internalReverseCyclic(start, actualString, actualLength, length):
    if length == 0:
        return True

    for i in range(start+2, actualLength+1):
        substring = actualString[start:i]
        substring = substring[::-1]
     
        if substring in cache:
            res = cache[substring]
            if not res:
                return False
            elif res:
                continue

        isCyclicSubstring = cyclicSubstring(substring, actualString, 0, actualLength )
        cache[substring] = isCyclicSubstring
        if not isCyclicSubstring:
            return False
    
    return internalReverseCyclic(start+1,actualString, actualLength, length-1)


string = input()
# rotations.append(string)
length = len(string)
# rotateString(string, 0 , length)
res= internalReverseCyclic(0, string, length, length )
if res:
    print(1)
else:
    print(0)

