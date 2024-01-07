
C,N=input().split(" ")
N=int(N)
C=int(C)
error=list(map(int, input().split(" ")))
print(error)
print(N,C)


def exist(n, list):
    for a in range(len(list) - 1):
        if n == list[a]:
            return True
    return False

def find_end(a, b, list):
    while list[b] - list[a] == b - a:
        if b == len(list) - 1:
            print(" and ", end="")
            return b
        b += 1
    return b - 1

def print_list(list):
    a = 0
    b = 1
    while b<len(list):
        if list[a] + 1 != list[b]:
            if a != 0:
                print(",",end="")
                print(" ",end="")
            print(list[a], end="")
            a += 1
            b += 1
        else:
            b = find_end(a, b, list)
            print(list[a], end="")
            print("-",end="")
            print(list[b], end="")
            a = b + 1
            b = a + 1




correct = []

for k in range(1, 21):
    if not exist(k, error):
        correct.append(k)


print("Errors: ", end="")
print_list(error)
print("")
print("Correct: ", end="")
print_list(correct)



