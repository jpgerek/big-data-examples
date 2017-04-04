from mredu import simul
import random

M = 3
START_VALUE = 1
VALUES_NUM  = 10

data = [ (x, random.randint(0, 100)) for x in range(START_VALUE, VALUES_NUM+START_VALUE) ]

print("data\n", data)

def mapper(sequence_num, value):
    return [(x, value) for x in range(sequence_num, min(sequence_num+M, VALUES_NUM+START_VALUE))]

def reducer(sequence_num, moving_avg_values):
    return sequence_num, sum(moving_avg_values)/M

result_mapred = simul.map_red(data, mapper, reducer)

print('')

print("result_mapred")

for item in result_mapred:
    print("\t", item)
