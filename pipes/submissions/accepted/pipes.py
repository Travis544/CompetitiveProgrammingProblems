from collections import deque

n = int(raw_input())
F = [int(i) for i in raw_input().split()]

group = [0] * n
children = [[] for _ in range(n)]

rootcount = 0
for i in range(n):
    fi = F[i]
    if (fi != -1):
        children[fi].append(i)
    else:
        rootcount += 1
        group[i] = rootcount

bestdrops = [None] * (rootcount + 1)
visited = [False] * n

for i in range(n):

    if visited[i] or group[i] == 0:
        continue

    bfs = deque([])
    bfs.append((0, i))
    visited[i] = True
    bestdrop = (n, n)

    while len(bfs) > 0:

        d, u = bfs.popleft()

        if len(children[u]) == 0:
            bestdrop = min(bestdrop, ( d, u ))

        for c in children[u]:
            if not visited[c]:
                group[c] = group[i]
                visited[c] = True
                bfs.append(( d + 1, c ))

    bestdrops[group[i]] = bestdrop[1]

q = int(raw_input())
S = [int(i) for i in raw_input().split()]
for i in range(q):
    s = S[i]
    print(bestdrops[group[s]])

