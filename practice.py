
def findKing(num):
    for i in range(2, len(num)-1):
        # if int(num[i])>int(num[i-1]) and int(num[i])>int(num[i+1]):
        #     return i
        # elif int(num[i])<int(num[i-1]) and int(num[i])<int(num[i+1]):
        #     return 
        # 
        if int(num[i])-int(num[i-1])>1 or int(num[i])-int(num[i-1])<1:
            return i
        
            
        # if int(num[i])>int(num[i+1]):
        #     return i+1
            
num=input()
if num:

    res=[]
    lines=[]
    for i in range(int(num)): 
        line=input()
        lines.append(line)
        
    for line in lines:
        index=findKing(line.split(" "))
        res.append(index)
    for val in res:
        print(val)
    
