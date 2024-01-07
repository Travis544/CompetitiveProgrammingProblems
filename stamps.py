






c,q =list(map(int, input().split(" ")))
clusters=list(map(int,input().split(" ")))


    
def isImpossible(need):
    return bfs(need)
    


class ClusterState:
    def __init__(self, s,a):
        self.arr=a
        self.sum=s
    
def bfs(need):
    queue=[]
    # queue.add(clusters[0])
    # queue.add(clusters[len(clusters)-1])
    # initial = clusters.copy()
    # intital2=clusters.copy()
    first=clusters[0]
    last=clusters[len(clusters)-1]
    # initial.pop(0) 
    queue.append(ClusterState(last,clusters[:-1])) 
    queue.append(ClusterState(first,clusters[1:]))
   
    
    # clusters.pop(len(clusters)-1)
    while len(queue)>0:
        state=queue.pop()
       
        if state.sum==need:
            return True
        elif state.sum<need:
            arr1=state.arr
            if (len(state.arr)==0):
                if state.sum==need:
                    return True
                continue
           
            sum=state.sum+arr1[0]
            sum2=state.sum+arr1[len(arr1)-1]

            if sum==need or sum2==need:
                return True
            
            if sum<need:
                # /arr1.pop(0)
                # queue.append(ClusterState(sum, arr1))
                if (len(arr1[1:])>0):
                 queue.append(ClusterState(sum, arr1[1:]))
                # arr3.pop(len(arr3)-1)
                # queue.append(ClusterState(sumP, arr3)) 
            if sum2<need:
                if (len(arr1[:-1])>0):
                    queue.append(ClusterState(sum2, arr1[:-1]))
            
    return False
    
res=[]
sums=sum(clusters)

def fastSearch(need):
    total=0
    if clusters[0]+clusters[len(clusters)-1]==need:
        return True
    for i in range(len(clusters)):
        total+=clusters[i]
        
        if total> need:
            return False
        if total==need:
            return True
    
    
for i in range(q):
    query=int(input())
    if query==sums:
        res.append("Yes")
    
    elif query==0:
        res.append("Yes")
    elif fastSearch(query):
         res.append("Yes")
    else:
        val=isImpossible(query)
        if val:
            res.append("Yes")
        else:
            res.append("No")
        
        
for i in range(q):
    print(res[i])
