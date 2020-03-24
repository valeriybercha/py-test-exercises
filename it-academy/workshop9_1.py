# TASK 1
import math
def distance(x1, x2, y1, y2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d
print(distance(2, 4, 5, 6))

distance(4, 5, 8, 9)

# TASK 2
def pyramidVolume(height, baseLength):
    baseArea = baseLength * baseLength
    return height * baseArea / 3
print("Volume:", pyramidVolume(146, 55000))