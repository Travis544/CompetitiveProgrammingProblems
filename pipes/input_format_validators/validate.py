#!/usr/bin/python

import sys

MAX_ADDRESS_COUNT = 100000
MAX_DELIVERY_COUNT = 100000

def cyclic(graph):
    visited = set()
    path = [object()]
    path_set = set(path)
    stack = [iter(graph)]
    while stack:
        for v in stack[-1]:
            if v in path_set:
                return True
            elif v not in visited:
                visited.add(v)
                path.append(v)
                path_set.add(v)
                stack.append(iter(graph.get(v, ())))
                break
        else:
            path_set.remove(path.pop())
            stack.pop()
    return False

N = int(raw_input())
assert 0 < N <= MAX_ADDRESS_COUNT

F = [int(f) for f in raw_input().split(' ')]
assert len(F) == N

for f in F:
    assert -1 <= f < N

A = int(raw_input())
assert 0 < A <= MAX_DELIVERY_COUNT

D = [int(a) for a in raw_input().split(' ')]
assert len(D) == A

for d in D:
    assert 0 <= d < N

graph = dict((i, (v,)) for i,v in enumerate(F))
assert(not cyclic(graph))

sys.exit(42)
