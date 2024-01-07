
class UnionFind:
    def __init__(self, init_arr, annotations, queryNum):
        self.numComponents  = len(init_arr)
        # self.id[i] points to the parent nod eof i
        # self.id[i] == i ,then i is a root node
        self.id = [0]*self.numComponents
        self.size = [0]*self.numComponents
        self.annotations = annotations
        # self.lastMerged = 0
        # self.prevWeight= -1
        # self.lastMergedQueries = set()
        # self.sizeLookup = dict()
        self.answer = [0]*numQueries

        for i in range(self.numComponents):
            self.id[i] = i
            self.size[i] = 1

    
    #find and perform path compression
    def find(self, p):
        root = p
        while(root != self.id[root]):
            root = self.id[root]
        
        # Compress path leading to root
        while(p != root):
            next = self.id[p]
            self.id[p] = root
            p = next

        return root

    def connected(self,p, q):
        return self.find(p) == self.find(q)

    def componentSize(self,p):
        return self.size[self.find(p)]
    
    def unify(self,p, q, weight):
        solved = []
        root1 = self.find(p)
        root2 = self.find(q)

        toDel = None 
        toSav = None

        if root1==root2:
            return solved

    
        if self.size[root1] < self.size[root2]:
            self.id[root1] = root2
            self.size[root2] += self.size[root1]
            toDel = root1
            toSav = root2
        else:
            self.id[root2] = root1
            self.size[root1] += self.size[root2]
            toDel = root2
            toSav = root1

        self.numComponents = self.numComponents - 1
        for key in self.annotations[toDel]:
    
            if not key in self.annotations[toSav]:
                self.annotations[toSav][key] = self.annotations[toDel][key]
            else:
                # self.lastMergedQueries.add(key)
                solved.append((key,p))
                self.annotations[toSav][key] = True
                # self.annotations[toSav][key] = (weight, self.size[toSav])
                
        return solved



numCities, numRoads, numQueries = list(
    map(lambda x: int(x), input().split(" ")))
graph = []
disjointSet = []
queries = []
annotations = [dict() for i in range(numCities)]
tollToEdge = dict()
tolls = []

for i in range(numRoads):
    start, end, toll = list(map(lambda x: int(x), input().split(" ")))
    disjointSet.append(start)
    disjointSet.append(end)
    # graph.append((toll, start, end))
    tolls.append(toll)
    if not toll in tollToEdge:
        tollToEdge[toll] = [(start, end)]
    else:
        tollToEdge[toll].append((start, end))


# print(numQueries)
# print(self.annotations)


for i in range(numQueries):
    qStart, qEnd = list(map(lambda x: int(x), input().split(" ")))
    queries.append((qStart, qEnd))
    annotations[qStart-1][i] = True
    annotations[qEnd-1][i] = True





disjointSet = list(set(disjointSet))

disjointSet =  UnionFind(disjointSet, annotations, numQueries)

lastIndex = [0]
# print("GRAH")
# print(graph)
tolls.sort()
def solve():
    for t in tolls:
        edges = tollToEdge[t]
        # print("______")
        # print(tollToEdge)
        allSolved= []
        for edge in edges:
            start, end = edge
            solved = disjointSet.unify(start-1, end-1, t)
            allSolved = allSolved + solved

        for s in allSolved:
            query, p = s
           
            disjointSet.answer[query] = (t, disjointSet.size[disjointSet.find(p)])
    

solve()

# for key in annotation:
#     weight, k = annotation[key]
#     newK=disjointSet.sizeLookup[weight]
#     annotation[key] = (weight, newK)


for i in range(numQueries):
   w,k = disjointSet.answer[i]
   print(w,k)