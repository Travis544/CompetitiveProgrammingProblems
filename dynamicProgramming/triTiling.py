


def solve(n):
    dp = []
    for i in range(n+1):
       arr= [0]*8 
       dp.append(arr)

    dp[0][7] = 1
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][7]

        dp[i][1] += dp[i-1][6]
        dp[i][2] += dp[i-1][5]
        dp[i][3] += dp[i-1][7] 
        dp[i][3] += dp[i-1][4]
        dp[i][4] += dp[i-1][3]

        dp[i][5] += dp[i-1][2]
        dp[i][6] += dp[i-1][7]
        dp[i][6] += dp[i-1][1]

        dp[i][7] += dp[i-1][3]
        dp[i][7] += dp[i-1][6]
        dp[i][7] += dp[i-1][0]

    return dp[n][7]




answers = []
while(True):
   n = int(input())
   if not n == -1:
        res = solve(n)
        answers.append(res)
   else:
        break

for ans in answers:
    print(ans)