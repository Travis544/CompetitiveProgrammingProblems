from collections import deque

class Chain:
    def __init__(self, string, total, length):
        self.string = string
        self.total = total
        self.length=length


def main():
    numAndWeight=input().split(" ")
    n=int(numAndWeight[0])
    weight=int(numAndWeight[1])
    alphabet=dict()
    for i in range(26):
        curLetter=97+i
        alphabet[chr(curLetter)]=i+1
    if 26*n<weight:
        print("impossible")
    else:
        res=dfs(n, weight, alphabet)
        if res:
            print(res.string)
        else:
             print("impossible")

def dfs(n, weight, alphabet):
    stack = deque([])
    for key in alphabet:
        stack.append(Chain(key, alphabet[key], 1 ))

    while len(stack)>0:
        c=stack.pop()
        if c.total==weight and c.length==n:
            return c

        elif c.total<weight:
            for key in alphabet:
                newValue=c.total+alphabet[key]
                newString=c.string+key
                newLength=c.length+1
                if newValue<weight and newLength<n:
                    newChain=Chain(newString, newValue, newLength)
                    stack.append(newChain)
                elif newValue==weight and newLength==n:
                    return Chain(newString, newValue, newLength)


    

   


if __name__ == "__main__":
    main()