





def findAlien(val):
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
        return "Impossible"
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
                cont=False
                return "0"
                
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
            
            # print(final)
            # print(*final)
            
            return ' '.join(list(map(str, final)))

