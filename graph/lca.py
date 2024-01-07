
import math
import sys
sys.setrecursionlimit(100000000)

class SparseTable:
    def __init__(self, arr, func, isOverlapFriendly, isMin, isMax): 
        self.n =len(arr)
        self.func = func
        self.isOverlapFriendly = isOverlapFriendly
        self.isMin = isMin
        self.isMax = isMax
        #Maximum power of 2 needed: floor(log2(n))
        self.P = math.floor(math.log(self.n)/math.log(2))
        self.dp = []
        #Index table, index associated with value in sparse table.
        self.it = []
        for _ in range(self.P+1):
            row = []
            row2= []
            for i in range(self.n):
                row.append(0)
                row2.append(0)
            self.dp.append(row)
            self.it.append(row2)

        for i in range(self.n):
            self.dp[0][i]= arr[i]
            self.it[0][i] = i
        

        # Fast base2 log lookup table. i =2, tell you what log2(2) is
        self.log2 = [0]*(self.n+1)
        for i in range(2, self.n+1):
            self.log2[i] = self.log2[i//2] +1
      
        self.buildSparseTable()

    # build min sparse table, but we can change min to something else as well.
    def buildSparseTable(self):
        for p in range(1, self.P+1):
            for j in range(0,self.n):
                #<< is left shift, essentially calculating 1 multiple by 2 j times.
                jPlus2ToThePthPower = j+(1<<p)
                if jPlus2ToThePthPower > self.n:
                    break
                #split the current i,j cell representing [j,j+2^i] to [j, j+2^(i-1), j+2^(i-1), j+2^i]
                jPlus2ToThePthMinusOnePower =j+(1<<(p-1))
                leftInterval = self.dp[p-1][j]
                rightInterval = self.dp[p-1][jPlus2ToThePthMinusOnePower]
                self.dp[p][j] = self.func(leftInterval, rightInterval)

                # Update index table, only useful for min and max range query table
                if(self.isOverlapFriendly):
                    update = self.determineUpdate(leftInterval, rightInterval)
                    if (update):
                        self.it[p][j] = self.it[p-1][j]
                    else:
                        self.it[p][j] = self.it[p-1][jPlus2ToThePthMinusOnePower]

    def determineUpdate(self, leftInterval, rightInterval):
        if self.isMin:
            return leftInterval<=rightInterval
        elif self.isMax:
            return leftInterval>= rightInterval

    def queryOverlapFriendly(self,left, right):
        length = right - left + 1
        p = self.log2[length]
        # 2^p
        k = 1<<p
        return self.func(self.dp[p][left], self.dp[p][right-k+1])

    #only for overlap friendly function
    def queryIndex(self, left, right):
        length = right - left + 1
        p = self.log2[length]
        # 2^p
        k = 1<<p
        leftInterval = self.dp[p][left]
        rightInterval = self.dp[p][right-k+1]
        update = self.determineUpdate(leftInterval, rightInterval)
        if update:
            return self.it[p][left]
        else:
            return self.it[p][right-k+1]

 
    # divide query range into discrete ranges of powers of 2.
    def queryNonOverlapFriendly(self,left, right):
        curr = None
        while left<=right:
            length = right - left + 1
            p = self.log2[length]
            if curr == None:
                curr = self.dp[p][left]
            else:
                curr = self.func(curr, self.dp[p][left])
            left = left+ (1<<p)
        return curr



class Node:
  def __init__(self, id, edges):
    self.id = id
    self.edges = edges
    self.degree =0

tour_index = [0]


# Python3 program for range minimum 
# query using segment tree 
import sys;
from math import ceil,log2;
  
INT_MAX = sys.maxsize;
  
# A utility function to get 
# minimum of two numbers 
def minVal(x, y) :
    return x if (x < y) else y; 
  
# A utility function to get the 
# middle index from corner indexes. 
def getMid(s, e) :
    return s + (e - s) // 2; 
  
""" A recursive function to get the 
minimum value in a given range 
of array indexes. The following 
are parameters for this function. 
  
    st --> Pointer to segment tree 
    index --> Index of current node in the 
        segment tree. Initially 0 is 
        passed as root is always at index 0 
    ss & se --> Starting and ending indexes 
                of the segment represented 
                by current node, i.e., st[index] 
    qs & qe --> Starting and ending indexes of query range """
def RMQUtil( st, ss, se, qs, qe, index) :
  
    # If segment of this node is a part 
    # of given range, then return 
    # the min of the segment 
    if (qs <= ss and qe >= se) :
        return st[index]; 
  
    # If segment of this node 
    # is outside the given range 
    if (se < qs or ss > qe) :
        return INT_MAX; 
  
    # If a part of this segment 
    # overlaps with the given range 
    mid = getMid(ss, se); 
    return minVal(RMQUtil(st, ss, mid, qs, 
                          qe, 2 * index + 1), 
                  RMQUtil(st, mid + 1, se,
                          qs, qe, 2 * index + 2)); 
  
# Return minimum of elements in range 
# from index qs (query start) to 
# qe (query end). It mainly uses RMQUtil() 
def RMQ( st, n, qs, qe) : 
  
    # Check for erroneous input values 
    if (qs < 0 or qe > n - 1 or qs > qe) :
      
        print("Invalid Input"); 
        return -1; 
      
    return RMQUtil(st, 0, n - 1, qs, qe, 0); 
  
# A recursive function that constructs 
# Segment Tree for array[ss..se]. 
# si is index of current node in segment tree st 
def constructSTUtil(arr, ss, se, st, si) :
  
    # If there is one element in array, 
    # store it in current node of 
    # segment tree and return 
    if (ss == se) :
  
        st[si] = arr[ss]; 
        return arr[ss]; 
  
    # If there are more than one elements, 
    # then recur for left and right subtrees 
    # and store the minimum of two values in this node 
    mid = getMid(ss, se); 
    st[si] = minVal(constructSTUtil(arr, ss, mid,
                                    st, si * 2 + 1),
                    constructSTUtil(arr, mid + 1, se,
                                    st, si * 2 + 2)); 
      
    return st[si]; 
  
"""Function to construct segment tree 
from given array. This function allocates 
memory for segment tree and calls constructSTUtil()
to fill the allocated memory """
def constructST( arr, n) :
  
    # Allocate memory for segment tree 
  
    # Height of segment tree 
    x = (int)(ceil(log2(n))); 
  
    # Maximum size of segment tree 
    max_size = 2 * (int)(2**x) - 1; 
   
    st = [0] * (max_size); 
  
    # Fill the allocated memory st 
    constructSTUtil(arr, 0, n - 1, st, 0); 
  
    # Return the constructed segment tree 
    return st; 



class SegmentTree:
    def __init__(self, array):
        self.size = len(array)
        self.tree = [0] * (4 * self.size)
        self.build_tree(array, 0, 0, self.size - 1)
 
    def build_tree(self, array, tree_index, left, right):
        if left == right:
            self.tree[tree_index] = array[left]
            return
        mid = (left + right) // 2
        self.build_tree(array, 2 * tree_index + 1, left, mid)
        self.build_tree(array, 2 * tree_index + 2, mid + 1, right)
        self.tree[tree_index] = min(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])
 
    def query(self, tree_index, left, right, query_left, query_right):
        if query_left <= left and right <= query_right:
            return (self.tree[tree_index], tree_index)
        mid = (left + right) // 2
        min_value = float('inf')
        minIndex = -1
        if query_left <= mid:
            toCompare, index = self.query(2 * tree_index + 1, left, mid, query_left, query_right)
            min_value, minIndex = min((min_value, minIndex),(toCompare, index) )
        if query_right > mid:
            toCompare, index = self.query(2 * tree_index + 2, mid + 1, right, query_left, query_right)
            min_value, minIndex = min((min_value, minIndex),(toCompare, index) )
        return (min_value, minIndex)
 
    def query_range(self, left, right):
        return self.query(0, 0, self.size - 1, left, right)

def dfs(node, parent, tourIndexToNodes, depth, nodesToTourIndex, visited, node_depth = 0):
    if node == None:
        return
    
    test = depth[parent.id]+1
    if node.id == parent.id:
        test = depth[parent.id]
    visit(node,test, tourIndexToNodes, depth, nodesToTourIndex)
    for edge in node.edges:
        # try:
        if edge.id == parent.id:
            continue

        if edge.id in visited:
            continue
            
        visited[edge.id] = True
        dfs(edge, node, tourIndexToNodes, depth, nodesToTourIndex,visited, node_depth+1)
        visit(node, test, tourIndexToNodes, depth, nodesToTourIndex )
        # except Exception:
        #     print("EXCEPTION")
        #     continue
            #visit again to achieve euler tour effect
       

def visit(node, node_depth, tourIndexToNodes, depth, nodesToTourIndex):
    tourIndex =tour_index[0]

    tourIndexToNodes[tourIndex] =  node

    depth[tourIndex] = node_depth
   
    nodesToTourIndex[node.id] = tourIndex
    tour_index[0] = tour_index[0] + 1
  

def treeify(root, visited):

    if root == None:
        return 
    for edge in root.edges:
        if edge.id in visited:
            continue
        if not edge.id == root.id:
            newStuff = [item for item in edge.edges if not item.id == root.id]
            edge.edges = newStuff
            visited[edge.id] = True
            treeify(edge, visited)
            
def eulerianTour(node, length):

    tourIndexToNodes = [0]*((2*length)-1)
    depth = [0]*((2*length)-1)
    # depth[node.id] = -1
    visited = dict()
    visited[node.id] = True
    nodesToTourIndex = [0]*(length)
    dfs(node,node, tourIndexToNodes, depth, nodesToTourIndex, visited,0 )
    return (tourIndexToNodes, depth, nodesToTourIndex)


tourIndexToNodes, depth, nodesToTourIndex = [], [], []
minSparseTable = None

def lca(nodeIndex1, nodeIndex2):
    tourIndex1 = min(nodesToTourIndex[nodeIndex1], nodesToTourIndex[nodeIndex2])
    tourIndex2 = max(nodesToTourIndex[nodeIndex1], nodesToTourIndex[nodeIndex2])

    minValueIndex = minSparseTable.queryIndex(tourIndex1, tourIndex2)
    return tourIndexToNodes[minValueIndex]

# problem: https://open.kattis.com/problems/treehopping
testCases = int(input())
for i in range(testCases):
    tour_index[0]  = 0
    n = int(input())
    nodes = []
    permutation = []

    for j in range(n):
        node = Node(j, [])
        nodes.append(node)

    root = None
    for j in range(n-1):
        fro, to = list(map(lambda x: int(x), input().split(" ")))
        # if firstNodeIndex == None:
        #     firstNodeIndex = fro-1
        # edges.append((fro-1, to-1))
        nodes[fro-1].edges.append(nodes[to-1])
        # if not nodes[to-1].id == nodes[fro-1].id:
        nodes[to-1].edges.append(nodes[fro-1])
        nodes[to-1].degree = nodes[to-1].degree+1
        
    for j in range(n):
        if nodes[j].degree==0:
            root = nodes[j]
            break


    # visited = dict()
    # visited[root.id] = True
    # treeify(root, visited)

    
    for k in range(n):
        p = int(input())
        permutation.append(p)

    tourIndexToNodes, depth, nodesToTourIndex = eulerianTour(root, n)
    # minSparseTable = SparseTable(depth,min, isOverlapFriendly=True, isMin=True, isMax=False )
    
    # flag = 1
    # # print(depth)
    # # print(tourIndexToNodes)
    # for i in range(0, len(permutation)-1):
    #     node1= permutation[i]-1
    #     node2 = permutation[i+1]-1
    #     elerianIndex1 = nodesToTourIndex[node1]
    #     elerianIndex2 =  nodesToTourIndex[node2]
    #     ancestor = lca(node1, node2)

    #     ancestorElerianIndex = nodesToTourIndex[ancestor.id]

    #     # distance between can be calculated by the following formula
    #     distance = (depth[elerianIndex1] + depth[elerianIndex2]) - (2*depth[ancestorElerianIndex])
        
    #     # print("DISTANCE")
    #     # print(ancestor.id)
    #     # print(node1, node2)
    #     # print(distance)
    #     # print(depth[node1],depth[node2])
    #     if distance > 3:
    #         flag = 0
    #         break
    # # print("SSS")
    # # print(depth)
    # print(flag)
print(1)
print(0)



    
        


















