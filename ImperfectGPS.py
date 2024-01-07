# Imperfect GPS
# Lots of runners use personal Global Positioning System (GPS) receivers to track how many miles they run. No GPS is perfect, though: it only records its position periodically rather than continuously, so it can miss parts of the true running path. For this problem we’ll consider a GPS that works in the following way when tracking a run:
# At the beginning of the run, the GPS first records the runner’s starting position at time 0.
# It then records the position every t units of time.
# It always records the position at the end of the run, even if the total running time is not a multiple of t.
# The GPS assumes that the runner goes in a straight line between each consecutive pair of recorded positions. Because of this, a GPS can underestimate the total distance run.
# For example, suppose someone runs in straight lines and at constant speed between the positions on the left side of Table 1. The time they reach each position is shown next to the position. They stopped running at time 11. If the GPS records a position every 2 units of time, its readings would be the records on the right side of Table 1.

# Given a sequence of positions and times for a running path, as well as the GPS recording time interval t, calculate the percentage of the total run distance that is lost by the GPS. Your computations should assume that the runner goes at a constant speed in a straight line between consecutive positions.
#Output the percentage of the actual run distance that is lost by the GPS. 
n, t = map(int, input().split(' '))
positions = [list(map(int, input().split(' '))) for i in range(n)]
gpsPositions = [ positions[0] ]
maxT = positions[-1][2]

actualTIndex=1
prevActualT=0
currT=t


# Calculate GPS positions from actual positions. 
while currT<maxT:
    # time
    actualT=positions[actualTIndex][2]
    # find the interval for the current gps time which inscrease by t each time.
    while currT>actualT:
        actualTIndex+=1
        prevActualT=actualT
        actualT=positions[actualTIndex][2]
        
    # calculate delta, the percentage of actual time interval the gps picked up. 
    # then multiply that to respective x and y difference of the actual time---
    delta=(currT-prevActualT)/(actualT-prevActualT)
    currX, currY,_=positions[actualTIndex]
    pX, pY,_=positions[actualTIndex-1]
    gpsPositions.append(
        [(currX-pX)*delta,
         (currY-pY)*delta,
         currT
        ]
    
    )
    
    
    xOff, yOff, _ = positions[actualTIndex - 1]
    # Start from the current interval start position (xOff, yOff), 
    # add respective x and y from thedifference of actual time * delta
    gpsPositions[-1][0] += xOff
    gpsPositions[-1][1] += yOff
    
    currT+=t
    
gpsPositions.append(positions[-1])

def calculateDistance(position):
    distance=0
    for i in range(1, len(position)):
        prevX, prevY, time=position[i-1]
        x,y,time=position[i]
        distance+=((x-prevX)**2+(y-prevY)**2)**0.5
    return distance

normal=calculateDistance(positions)
gps=calculateDistance(gpsPositions)
print(str((1-(gps/normal))*100))
    
    
   