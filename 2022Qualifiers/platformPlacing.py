

def checkConstraint(yi, nextYi, xi, nextXi ):
    if (nextYi+yi)/2 <= nextXi-xi:
        return True
    else:
        return False


n, s, k  = list(map(lambda x: int(x), input().split(" ")))
points = []

answers = [s]*n
for i in range(n):
    p = int(input())
    points.append(p)

cannotSatisfy = False
points.sort()
for i in range(1, len(points)):
    if abs(points[i] - points[i-1]) < s:
    
        cannotSatisfy = True
        break


if cannotSatisfy:
    answers = [-1]


if not cannotSatisfy:

    for i in range(n):
        satisfy = True
        newAns = None
        while satisfy == True:
            for j in range(s, k+1):       
                if i > 0:
                    satisfy = checkConstraint(answers[i-1],j,points[i-1],points[i])
                
                if i<=n-2:
                    satisfy = satisfy and checkConstraint(j, answers[i+1], points[i],points[i+1])

                if satisfy == True:
                    newAns = j

                if satisfy == False:
                    break


            break
        
        if newAns:
            answers[i] = newAns


print(sum(answers))
    
    
