
import sys
import math
sys.setrecursionlimit(100000)

# class SparseTable:
#     def __init__(self, arr, func, isOverlapFriendly, isMin, isMax): 
#         self.n =len(arr)
#         self.func = func
#         self.isOverlapFriendly = isOverlapFriendly
#         self.isMin = isMin
#         self.isMax = isMax
#         #Maximum power of 2 needed: floor(log2(n))
#         self.P = math.floor(math.log(self.n)/math.log(2))
#         self.dp = []
#         #Index table, index associated with value in sparse table.
#         self.it = []
#         for _ in range(self.P+1):
#             row = []
#             row2= []
#             for i in range(self.n):
#                 row.append(0)
#                 row2.append(0)
#             self.dp.append(row)
#             self.it.append(row2)

#         for i in range(self.n):
#             self.dp[0][i]= arr[i]
#             self.it[0][i] = i
        

#         # Fast base2 log lookup table. i =2, tell you what log2(2) is
#         self.log2 = [0]*(self.n+1)
#         for i in range(2, self.n+1):
#             self.log2[i] = self.log2[i//2] +1
      
#         # self.powerOfTwo= [0]*self.P
#         # self.powerOfTwo[0]=1
#         # for i in range(1,self.P+1):
#         #     self.powerOfTwo[i] =  self.powerOfTwo[i-1]*2

#         self.buildSparseTable()

#     # build min sparse table, but we can change min to something else as well.
#     def buildSparseTable(self):
#         for p in range(1, self.P+1):
#             for j in range(0,self.n):
#                 #<< is left shift, essentially calculating 1 multiple by 2 j times.
#                 jPlus2ToThePthPower = j+(1<<p)
#                 if jPlus2ToThePthPower > self.n:
#                     break
#                 #split the current i,j cell representing [j,j+2^i] to [j, j+2^(i-1), j+2^(i-1), j+2^i]
#                 jPlus2ToThePthMinusOnePower =j+(1<<(p-1))
#                 leftInterval = self.dp[p-1][j]
#                 rightInterval = self.dp[p-1][jPlus2ToThePthMinusOnePower]
#                 self.dp[p][j] = self.func(leftInterval, rightInterval)

#                 # Update index table, only useful for min and max range query table
#                 if(self.isOverlapFriendly):
#                     update = self.determineUpdate(leftInterval, rightInterval)
#                     if (update):
#                         self.it[p][j] = self.it[p-1][j]
#                     else:
#                         self.it[p][j] = self.it[p-1][jPlus2ToThePthMinusOnePower]

#     def determineUpdate(self, leftInterval, rightInterval):
#         if self.isMin:
#             return leftInterval<=rightInterval
#         elif self.isMax:
#             return leftInterval>= rightInterval

#     def queryOverlapFriendly(self,left, right):
#         length = right - left + 1
#         p = self.log2[length]
#         # 2^p
#         k = self.powerOfTwo[p]
#         return self.func(self.dp[p][left], self.dp[p][right-k+1])

#     #only for overlap friendly function
#     def queryIndex(self, left, right):
#         length = right - left + 1
#         p = self.log2[length]
#         # 2^p
#         k = 1<<p
#         leftInterval = self.dp[p][left]
#         rightInterval = self.dp[p][right-k+1]
#         update = self.determineUpdate(leftInterval, rightInterval)
#         if update:
#             return self.it[p][left]
#         else:
#             return self.it[p][right-k+1]

 
#     # divide query range into discrete ranges of powers of 2.
#     def queryNonOverlapFriendly(self,left, right):
#         curr = None
#         while left<=right:
#             length = right - left + 1
#             p = self.log2[length]
#             if curr == None:
#                 curr = self.dp[p][left]
#             else:
#                 curr = self.func(curr, self.dp[p][left])
#             left = left+ (1<<p)
#         return curr


        
def treeify(tree, root):
    for edge in tree[root]:
        if root in tree[edge]:
            del tree[edge][root]
        treeify(tree, edge)





class SegmentTree:
    def __init__(self, array):
        self.size = len(array)
        self.arr = array
        self.tree = [0] * (4 * self.size)
        self.indexTree = [0] * (4 * self.size)
        self.build_tree(array, 0, 0, self.size - 1)
 
    def build_tree(self, array, tree_index, left, right):
        if left == right:
            # self.tree[tree_index] = array[left]
            
            self.indexTree[tree_index] = left
            return
        mid = (left + right) // 2
        self.build_tree(array, (tree_index *2 )+1, left, mid)
        self.build_tree(array, (tree_index *2)+2, mid + 1, right)
        #self.tree[tree_index] = min(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])
        leftChildMinIndex = self.indexTree[tree_index*2+1]
        rightChildMinIndex = self.indexTree[tree_index*2+2]
        if self.arr[leftChildMinIndex] <= self.arr[rightChildMinIndex]:
            self.indexTree[tree_index] = leftChildMinIndex
        else: 
            self.indexTree[tree_index] = rightChildMinIndex

    def query(self, tree_index, left, right, query_left, query_right):

        if (query_left>right) or (query_right < left):
            return -1
         
        if query_left <= left and right <= query_right:
            return  self.indexTree[tree_index]



        mid = (left + right) // 2
        
        index1 = self.query((tree_index * 2)+1, left, mid, query_left, query_right)
        index2 = self.query((tree_index * 2)+2, mid + 1, right, query_left, query_right)
        if index1==-1:
            return index2
        
        if index2 == -1:
            return index1

        if self.arr[index1] <= self.arr[index2]:
            return index1
        else:
            return index2
       
 
    def query_range(self, left, right):
        return self.query(0, 0, self.size - 1, left, right)


def dfs(cur, depth, L,E,  H, idx,  tree):
    index = idx[0]
    H[cur] = idx[0]
    E[index] = cur
    L[index] = depth
    idx[0] = idx[0] +1
    for edge in tree[cur]:
        dfs(edge, depth+1, L, E,H, idx, tree)
        E[idx[0]] = cur
        # print("INDEX")
        # print(idx[0])
        # print(H)
        L[idx[0]] = depth
        idx[0] = idx[0]+1

    
   
       
# def dfs(node,nodes, tourIndexToNodes, depth, nodesToTourIndex, node_depth):
    
#     # visit(node, node_depth, tourIndexToNodes, depth, nodesToTourIndex)
#     tourIndex =tour_index[0]
   
#     tourIndexToNodes[tourIndex] =  node

#     depth[tourIndex] = node_depth
   
#     nodesToTourIndex[node] = tourIndex
#     tour_index[0] = tour_index[0] + 1

#     for edge in nodes[node]:
#         # try:
#         dfs(edge, nodes, tourIndexToNodes, depth, nodesToTourIndex, node_depth+1)
#         # visit(node, node_depth, tourIndexToNodes, depth, nodesToTourIndex )
#         tourIndex =tour_index[0]
#         tourIndexToNodes[tourIndex] =  node
#         depth[tourIndex] = node_depth
#         nodesToTourIndex[node] = tourIndex
#         tour_index[0] = tour_index[0] + 1
       


# def visit(node, node_depth, tourIndexToNodes, depth, nodesToTourIndex):


#     tourIndex =tour_index[0]
   
#     tourIndexToNodes[tourIndex] =  node

#     depth[tourIndex] = node_depth
   
#     nodesToTourIndex[node] = tourIndex
#     tour_index[0] = tour_index[0] + 1
  
            
def eulerianTour(node, tree, length):

    tourIndexToNodes = [0]*((2*length)-1)
    depth = [0]*((2*length)-1)
   
    nodesToTourIndex = [0]*(length)
    tour_index =[0]
    # dfs(node,nodes, tourIndexToNodes, depth, nodesToTourIndex,0 )
    # cur,depth, L,E,  H, idx,  tree
    dfs(0 , 0, depth, tourIndexToNodes, nodesToTourIndex,tour_index, tree )
    return (tourIndexToNodes, depth, nodesToTourIndex)


def lca(nodeIndex1, nodeIndex2, nodesToTourIndex, segmentTree : SegmentTree, tourIndexToNodes):

    lo = nodesToTourIndex[nodeIndex1]
    hi = nodesToTourIndex[nodeIndex2]
    if not (lo < hi):
        tmp = lo
        lo = hi
        hi = tmp
    # print("QUERYING", lo,hi)
    minValueIndex = segmentTree.query_range(lo, hi)
    return tourIndexToNodes[minValueIndex]



testCases = int(input())
for i in range(testCases):
   
    n = int(input())
    tree = []
    for j in range(n):
        tree.append(dict())
  
    for _ in range(0,n-1):
        fro, to = map(int, input().split(" "))
        tree[fro-1][to-1] = True
        tree[to-1][fro-1] = True

    permutation = []
    for k in range(n):
        p = int(input())
        permutation.append(p-1)

    treeify(tree, 0)
    tourIndexToNodes, depth, nodesToTourIndex = eulerianTour(0,tree, n)
    flag = 1

    # minSparseTable = SparseTable(depth,min, isOverlapFriendly=True, isMin=True, isMax=False )
    segmentTree = SegmentTree(depth)
    # print(permutation)
    for i in range(0, len(permutation)-1):
      
        node1= permutation[i]
        node2 = permutation[i+1]
        elerianIndex1 = nodesToTourIndex[node1]
        elerianIndex2 =  nodesToTourIndex[node2]
        ancestor = lca(node1, node2, nodesToTourIndex, segmentTree, tourIndexToNodes)
        ancestorElerianIndex = nodesToTourIndex[ancestor]
        # distance between can be calculated by the following formula
        distance = (depth[elerianIndex1] + depth[elerianIndex2]) - (2*depth[ancestorElerianIndex])
       
        # print("ANSCESTOR")
        # print(ancestor)
        # print(node1, node2)
        # print(depth)
        # print("DISTANCE")
        # print(distance)
       
        if distance > 3:
            flag = 0
            break
    # print("SS")
    print(flag)
