
#define base cases
alphabet = "abcdefghijklmnopqrstuvwxyz"
string = input()

dp = []
for i in range(len(alphabet)+1):
    arr = []
    for j in range(len(string)+1):
        arr.append(0)
    dp.append(arr)


# print(len(alphabet))
# print(len(string))
# print(len(dp[0]))

for i in range(len(alphabet)+1):
    dp[i][0] = 0 

for j in range(len(string)+1):
    dp[0][j]  = 0


    
for i in range(1,len(alphabet)+1):
    arr = []
    for j in range(1,len(string)+1):
        if alphabet[i-1] == string[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 

print(len(alphabet)-dp[len(alphabet)][len(string)])
