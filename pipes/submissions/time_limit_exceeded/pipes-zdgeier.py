#!/usr/bin/python3

from collections import defaultdict

N = int(input())
F = [int(f) for f in input().split(' ')]

A = int(input())
D = [int(a) for a in input().split(' ')]

def BFS(graph, s):
    queue = []
    queue.append(s)
    queue.append(None)

    visited = [False] * N
    visited[s] = True

    min_index = N
    min_level = N
    possible = []
    level = 0

    while queue:

        s = queue.pop(0)

        if (s == None):
            level += 1
            queue.append(None)
            if (queue[0] == None):
                break
            continue

        if len(graph[s]) == 0:
            if level <= min_level and s < min_index:
                min_level = level
                min_index = s
            possible.append(s)

        for i in graph[s]:

            if visited[i] == False:
                if min_index == N:
                    queue.append(i)
                visited[i] = True

    return min_index

# Create reversed graph
graph = defaultdict(list)
for i,f in enumerate(F):
    if f != -1:
        graph[f].append(i)

for d in D:

    # Traverse to destination
    c = d
    while F[c] != -1:
        c = F[c]

    # BFS on reversed graph
    print(BFS(graph, c))
