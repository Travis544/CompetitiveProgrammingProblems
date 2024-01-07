
import os
import testAlien
tests=[]
answers=[]
def load():
    # print(os.listdir('./naq21data/alienintegers/data/secret'))
    answer=True
    ques=False
    for file in os.listdir('./naq21data/alienintegers/data/secret'):
        f = open("./naq21data/alienintegers/data/secret"+"/"+file, "r")
        data=f.readlines()[0]
        extension=file.split('.')[1]
       
        data=data.replace("\n","")
        data=data.replace(" ", "")
        if extension=="ans":
            answers.append(data)
        else:
            tests.append(data)
        # if answer==True:
        #     answers.append(data)
        #     answer=False
        #     ques=True
        # if ques==True:
        #     tests.append(data)
        #     ques=False
        #     answer=True
    print(len(answers))
    print(len(tests))
        
        



def runTest(toTest):
    errors=0
    
    for i in range(len(tests)):
        res=toTest(tests[i])
      
        res=res.replace(" ","")
        print("Test:  "+str(i))
        if res!=answers[i]:
            print("Expected "+answers[i])
            print("But got: "+res)
            errors=errors+1
    print(errors)

load()

runTest(testAlien.findAlien)


