from mredu import simul
import random

GRID_SIZE = 5

data = [ (x, (random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE))) for x in range(1, GRID_SIZE*2) ]


print("data\n", data)

def mapper1(neighbor, coords):
    x, y = coords
    result = [(coords, neighbor)]
    if x > 1:
        # left
        result.append(((x-1, y), neighbor))
        # top left
        if y > 1:
            result.append(((x-1, y-1), neighbor))
    if x < GRID_SIZE:
        # right
        result.append(((x+1, y), neighbor))
        if y < GRID_SIZE:
            # bottom right
            result.append(((x+1, y+1), neighbor))
    if y > 1:
        # top
        result.append(((x, y-1), neighbor))
        if  x < GRID_SIZE:
            # top right
            result.append(((x+1, y-1), neighbor))
    if y < GRID_SIZE:
        # bottom
        result.append(((x, y+1), neighbor))
        if x > 1:
            # bottom left
            result.append(((x-1, y+1), neighbor))
   
        
    return result

def reducer1(coords, neighborsList):
    return coords, neighborsList

result_mapred1 = simul.map_red(data, mapper1, reducer1)

print("result_mapred1")

for item in result_mapred1:
    print("\t", item)

def mapper2(coords, neighborsList):
    result = []

    for x, neighbor1 in enumerate(neighborsList):
        for neighbor2 in neighborsList[x:]:
           result.append(((neighbor1, neighbor2), 1))

    return result

def reducer2(neighborsPair, _):
    return neighborsPair, None

result_mapred2 = simul.map_red(data, mapper2, reducer2)

print("result_mapred1")

for item in result_mapred2:
    print("\t", item)
