import string
length=input()
length=int(length)
scrambles=[input() for i in range(length)]

#create a list of all elements
x = list(string.ascii_lowercase)
x.insert(0, " ")

def encrypt(string):
    res=""
    count=0
    for i in range(len(string)): 
        val=x.index(string[i])
        res=res+x[((val+count)%27)]
        count=count+val
    print(res)

def decrypt(string):
    count=0
    res=""
    for i in range(len(string)):
        curVal=x.index(string[i])
        for j in range(27):
            if (count+j)%27==curVal:
                res=res+x[j]
                count=count+j
                break
            
    print(res)

for scramble in scrambles:
    if scramble[0]=="e" :
        encrypt(scramble[2:])
    else:
        decrypt(scramble[2:])