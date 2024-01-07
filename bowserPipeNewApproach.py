from collections import deque

nNodes = int(input())
nodes = list(map(lambda x: int(x), input().split(" ")))
nLeafToEnter = int(input())
leafToEnter = list(map(lambda x: int(x), input().split(" ")))

#Children for each node
children = [[] for _ in range(nNodes)]
graphIds = [0]*nNodes
graphId = 0

for i in range(nNodes):
    nodeVal = nodes[i]
   
    if nodeVal == -1:
        graphId = graphId+1
        graphIds[i] = graphId
    else:
        children[nodeVal].append(i)


#Given a forest of "graphs", 
# Use bfs to label the "graph" each node belong in and the closet node to root(other than root) for a graph
bestNodesForEachGraph  = dict()
nodeToGraphId = dict()
visited = [False]*nNodes

def bfs(graphId, start):
    currBestNode = (nNodes, nNodes)
    #Create a queue for bfs
    queue = deque([])
    # currDepth = 0
    # (depth, index of pipe)
    queue.append((0, start))    

    while len(queue) > 0:
        depth, nodeIndex = queue.popleft()
        nodeToGraphId[nodeIndex] = graphId
        # If this node has no children, then it is a leaf node.
        if len(children[nodeIndex]) == 0:
            #Min function will check first by depth, and break tie by node index
            currBestNode = min(currBestNode, (depth, nodeIndex))
        else:
            nodeChildren = children[nodeIndex]
            #Why can't I use current depth? If I pop a element, add its children, 
            # the current depth increase by one and now is 1, and the children has depth of 1.
            # Then if I pop another element, add its children, the current depth is now 2 and the children has depth of 2
            # However, this popped element is at the same level as the previous popped element, 
            # so its children should have depth of 2 as well.
            # currDepth = currDepth+1
            for child in nodeChildren:
                if visited[child]:
                     continue
                else:
                    visited[child] = True
                    queue.append((depth+1, child))
      
    bestNodesForEachGraph[graphId] = currBestNode[1]



for i in range(len(graphIds)):
    if graphIds[i] > 0:
        bfs(graphIds[i], i)


for i in range(nLeafToEnter):
    leaf = leafToEnter[i]
    graphId = nodeToGraphId[leaf]
    bestNode = bestNodesForEachGraph[graphId]
    print(bestNode)

            




    







