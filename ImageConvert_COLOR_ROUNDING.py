import os
import concurrent.futures
import itertools
from more_itertools import grouper
import cv2

in1 = ".\images"
out = ".\in"
def get_files():
    fileList = []
    for root, dirs, files in os.walk(os.path.abspath(in1)):
        for file in files:
            fileList.append(os.path.join(root, file)) #Appends all of the files into the fileList list.
    fileList.sort(key = lambda x: os.path.getmtime(x)) #Sorts the fileList based on the time it was added to the new folder.
    return fileList

#List of colors found on the Nvidia Canvas program
colors = [(123, 200, 0), (147, 100, 200), (135, 113, 111), (168, 200, 50),
    (125, 48, 84), (177, 200, 255), (139, 48, 39), (150, 0, 177),
    (96, 110, 50), (124, 50, 200), (181, 123, 0), (162, 163, 235),
    (158, 158, 170), (118, 0, 0), (94, 91, 197), (170, 209, 106),
    (176, 193, 195), (143, 42, 145), (127, 69, 2), (148, 110, 40),
    (110, 110, 40), (156, 238, 221), (154, 198, 218), (134, 150, 100),
    (174, 41, 116), (161, 161, 100), (105, 105, 105), (112, 100, 25),
    (153, 153, 0), (119, 186, 29), (126, 200, 100)]

###########################################################################################################
#Finds the shortest scalar and gives us the color that is the closest to the colors above.
@jit
def nearest(a,b2,c):
    scalarList = []
    for i , color in enumerate(colors):
        (r,g,b) = color
        x = a - r
        y = b2 - g
        z = c - b
        scalar = ((x**2) + (y**2) + (z**2))
        scalarList.append((scalar, i))
    nearest = sorted(set(scalarList))[0]
    firstNearestColor = colors[nearest[1]]
    return firstNearestColor
###########################################################################################################

def convert_image(pic):
    img=cv2.imread(pic)
    height, width, channels = img.shape
    for x in range(0,width):
        for y in range(0,height):
            a,b2,c = img[y,x]
            img[y,x] = list(nearest(a,b2,c))
    imagename = pic.split("\\")[-1]
    imagename = imagename.replace(".jpg",".png")
    cv2.imwrite(out+"\\" + imagename, img)

###########################################################################################################

def main(List):
    for file in List:
        print(f'CONVERTING: {file}')
        convert_image(file)  
        print(f'Saved Image {file}')

def execute():
    items = get_files()
    main(items)
	# executor = concurrent.futures.ProcessPoolExecutor(5)
	# futures = [executor.submit(main, group) for group in grouper(5, items)]
	# return concurrent.futures.wait(futures,timeout=None)


if __name__ == "__main__":
    execute()


