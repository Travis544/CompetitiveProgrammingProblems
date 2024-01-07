


from string import ascii_lowercase

letToValue=dict()

nums=["0","1","2","3","4","5","6","7","8","9"]

for c in ascii_lowercase:
    letToValue[c]=ord(c)-87


def toNumber(representation, base):
    total=0
    toMuliply=0
    leng=len(representation)-1
    for i in reversed(range(len(representation))):
        #print(representation[i])
        if not representation[leng-i] in nums:
            toMuliply=letToValue[representation[leng-i]]
        else:
            toMuliply=int(representation[leng-i])
            
        # print(base**i)   
        # print("SSS"+str(toMuliply)) 
        #print(toMuliply*(base**i))
       
           
        total=total+toMuliply*(base**i)
        if base==1: 
            if toMuliply>base or toMuliply==0:
                return -1
        elif toMuliply>base-1:
            return -1
        
       
            
    return total

#  +, -, *, /
def eval_exp(num1, num2, num3, op):
    if op=="+":
        return num1+num2==num3
    elif op=="-":
        return num1-num2==num3
    elif op=="*":
        return num1*num2==num3
    elif op=="/":
        return num1/num2==num3



num=int(input())

for i in range(num):
    exp=input().split(" ")
    possible=[]
    for j in range(1, 37):
        val=toNumber(exp[0], j)
        val2=toNumber(exp[2], j)
        val3=toNumber(exp[4],j)
        if val==-1 or val2==-1 or val3==-1:
            continue
        m=(2**32)-1
        if val >m or val2>m or val3>m:
            continue
        
        if eval_exp(val, val2, val3, exp[1]):
            if j<10:
                possible.append(str(j))
            else:
                if j==36:
                    possible.append("0")
                else:
                    for key in letToValue:
                        if letToValue[key]==j:
                            possible.append(key)
                            break
                
    if len(possible)==0:
        print("invalid")
    else:
        print("".join(possible))   
