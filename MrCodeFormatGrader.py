n, e=input().split(" ")
n=int(n)
e=int(e)
error=list(map(int,input().split(" ")))
ErrorRes=[]
CorrectRes=[]

current=error[0]
next=error[1]
index=1
start=0
for i in range(0, len(error)-1):
    conse=[]
    ErrorRes.append(current)
    start=0
    while True:
        if next-current>1:
            break
        else:
            
    # while next-current==1:
    #     current=next
    #     conse.append(current)
    #     index=index+1
    #     next=error[index]
    
    
        
        
        
    
    