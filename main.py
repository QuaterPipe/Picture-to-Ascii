from PIL import Image
from sty import fg
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
  
density = "@JD%*P+Y$,x. "[::-1]
density = "@%#*•· "[::-1]
density ="@QB#NgWM8RDHdOKq9$6khEPXwmeZaoS2yjufF]}{tx1zv7lciL/\\|?*>r^;:_\"~,'.-` "[::-1]

path = input("Enter path: ")
image = Image.open(path).convert("RGB")
if image.size[0] > 100 or image.size[1] > 100:
    width, height = image.size
    aspect_ratio = height / width
    new_width = 50
    new_height = aspect_ratio * new_width
    image = image.resize((new_width, round(new_height)))
pxls = image.load()
    
maxbrt = getBrightness([255 for _ in pxls[0,0]]) # magnitude of vector (255, 255, 255)

strImg = ""
for i in range(image.size[1]):
    for j in range(image.size[0]):
        brt = getBrightness(pxls[j, i])
        avg = int((len(density) - 1) * brt / maxbrt )
        print(fg(*getClosest(pxls[j, i])), density[avg], end=' ', sep='')
    print()
print(strImg)
print(fg.white)
