N = 100000
F = []
D = []

F.append(-1)
for i in range(1, N):
    F.append(i-1)

for i in range(1, N):
    D.append(N-1);

print N
for f in F:
    print f,
print
print len(D)
for d in D:
    print d,
