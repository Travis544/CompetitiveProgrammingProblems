
width,height = map(lambda x: int(x), input().split(" "))
obstacleBot = []
obstacleTop = []

for i in range(width):
    obstacle = int(input())
    if i%2 == 0:
        obstacleBot.append(obstacle)
    elif i%2 == 1:
        obstacleTop.append(obstacle)


obstacleBot.sort()
obstacleTop.sort()

def binarySearch(currHeight, obstacles):
    left = 0 
    right = width//2
    # print(currHeight)
    # print(obstacles)
    while(left<right):
        midPoint = int((left+right)//2)
        if obstacles[midPoint] < currHeight:
            left = midPoint+1
        else:
            right = midPoint

    return width//2-left



# answers = []
# length = len(obstacles)
minObstacles = float("inf")
count = 0
for i in range(1, height+1):
    answerBot = binarySearch(i, obstacleBot)
    answerTop = binarySearch(height-i+1, obstacleTop)
    answer = answerTop+answerBot
    if answer < minObstacles:
        count = 1
        minObstacles = answer
    elif answer == minObstacles:
       count = count+1


print(minObstacles, count)





    

