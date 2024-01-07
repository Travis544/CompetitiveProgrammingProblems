from queue import PriorityQueue




def huffmanTree(canvas):
    totalSum = 0
    q = PriorityQueue()
    for canva in canvas:
        q.put(canva)
    
    while not q.empty():
        # print("SS")
        first_lowest = q.get()
        if q.empty():
            return totalSum
        second_lowest = q.get()
        sum = first_lowest+second_lowest
        q.put(sum)
        totalSum = totalSum + sum
    
    return totalSum

ans = []
numTest = int(input())

for test in range(numTest):
    canvasNum = int(input())
    canvas= list(map(lambda x: int(x), input().split(" ")))
    res = huffmanTree(canvas)
    ans.append(res)

for an in ans:
    print(an)


   
        
