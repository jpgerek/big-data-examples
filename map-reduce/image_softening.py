from mredu import simul
import random

IMAGE_WIDTH = 9
IMAGE_HEIGHT = 9
data = [ ( (x, y), (random.randint(0,255), random.randint(0, 255), random.randint(0, 255)) ) for x in range(IMAGE_WIDTH) for y in range(IMAGE_HEIGHT) ]

for pixel in data:
    print(pixel)


def mapper(point, rgb):
    x, y = point
    left_x = max(0, x-1)
    top_y = max(0, y-1)
    right_x = min(IMAGE_WIDTH, x+1)
    bottom_y = min(IMAGE_HEIGHT, y+1)

    result = []
    for current_x in range(left_x, right_x+1):
        for current_y in range(top_y, bottom_y+1):
            result.append(((current_x, current_y), rgb))

    return result

def reducer(point, rgbList):
    pointsNum = len(rgbList)

    avgR = sum(map(lambda item: item[0], rgbList)) / pointsNum
    avgG = sum(map(lambda item: item[1], rgbList)) / pointsNum
    avgB = sum(map(lambda item: item[2], rgbList)) / pointsNum

    return (point, (avgR, avgG, avgB))

result_mapred = list(simul.map_red(data, mapper, reducer))

print("result_mapred\n")

for point, rgb in result_mapred:
    print(point, rgb)
