from mredu import simul

data = [
        ('josé',  'maría'), ('josé',  'isabel'), ('josé',  'francisco'), ('josé',  'juan'),
        ('maría', 'ana'  ), ('maría', 'juan'  ), ('maría', 'francisco'), ('maría', 'marta'),
        ('juan',  'josé'), ('juan',  'sergio'), ('juan',  'francisco'), ('juan',  'leticia'),
        ('francisco', 'maría'), ('francisco', 'juan')
       ]


def mapper(user, friend):
    key = sorted((user, friend))
    return tuple(key), 1 

def reducer(friendship, linksAmount):
    if sum(linksAmount) < 2:
        return None
    return friendship, None

result_mapred = list(simul.map_red(data, mapper, reducer))

print("result_mapred:")

for item in result_mapred:
    print("\t", item)

"""
output:

result_mapred:
         (('josé', 'juan'), None)
         (('francisco', 'maría'), None)
         (('francisco', 'juan'), None)
"""
