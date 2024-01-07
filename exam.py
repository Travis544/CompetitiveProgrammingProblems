friendCorrect=input()
myAnswer=input()
friendAnswer=input()
match=0
for i in range(len(myAnswer)):
    if myAnswer[i]==friendAnswer[i]:
        match+=1

friendCorrect=int(friendCorrect)
if friendCorrect>=match:
    print(len(myAnswer)- (friendCorrect-match))
else:
    print(len(myAnswer)- (match-friendCorrect))