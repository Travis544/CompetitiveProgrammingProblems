# Generates sample data for mail based on number of addresses and destinations

import random

N = 10
num_destinations = 5
target_path_length = 1

nodes = [None] * N          # Value of node is the index of the next node
available = range(N)        # Node indexes currently available
destinations = []           # Indexes of destinations (-1 values in nodes)
delivery_addresses = []     # Indexes of sources

# Populate destinations and assign nodes destination values
random.shuffle(available)
for dest in range(num_destinations):
    d = available.pop()
    destinations.append(d)
    nodes[d] = -1

starting_points = destinations      # Contains destinations and a random point
                                    # in each path excluding the source
while len(available) != 0:
    rand_start = random.randrange(len(starting_points))
    prev = starting_points[rand_start]
    length = random.randint(1, min(target_path_length, len(available)))

    path = [prev]
    for i in range(length):
        new = available.pop();
        nodes[new] = prev
        if i != length - 1:     # Don't add the source
            path.append(new)
        prev = new

    delivery_addresses.append(new)
    rand_path = random.randrange(len(path))
    starting_points.append(path[rand_path])

# Print node count, node values, delivery address count, and delivery addresses
print N
for edge in nodes:
    print edge,
print
print len(delivery_addresses)
for address in delivery_addresses:
    print address,
