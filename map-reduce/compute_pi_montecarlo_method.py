from mredu import simul
import random
import math

POINT_TRIES = 100000

data = ( ((-1+random.random()*2, -1+random.random()*2), None) for _ in range(POINT_TRIES) )

def mapper(point, _):
    x, y = point
    dist = math.sqrt(x*x + y*y)
    if (dist<1):
        return (0, 1)
    return None

def reducer(_, countList):
    return 'points-inside', sum(countList)


result_mapred1 = simul.map_red(data, mapper, reducer)

_, points_inside = list(result_mapred1)[0]

print("Point tries: {}\nPoints inside: {}\n".format(POINT_TRIES, points_inside))

print("PI: {}\n".format(4*(points_inside/POINT_TRIES)))
