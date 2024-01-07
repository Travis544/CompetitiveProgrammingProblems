class Graph:
    def __init__(self, graph):
        self.graph = graph  
        self.ROW = len(graph)
        # self.COL = len(gr[0])
        
    def BFS(self, source, sink, parent):
        visited = [False]*(self.ROW)
        queue=[]
        queue.append(source)
        visited[source]=True
        while len(queue)>0:
            u=queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind]==False and val>0:
                    queue.append(ind)
                    visited[ind]=True
                    parent[ind]=u
                    if ind==sink: 
                        return True
        return False
    
    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self,source, sink):
        # might need to change this
        totalFlow=0
        parent=[-1]*self.ROW
        allPaths=[]
        while self.BFS(source, sink, parent):
            augmentedPath=[]
            minFlow=float('inf')
            current=sink
            while current!=source:
                minFlow=min(minFlow, self.graph[parent[current]][current])
                augmentedPath.insert(0, current)
                current=parent[current]
            # augmentedPath.insert(0,source)
            totalFlow+=minFlow
            allPaths.append(augmentedPath)
            start=sink
            # update residual graph
            while start!=source:
                self.graph[parent[start]][start]-=minFlow
                self.graph[start][parent[start]]+=minFlow
                start=parent[start]    
                
        return (totalFlow, allPaths)
 
def generateGraph(ra,days, raName, availableDays, k):
    graph=[]
    for i in range(2+ra+days):
        graph.append([0]*(2+ra+days))
    for i in range(1, days+1):
        graph[0][i]=2 
    for i in range(len(availableDays)):
        for j in range(len(availableDays[i])):
            day=int(availableDays[i][j])
            graph[day][days+1+i]=1 
    sink=len(graph)-1
    for i in range(days+1,days+1+ra):
        graph[i][sink]=k
    # for i in range(1, days+1):
    #     for j in range(days+1,ra+1):
    #         graph[i][j]=
    return graph
        
 
ra, days=list(map(int, input().split(' ') ))
raName=[]
availableDays=[]
for i in range(ra):
    val = input().split(' ')
    raName.append(val[0])
    availableDays.append(val[2:])

for k in range(1,days+1):
    graph=generateGraph(ra,days,raName,availableDays,k)
    
# print(graph)
    g = Graph(graph)
    source = 0; sink = len(graph[0])-1
    totalFlow, allPath=g.FordFulkerson(source, sink)
    needRedo=False
    # print("__________-")
    # print(i)
    # print(totalFlow)
    # print("__________-")
    if totalFlow>=2*days:
        # print(totalFlow)
        # print(i)
       
        schedule=dict()
        for i in range(1, days+1):
            for j in range(days+1, days+1+ra):
                if g.graph[j][i]>0:
                    #   print(g.graph[j][i])
                      index=j-days-1
                      if not i in schedule:
                        schedule[i]=[raName[index]]
                      else:
                        schedule[i].append(raName[index])
                
        # for i in range(len(allPath)): 
        #     # if len(allPath[i])!=3:
                
        #     index=allPath[i][1]-days-1
            
        #     if not allPath[i][0] in schedule:
                
        #         schedule[allPath[i][0]]=[raName[index]]
        #     else:
        #         schedule[allPath[i][0]].append(raName[index])
                
        # if needRedo:
            
        #     needRedo=False
        #     continue
        
        # print(allPath)
        # print(g.graph[days+1])
        # print("DAY")
        print(k)
        for key in schedule:
            # print(schedule[key])
            print("Day "+str(key)+": ", *schedule[key])
        
        break
    else:
        continue
                
   
            
