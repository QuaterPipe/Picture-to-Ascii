from PIL import Image
from sty import fg
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

nums = [0, 25, 51, 76, 102, 153, 178, 204, 255]

def findNearestVal(num):
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < num:
            lo = mid + 1
        elif nums[mid] > num:
            hi = mid
        else:
            return nums[mid]
    return nums[lo]

def getClosest(rgb):
    if rgb[0] == rgb[1] == rgb[2]:
        t = round(rgb[0] / 32) * 32
        return (t, t, t)
    return tuple([findNearestVal(val) for val in rgb])

def getBrightness(rgb):
    return sum([x**2 for x in rgb])**0.5
