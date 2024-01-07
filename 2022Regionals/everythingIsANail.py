n = int(input())
tasks = []

for i in range(n):
    task = int(input())
    tasks.append(task)

def translate(num):
    if num == 0:
        return []
    if num == 1:
        return [0]
    if num == 2:
        return [1]
    if num == 3:
        return [2]
    if num == 4:
        return [0,1]
    if num == 5:
        return [0,2]
    if num == 6:
        return [1,2]
    if num == 7:
        return [0,1,2]
    
def inverseTranslate(key):
    d = {
        (): 0,
        (0,): 1,
        (1,): 2,
        (2,): 3,
        (0,1):4,
        (0,2):5,
        (1,2):6,
        (0,1,2):7
    }

    return d[key]



dp = []

for i in range(n+1):
    dp.append([])
    for j in range(0,8):
        dp[i].append([0]*3)
        # for k in range(0,3):
        # dp[i][j].append([0]*3)
        


# print(dp)
    
for i in range(1, n+1):
    for j in range(1, 8):
        for k in range(0, 3):
            curTool = tasks[i-1]
            toAdd = 0
            toCheck = []
            availableTools = translate(j)
            #cannot have current k as the last used tool, look at previous one.
            if not k in availableTools or not curTool in availableTools:
                
                dp[i][j][k] = dp[i-1][j][k]
                continue


#             print(k, availableTools, curTool )
# # 
            #can take current task
            # if (curTool == k):
            #     toAdd = 1
            
            # useCurTaskAndPrevSame = dp[i-1][j][k]+toAdd
            #
            # We know k is in available tools. 
            # print("_______________________________")
            # for t in availableTools:
            #     #go through list of tool.
            #     curr = dp[i-1][j][t]
            #     if t == k:
            #         if t == curTool:
            #             print("ADDING by consecutive")
            #             curr =  curr + 1
            #     print("USING", i-1, j,t)
            #     toCheck.append(curr)

            curr = dp[i-1][j][k]
            #skipping tool is controlled by k, if hold a different tool than the current tool, then we don't add one.
            if k == curTool:
                # print("ADDING by consecutive")
                curr =  curr + 1

            toCheck.append(curr)


            #Use current tool but drop previous tool.
            if k==curTool:

                for t in availableTools:
                    if t == k:
                        continue
                    arr = translate(j)
                    arr.remove(k)
                    num = inverseTranslate(tuple(arr))
                    # print("ADDING by dropping prev")
                    curr = dp[i-1][num][t]+1
                    toCheck.append(curr)

            # print("MAX AT", i, "WITH AVAILABLE TOOLS", j, "WITH PREVIOUS TOOL", k)
            # print(max(toCheck))
            dp[i][j][k] = max(toCheck)


print(max(dp[n][7]))