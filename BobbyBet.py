
# Bobby's bets
# Bobby and Betty have a bet. Betty bets Bobby that he cannot roll an S-sided die (having values 1 through S) and obtain a value ≥R on at least X out of Y rolls. Betty has a variety of dice with different numbers of sides S, and all her dice are fair (for a given die, each side’s outcome is equally likely). In order to observe statistically rare events while still giving Bobby a reason to bet, Betty offers to pay Bobby W times his bet on each encounter. For example, suppose Betty bets Bobby 1 bitcoin that he can’t roll at least a 5 on a 6-sided die at least two out of three times; if Bobby does, she would give him W=3 times his initial bet (i.e. she would give him 3 bitcoins). Should Bobby take the bet (is his expected return greater than his original bet)?

#Input: Input begins with an integer 1≤N≤10000, representing the number of cases that follow. The next N lines each contain five integers, R, S, X, Y, and W. Their limits are 1≤R≤S≤20, 1≤X≤Y≤10, and 1≤W≤100.
#Output:For each case, output “yes” if Bobby’s expected return is greater than his bet, or “no” otherwise. Bobby is somewhat risk averse and does not bet if his expected return is equal to his bet.
num=int(input())

bin = [[0 for x in range(11)] for y in range(11)] 
bin[0][0]=1

def binomial(n,k):
    if n<0 or k>n:
        return 0
    else:
        return bin[n][k]
    
def buildBinomial():
    for i in range(1,11):
        for j in range(0, i+1):
            bin[i][j]=binomial(i-1,j)+binomial(i-1,j-1)
        
            
buildBinomial()
for i in range(num):
    R,S,X,Y,W=list(map(int, input().split(" ")))
    pWin=0
    for n in range(X,Y+1):
        pWin+=binomial(Y,n)*(((S-R+1)/S)**n)*((1-((S-R+1)/S))**(Y-n))
    if ((pWin*(W-1)+((1-pWin)*(-1)))>0):
        print("yes")
    else:
        print("no")

   