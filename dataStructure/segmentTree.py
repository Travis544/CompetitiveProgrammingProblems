# Python3 program to show segment tree operations like
# construction, query and update
from math import ceil, log2

# A utility function to get the
# middle index from corner indexes.


def getMid(s, e):
	return s + (e - s) // 2


""" A recursive function to get the sum of values
	in the given range of the array. The following
	are parameters for this function.

	st --> Pointer to segment tree
	si --> Index of current node in the segment tree.
		Initially 0 is passed as root is always at index 0
	ss & se --> Starting and ending indexes of the segment
				represented by current node, i.e., st[si]
	qs & qe --> Starting and ending indexes of query range """


def getSumUtil(st, ss, se, qs, qe, si):

	# If segment of this node is a part of given range,
	# then return the sum of the segment
	if (qs <= ss and qe >= se):
		return st[si]

	# If segment of this node is outside the given range
	if (se < qs or ss > qe):
		return 0

	# If a part of this segment overlaps with the given range
	mid = getMid(ss, se)

	return (getSumUtil(st, ss, mid, qs, qe, 2 * si + 1) +
		getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2))


""" A recursive function to update the nodes
which have the given index in their range.
The following are parameters st, si, ss and se
are same as getSumUtil()
i --> index of the element to be updated.
	This index is in the input array.
diff --> Value to be added to all nodes
which have i in range """


def updateValueUtil(st, ss, se, i, diff, si):

    # Base Case: If the input index lies
    # outside the range of this segment
    if (i < ss or i > se):
        return
    # If the input index is in range of this node,
    # then update the value of the node and its children
  
    # all the parent of the particular leave node we are updating will increase by this diff
    st[si] = st[si] + diff
    if (se != ss):
        mid = getMid(ss, se)
        updateValueUtil(st, ss, mid, i,
                        diff, 2 * si + 1)
        updateValueUtil(st, mid + 1, se, i,
                        diff, 2 * si + 2)

# The function to update a value in input array
# and segment tree. It uses updateValueUtil()
# to update the value in segment tree


def updateValue(arr, st, n, i, new_val):

    # # Check for erroneous input index
    # if (i < 0 or i > n - 1) :
    # 	print("Invalid Input", end = "")
    # 	return

    # Get the difference between
    # new value and old value
    diff = new_val - arr[i]
    # Update the value in array
    print("AT")
  
    arr[i] = new_val
    print(arr)
    # Update the values of nodes in segment tree
    updateValueUtil(st, 0, n - 1, i, diff, 0)

# Return sum of elements in range from
# index qs (query start) to qe (query end).
# It mainly uses getSumUtil()


def getSum(st, n, qs, qe):

	# Check for erroneous input values
	if (qs < 0 or qe > n - 1 or qs > qe):

		print("Invalid Input", end="")
		return -1

	return getSumUtil(st, 0, n - 1, qs, qe, 0)

# A recursive function that constructs
# Segment Tree for array[ss..se].
# si is index of current node in segment tree st


def constructSTUtil(arr, ss, se, st, si):

	# If there is one element in array,
	# store it in current node of
	# segment tree and return
	if (ss == se):

		st[si] = arr[ss]
		return arr[ss]

	# If there are more than one elements,
	# then recur for left and right subtrees
	# and store the sum of values in this node
	mid = getMid(ss, se)

	st[si] = (constructSTUtil(arr, ss, mid, st, si * 2 + 1) +
			constructSTUtil(arr, mid + 1, se, st, si * 2 + 2))

	return st[si]


""" Function to construct segment tree
from given array. This function allocates memory
for segment tree and calls constructSTUtil() to
fill the allocated memory """
def constructST(arr, n):

	# Allocate memory for the segment tree
	# Height of segment tree
	x = (int)(ceil(log2(n)))
	# Maximum size of segment tree
	max_size = 2 * (int)(2**x) - 1
	# Allocate memory
	st = [0] * max_size
	# Fill the allocated memory st
	constructSTUtil(arr, 0, n - 1, st, 0)
	# Return the constructed segment tree
	return st



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
        print("TREE")
        print(self.indexTree)
        return self.query(0, 0, self.size - 1, left, right)
        
# Driver Code
if __name__ == "__main__":

    arr = [1, 3, 5, 7, 9, 11]
    seg = SegmentTree(arr)
    print(seg.query_range(3,5))
    # n = len(arr)

    # # Build segment tree from given array
    # st = constructST(arr, n)

    # # Print sum of values in array from index 1 to 3

    # print("Sum of values in given range = ",
    #                 getSum(st, n, 2, 3))

    # # Update: set arr[1] = 10 and update
    # # corresponding segment tree nodes
    # # print(st)
    # updateValue(arr, st, n, 1, 10)
    # # print(st)
    # # Find sum after the value is updated
    # print("Updated sum of values in given range = ",getSum(st, n, 1, 3), end = "")
