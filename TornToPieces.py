# Torn to pieces
num=int(input())
graph=dict()
for i in range(num):
    connection=input().split(" ")
    start=connection[0]
    for stop in connection[1:]:
        if start in graph:
            graph[start].append(stop)
        else:
            graph[start]=[]
            graph[start].append(stop)
        
        if stop in graph:
            if not start in graph[stop]:
                graph[stop].append(start)
        else:
            graph[stop]=[]
            graph[stop].append(start)
            

            
def search(start, end):
    stack=[]
    visited=[]
    path=[]
    stack.append([start])
    while len(stack)>0:
        elem=stack.pop(0)
        value=elem[-1]
        visited.append(value)
        if value==end:
            return elem
        else:
            
            if value in graph:
                neighbors=graph[value]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        toAdd=elem.copy()
                        toAdd.append(neighbor)
                        stack.append(toAdd)
                    
                
toFind=input().split(" ")
path=None
if toFind and len(toFind)==2:  
    path=search(toFind[0], toFind[1])
if path==None:
    print("no route found")
else: 
    print(*path)