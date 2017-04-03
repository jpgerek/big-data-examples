from mredu import simul

data = [
        ('josé',  'maría'), ('josé',  'isabel'), ('josé',  'francisco'), ('josé',  'juan'),
        ('maría', 'ana'  ), ('maría', 'juan'  ), ('maría', 'francisco'), ('maría', 'marta'),
        ('juan',  'jorge'), ('juan',  'sergio'), ('juan',  'francisco'), ('juan',  'leticia')
       ]


def mapper1(user, friend):
    return [
            (user, friend),
            (friend, user)
           ]

def reducer1(user, friendsList):
    result = []
    for friend in friendsList:
        key = tuple(sorted((friend, user)))
        result.append((key, friendsList))
    return result

result_mapred1 = list(simul.map_red(data, mapper1, reducer1))

print("result_mapred1:\n")
for item in result_mapred1:
    print ("\t", item)

def mapper2(friendship, friendsList):
    return friendship, friendsList

# friendshipFriendsList is two lists with the friends list of each one
# notice too many friends wouldn't scale well
def reducer2(friendship, friendshipFriendsList):
    friendsList1, friendsList2 = friendshipFriendsList
    commonFriends = list(set(friendsList1).intersection(friendsList2))
    return friendship, commonFriends

result_mapred2 = list(simul.map_red(result_mapred1, mapper2, reducer2))

print("result_mapred2:\n")
for item in result_mapred2:
    print("\t", item)
