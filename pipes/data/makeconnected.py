N = 100000
connections = 1000
F = []
D = []

for i in range(0, N, connections+1):
    F.append(-1)
    for c in range(connections):
        if len(F) < N:
            F.append(i)

for i,f in enumerate(F):
    if f != -1:
        D.append(i);

print N
for f in F:
    print f,
print
print len(D)
for d in D:
    print d,
