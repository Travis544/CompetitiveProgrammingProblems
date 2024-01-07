
def findMax():
        res=""
        for i in range(len(val[1:])):
            res+=str(digits[len(digits)-1])
            
        return res

def findMin():
        res=""
        for i in range(len(val[1:])):
            res+=str(digits[0])
        return res



val=input()
number=int(val)
val=list(map(int, list(val)))
digits=[]
ms=val[0]
for i in range(0,10):
    if not i in val or i==ms:
        digits.append(i)
  
if len(digits)==1:
    print("Impossible")

else:
    
    index=0
    for i in range(len(digits)):
        if ms==digits[i]:
            index=i
            break
        
    candidates=[]
    if len(digits)==2:
        digits.remove(ms)  
        candidates.append(digits[0])
        
    else:    
        digits.remove(ms)
        
        for i in range(len(digits)):
            candidates.append(digits[i])   
    res=[]
    for i in range(len(candidates)):
            temp=[]
            if candidates[i]<ms:
                rest=findMax()
                resultStr=str(candidates[i])+rest
                res.append(resultStr)
            elif candidates[i]>ms:
                rest=findMin()
                resultStr=str(candidates[i])+rest
                res.append(resultStr)
                
    min=abs(int(res[0])-number)
    minI=0
    final=[]
    for i in range(1, len(res)):
            if abs(int(res[i])-number)<min:
                minI=i
                min=abs(int(res[i])-number)
                
        
    for i in range(0, len(res)):
            if abs(int(res[i])-number)==min:

                
                if sum(list(map(int, list(res[i]))))==0:
                    final.append("0")
                elif res[i][0]=='0' and len(res[i])>1:
                        
                    final.append(res[i][1:])
                else:
                    final.append(res[i])
                    
    def check():
        for i in range(len(val)):
            if val[i]!=9:
                return False
        return True     
                    
    
    if check():
       if len(val)>1:
           print(str(number+1))
       else:    
            final.append(str(number+1)) 
            final.sort()
            print(*final)
    else: 
        final.sort()
        print(*final)

