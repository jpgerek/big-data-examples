from mredu import simul
from math import floor, ceil

BARS_NUM = 5

data = [ (x, None) for x in list(range(5)) + list(range(4, 5)) + list(range(0, 3)) ]

print("input data set:\n", data)

def mapper1(number, _):
    return ('all', number)

result_mapper1 = list(simul.process_mapper(data, mapper1))

print('')

print("result_mapper1:\n", sorted(result_mapper1))

def reducer1(k, numbersList):
    return 'max-min', (min(numbersList), max(numbersList))

result_reducer1 = list(simul.map_red(data, mapper1, reducer1))


print("result_reducer1:\n", result_reducer1)

print('')

MIN, MAX = result_reducer1[0][1]
DELTA = MAX - MIN

def mapper2(number, _):
    column_size = DELTA/BARS_NUM
    column = BARS_NUM - 1 if number == MAX else floor( (number-MIN) / column_size )
    range_from = number - number%column_size
    range_to = range_from + column_size
    return (column+1, (range_from, range_to)), 1

def reducer2(column_and_range, vList):
    return column_and_range, sum(vList)

result_reducer2 = list(simul.map_red(data, mapper2, reducer2))

print("result_reducer2:\n", result_reducer2)

print('')

for (column, (range_from, range_to)), count in result_reducer2:
    print("column {}, range({}, {}): {}".format(column, range_from, range_to, count))
