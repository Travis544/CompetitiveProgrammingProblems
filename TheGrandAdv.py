

def main():
    n=int(input())
    res=[]
    for i in range(n):
        AdStr=input()
        con=determineAdventure(AdStr)
        res.append(con)
    for val in res:
        if(val):
            print("Yes")
        else:
            print("No")


def determineAdventure(AdStr):
    inventory=dict.fromkeys(['$', '*', '|'], 0)
    for i in range(len(AdStr)): 
        if AdStr[i]=='.':
            continue
        if AdStr[i] in inventory:
            inventory[AdStr[i]]+=1
        else:
            canContinue=meetPerson(AdStr[i], inventory)
            if canContinue==False:
                return False
    if(sum(inventory.values())>0):
        return False
    else:
        return True

def meetPerson(sym, inventory):
    canContinue=True
    mapping={'t':'|', 'b':'$', 'j':'*'}
    if(inventory[mapping[sym]] >0):
        inventory[mapping[sym]]-=1
    else:
        canContinue=False
    return canContinue
        
    

if __name__ == "__main__":
    main()