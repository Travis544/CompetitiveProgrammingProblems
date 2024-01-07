val=input()
arr=val.split(" ")
n=int(arr[0])
price=int(arr[1])
num=int(arr[1])
commercial=input()
commercial=commercial.split(" ")

res=[]
for view in commercial:
    res.append(int(view)-price)

localMax=0
globalMax=0
for i in range(len(res)):
    localMax=max(res[i], res[i]+localMax)
    if localMax>globalMax:
        globalMax=localMax

print(globalMax)