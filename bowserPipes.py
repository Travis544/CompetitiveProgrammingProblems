#bowser's pipes
from collections import deque
n=int(input())
pipes=[int(i) for i in input().split()]
group=[0]*n
# create a range array of arrays of length n
children = [[] for _ in range(n)]
rootcount = 0
for i in range(n):
    pipe = pipes[i]
    # if the current pipe i does not lead to a coin room, but another pipe.
    if (pipe != -1):
        # save pipe that lead to the other pipe as the children of the pipe that was lead to. 
        # pipe lead to: parent
        # pipe i(current pipe): children
        children[pipe].append(i)
    else:
        # if the pipe i leads to a coin room, it is a root so add the rootcount, save the root count, which root is this.  
        rootcount += 1
        group[i] = rootcount
# length should be total number of root count?
bestdrops = [None] * (rootcount + 1)
visited = [False] * n

for i in range(n): 
    if visited[i] or group[i] == 0:
        continue
    bfs = deque([])
    bfs.append((0, i))
    visited[i] = True
    bestdrop = (n, n)
    # general idea: start from root, do bfs to the parents, while keeping track of the min parent with the lowest depth and pipe index. 
    while len(bfs) > 0:
        # print(bfs)
        # delete from left of queue.
        # depth and the pipe number
        d, u = bfs.popleft()
        
        # if this has no parent, it is the top node, update bestdrop. oh i see---we can only enter pipes with no other pipes that lead to it
        # if a "pipe" has another pipe leading to it, it is not a pipe, it it a warp which we cannot directly enter.
        if len(children[u]) == 0:
            bestdrop = min(bestdrop, ( d, u ))
            # print(bestdrop)
        # for each parent this current pipe has, it not visited, 
        for c in children[u]:
            if not visited[c]:
                #looks complicated...what this is really saying is,indicate that this parent can leads to this root. We use this for output. 
                group[c] = group[i]
                visited[c] = True
                # add into bfs, increase depth we need since we are moving up. 
                bfs.append(( d + 1, c ))
    # after finish searching, set the index of the root node that we want to find the best pipe for, to the best we found.
    bestdrops[group[i]] = bestdrop[1]
q = int(input())
S = [int(i) for i in input().split()]
for i in range(q):
    # pipes mario tell luigi to enter
    s = S[i]
    # access group array to find which root we want(we know pipe leads which root ultimately because we set it above
    # access best drop using that root index with respect to the number of root, to get the best pipe to enter. 
    print(bestdrops[group[s]])