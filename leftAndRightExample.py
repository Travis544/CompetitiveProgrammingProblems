def path(p):
    l,r = 1,1
    for x in p:
        # print("ENCOUNTER")
        # print(x)
        if x == 'R':
            for i in range(r,l-1,-1):
                # print("YIELDING 2")
                # print(str(i))
                yield str(i)
            l = r+1
        r += 1
    for i in range(r,l-1,-1):
        # print("YIELDING")
        # print(str(i))
       
        yield str(i)

def main():
    input()
    print('\n'.join(p for p in path(input())))

if __name__ == "__main__":
    main()

