numClick=input()
A=1
B=0
for i in range(int(numClick)):
    temp=B
    B+=A
    A=0
    A+=temp

print(A, B)
