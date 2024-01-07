num=int(input())
for i in range(num):
    command=input().split(" ")
    if command[0]=="Simon" and command[1]=="says":
        print(*command[2:])