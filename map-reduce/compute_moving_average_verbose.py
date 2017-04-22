# STILL WIP
from mredu import simul
import random

M = 3
START_VALUE = 1
VALUES_NUM = 7

data = [ (x, random.randint(0, 100)) for x in range(START_VALUE, START_VALUE+VALUES_NUM) ]

print("data\n", data)

def mapper(sequence_num, value):
    from_seq_num = sequence_num - M
    to_seq_num   = min(VALUES_NUM, sequence_num + M)
    sequences_affected = [x for x in range(from_seq_num, to_seq_num)]

    left_pointer  = from_seq_num
    right_pointer = left_pointer + M

    result = []

    while right_pointer < to_seq_num:
        key = tuple(x for x in sequences_affected if max(START_VALUE, left_pointer) <= x < min(right_pointer, VALUES_NUM+START_VALUE-1))
        result.append((key, value))
        left_pointer  += 1
        right_pointer += 1
    
    return result

def reducer(sequences_affected, moving_avg_values):
    return {'seq_num': sequences_affected[-1], 'sequences_affetected': sequences_affected}, {'avg': sum(moving_avg_values)/M, 'nums-list': moving_avg_values}

result_mapred = simul.map_red(data, mapper, reducer)

print('')

print("result_mapred")

for item in result_mapred:
    print("\t", item)
