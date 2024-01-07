def binpow(a,b):
    if (b == 0):
        print("RETURNING ONE")
        return 1
    res = binpow(a, b // 2)
    if (b % 2):
        print("CURRENT IS ODD Return"+ str(res) +"*"+ str(res) +"*"+ str(a))
        return res * res * a
    else:
        print("CURRENT IS EVEN Return"+str(res) +"*"+ str(res))
        return res * res


print(binpow(3,13))