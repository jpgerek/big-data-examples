# -*- coding: utf-8 -*-
from mredu import simul
import re

data = list(simul.input_file('quijote.txt'))

def mapper(k, v):
	line = re.sub(r'[^a-záéíóúüñç\s]', '', v.lower()).strip()
	if line == '':
		return None
	return [(word, 1) for word in re.split(r' +', line)]

def reducer(k, vList):
    return (k, sum(vList))

result_map = list(simul.map_red(data, mapper, reducer))

print("top 50\n")

for item in sorted(result_map, key=lambda item: item[1], reverse=True)[:50]:
	print("\t", item)
