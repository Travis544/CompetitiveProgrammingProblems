# Alien Number
# Exploratory robots are essential to expanding our understanding of the moon, Mars, and other celestial bodies. When there are two or more robots in the same vicinity, they need to be marked by humanly readable integers for purposes of visual tracking. 
# To reduce the possibility of error in visual recognition of the robots in dark and dusty environments, numbers are chosen so that they have no digits in common. More formally, two non-negative integers are alien to each other if there is no digit which occurs in both of their decimal representations. For example, 11229 and 67840 are alien to each other, while 2022 and 427 are not. No integer is alien to 1234567890.
#The numbers on robots in the same area should also be close to each other numerically (for instance, to simplify processing of the marks by the software, to make them easy to remember, to distinguish them from other groups of robots marked in similar manner, …).
#The Institute for Computerized Planetary Circumambulation needs a program to identify the nearest number that is alien to a given number. Can you help?

# Input
# The input consists of an integer N (1≤N≤1015) given on a single line.

# Output
# When there is one non-negative alien integer Y closest to the input number N, output the value of Y. When there are two such integers that are equally close to the input number N,  output both of them in ascending order, on a single line. When there is no integer alien to the input number N, output Impossible.
val=input()
number=int(val)
val=list(map(int, list(val)))
DNUX=[]
LD=val[0]
for i in range(0,10):
    if not i in val:
        DNUX.append(i)

res=[]
# find the smallest digit bigger than the leading digit ld. if there is a digit bigger than ld
def helper(x):
    if x<LD:
        return True
    else:
        return False

def helper2(x):
    if x>LD:
        return True
    else:
        return False   
    
if len(DNUX)==0:
    print("Impossible")
else:
    
    minDNUX=min(DNUX)
    maxDNUX=max(DNUX)

    def findMin():
        mins=list(filter(helper,DNUX))
        if (len(mins)==0):
            return str(maxDNUX)*(len(val)-1)
        maxMin=max(mins) 
       
        return str(maxMin)+str(maxDNUX)*(len(val)-1)


    def findMax(hasZero=False):
        maxs=list(filter(helper2,DNUX))
        if (len(maxs)==0):
            if hasZero:
                return str(minDNUX)+"0"*(len(val))
            else:
                return str(minDNUX)*(len(val)+1)
        minMax=min(maxs) 
        if hasZero:
           
            return str(minMax)+"0"*(len(val)-1)
        else:
            return str(minMax)+str(minDNUX)*(len(val)-1)
        
    hasZero=False
    cont=True
    if DNUX[0]==0:
        if len(DNUX[1:])==0:
            print( "0")
            cont=False
        if cont==True:
            minDNUX=min(DNUX[1:])
            hasZero=True
    if cont==True:
        r=findMin()
        # if r!="":
        #     if r[0]!='0' or (r[0]=='0' and len(r)==1):
        res.append(findMin())
            
        res.append(findMax(hasZero))

        small=int(res[0])
        final=[]
        for v in res:
            if abs((int(v)-number))<abs(small-number):
                small=int(v)
            
        for t in res:
            if abs((int(t)-number))==abs(small-number):
                final.append(int(t))
        
        print(*final)

