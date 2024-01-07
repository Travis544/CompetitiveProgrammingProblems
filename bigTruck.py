
#Big Truck
# Your boss has hired you to drive a big truck, transporting items between two locations in a city. 
# You’re given a description of the city, with locations of interest and the lengths of roads between them. 
# Your boss requires that you take a shortest path between the starting and ending location, 
# and she’ll check your odometer when you’re done to make sure you didn’t take any unnecessary side trips. 
# However, your friends know you have plenty of unused space in the truck,
# and they have asked you to stop by several locations in town, to pick up items for them. 
# You’re happy to do this for them. You may not be able to visit every location to pick up everything 
# your friends want, but you’d like to pick up as many 
# items as possible on your trip, as long as it doesn’t make the path any longer than necessary.

# The first line of input contains an integer, n (2≤n≤100), giving the number of locations in the city.
# Locations are numbered from 1 to n, with location 1 being the starting location and n being the destination. 

# The next input line gives a sequence of n integers, 
# t1…tn, where each ti indicates the number of items your friends have asked you to pick up from location i.
# The next input line contains a non-negative integer, m, giving the number of roads in the city
# three integers, abd. This indicates that there is a road of length d between location a and location b.


# output
# If it’s not possible to travel from location 1 to location n, 
# just output out the word “impossible”. Otherwise, output the length of a 
# shortest path from location 1 to location n,
# followed by the maximum number of items you can pick up along the way.
    
    
# recurrence relation:
# let dijk be the min distance between i and j with k intermediates
# dijk=min(dij(k-1), dik(k-1)+dkj(k-1))
def initialize(dp, m, items):
    # print(m)
    for i in range(len(m)):
        for j in range(len(m)):
            if i==j:
                
                dp[i][j]=(0, items[i])
                
            elif m[i][j]!=0:
                dp[i][j]=(m[i][j], items[i]+items[j])
            else:
                dp[i][j]=(float('inf'), 0)

                                
def floyd_warshall(dp,m, items):
    initialize(dp, m, items)
    
    for k in range(len(m)):
        for i in range(len(m)):
            for j in range(len(m)):
                # if with current intermeidate k we can arrive with less distance, use that
                if dp[i][k][0]+dp[k][j][0]<dp[i][j][0]:
                    val=(dp[i][k][1]+dp[k][j][1])-items[k]

                    newData=(dp[i][k][0]+dp[k][j][0], 
                                val
                            )
                    dp[i][j]=newData
                    
                    # if the current intermediate has same distance as the current distance without using the intermediate,
                    # but we can pick up more items, use that intermediate
                elif  dp[i][k][0]+dp[k][j][0]==dp[i][j][0]:
                    if  (dp[i][k][1]+dp[k][j][1])-items[k]>dp[i][j][1]:
                        
                        val=(dp[i][k][1]+dp[k][j][1])-items[k]
                    else:
                        val=dp[i][j][1]
                    
                    newData=(dp[i][k][0]+dp[k][j][0], 
                                val
                            )
                    dp[i][j]=newData    
                    
                    
                
numLocation=int(input())
items=list(map (int, input().split(' ')))
roads=int(input())
matrix=[]
for i in range(numLocation):
    matrix.append([0]*numLocation)

for i in range(roads):
     a,b,d=list(map (int, input().split(' ')))
     matrix[a-1][b-1]=d
     matrix[b-1][a-1]=d
     


dp=[]
for i in range(numLocation):
    dp.append([float('inf')]*numLocation)
    
floyd_warshall(dp ,matrix,items)

if dp[0][numLocation-1][0]==float('inf') or dp[0][numLocation-1][1]==0:
    print('impossible')
else:
    print(dp[0][numLocation-1][0], dp[0][numLocation-1][1])
 
