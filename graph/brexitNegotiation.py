import heapq

class Node:
  def __init__(self, id, weight, degree, edges):
    self.id = id
    self.weight = weight
    self.degree = degree
    self.edges = edges



def topologicalSort(nodes):
    visitedCount = len(nodes)-1
    sortedArr = []
    visited = dict() 
    minimumMaxTimeforMeeting = None
    priorityQueue = []
    for node in nodes:
        if node.degree == 0:
            heapq.heappush(priorityQueue, (node.weight, node.id))
            visited[node.id] = True

    while len(priorityQueue)>0:
        weight, id = heapq.heappop(priorityQueue)
        sortedArr.append(id)
        currNode = nodes[id]
        # nodeToVisitedCount[id] = visitedCount
     
        if minimumMaxTimeforMeeting == None or currNode.weight+visitedCount>minimumMaxTimeforMeeting:
            minimumMaxTimeforMeeting = currNode.weight+visitedCount

        visitedCount = visitedCount-1
        for childrenId in currNode.edges:
            childNode = nodes[childrenId]
           
            newDegree = childNode.degree-1
            childNode.degree = newDegree
            if newDegree == 0:
                # if childrenId in visited:
                #     continue
                # else:
                    visited[childrenId] = True
                    heapq.heappush(priorityQueue, (childNode.weight, childNode.id))

            visited[childrenId] = True

    return (sortedArr, minimumMaxTimeforMeeting)

n  = int(input())
nodes = []
edges = []
for i in range(n):
    topic = list(map(lambda x: int(x), input().split(" ")))
    weight = topic[0]
    numIncoming = topic[1]
   
    for j in range(2, 2+numIncoming):
        # edges are incoming to the current node
        nodeId = topic[j]-1
        edges.append((nodeId, i))

    node = Node(i, weight, 0,[])
    nodes.append(node)


for edge in edges:
   
    fro =  edge[0]
    to = edge[1]
    """
    build in opposite, why? consider 1 -> 100, 2, 3. We want to look at all the sink first, because 
    if we build the graph normally, and we prioritize the max weight, assigning time for it first,
    if there is a vertice with small weight that leads to a node with huge weight, that huge weight will be assigned
    late. If we build the graph in reverse, we can look at the huge weight, giving it priority to assign it earlier.
    then assigning its dependency earlier time. 

    Counterargument: what if we have node with the largest weight as source leading to the smallest node
    if we reverse build the graph, same thing, the largest weight will be assigned the earliest time,
    which matches our way of prioritizing max weight. 
    """
    nodes[to].edges.append(fro)
    nodes[fro].degree = nodes[fro].degree+1


sortedArr, minimumMaxTimeForMeeting = topologicalSort(nodes)
print(minimumMaxTimeForMeeting)





