#BOWSER PIPE

nPipes = int(input())
pipes = map(lambda x: int(x), input())
nPipesToEnter = int(input())
pipesToEnter = map(lambda x: int(x), input())


pipeToDestination = dict()
destinationToPipes = dict()


for i in range(len(nPipes)):
    pipe = pipes[i]
    coinRoomId = 0
    if pipe == -1:
        pipeToDestination[i] = (pipe, coinRoomId)

        if  destinationToPipes[(pipe, coinRoomId)] is None:
            destinationToPipes[(pipe, coinRoomId)] = []
        
        destinationToPipes[(pipe, coinRoomId)].append(i)
    
        coinRoomId = coinRoomId+1

    else:    
        if  destinationToPipes[(pipe, i)] is None:
            destinationToPipes[(pipe, i)] = []

        pipeToDestination[(pipe, i)].append(i)






def traversePipe(start):
    current = start
    steps = 0
    lastPipeEntered = start
    while not current == -1:
        destination, id = pipeToDestination[current] 
        current = destination
        step = step + 1
        lastPipeEntered = current

    return (steps,lastPipeEntered)



for i in range(len(nPipesToEnter)):
    pipeToEnter = pipesToEnter[i]
