r,s,k = list(map(lambda x: int(x), input().split(" ")))
window = []
for i in range(r):
    arr = input()
    window.append(list(arr))



vEnd = r-k
hEnd = s-k

def countFlies(i, j):
    total = 0
    for u in range(i+1, i+k-1):
        for p in range(j+1, j+k-1):
           
            if window[u][p]=="*":
                total = total + 1

    return total

maxFlies = None
row = None
column = None


for i in range(0, vEnd+1):
    for j in range(0, hEnd+1):
        flies = countFlies(i, j)
      
        if maxFlies == None or flies>maxFlies:
            maxFlies = flies
            row = i
            column = j



for i in range(row, row+k):
    for j in range(column, column+k):

        if (i == row and j == column) or (i == row and j == column+k-1) or  (i == row+k-1 and j == column+k-1) or  (i == row+k-1 and j == column):
            window[i][j] = "+"
        elif (i == row or i==row+k-1):
            window[i][j] = "-"
        elif (j==column or j==column+k-1):
            window[i][j] = "|"

print(maxFlies)
for row in window:
    print("".join(row))

