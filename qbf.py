a =int(input())
seq = []
for k in range(a):
    seq.append(input().lower())


def check_existence(n,str):
    for i in range(len(str)):
        if n == str[i]:

            return True
    return False

for m in range(len(seq)):
    string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for n in range(len(seq[m])):
        if check_existence(seq[m][n],string):
            string.remove(seq[m][n])
    str = ''
    for m in range(len(string)):
        str += string[m]
    if not str:
        print("pangram")
    else:
        print("missing ",end="")    
        print(str)
