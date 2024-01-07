from queue import PriorityQueue


def solve(n,k, time):
    remaining = n
    time.sort()
   
    q = PriorityQueue()
    for i in range(0,min(n,k)):
        q.put((time[i], i))

    used =[0]*k
    ans =0 
    while remaining > 0 :
        t, car = q.get()
        ans = t
        if used[car] == 0:
            remaining = remaining-5
        else:
            remaining = remaining-4
        
        used[car] = used[car]+1
        #need to use the original value
        q.put((time[car]+(2*used[car]*time[car]),car))

    return ans

    




n,k = map(int, input().split(" "))
time = []
for i in range(n):
    time.append(int(input()))

print(solve(n,k, time))