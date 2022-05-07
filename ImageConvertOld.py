import os
from PIL import Image
import concurrent.futures
from more_itertools import grouper

fileList = []

#List of colors found on the Nvidia Canvas program
colors = [(123, 200, 0),#grass
#(147, 100, 200),#river
#(135, 113, 111),#mud
(168, 200, 50),#tree
#(125, 48, 84),#Ground other
(177, 200, 255),#water
#(139, 48, 39),#pavement
#(150, 0, 177),#roof
#(96, 110, 50),#bush
(124, 50, 200),#Gravel
(181, 123, 0),#wood
#(162, 163, 235),#straw
(158, 158, 170),#snow
(118, 0, 0),#flower
#(94, 91, 197),#bridge
#(170, 209, 106),#wall brick
#(176, 193, 195),#wall wood
#(143, 42, 145),#platform
#(127, 69, 2),#house
#(148, 110, 40),#Road
(110, 110, 40),#dirt
(156, 238, 221),#sky
#(154, 198, 218),#sea
(134, 150, 100),#mountain
#(174, 41, 116),#Wall stone
#(161, 161, 100),#stone
(105, 105, 105),#clouds
#(112, 100, 25),#fence
(153, 153, 0),#sand
(119, 186, 29),#fog
(126, 200, 100),#hill
(149,100,50)]#rock

####################
#Finds the shortest scalar and gives us the color that is the closest to the colors above.
def nearest(a,b2,c):
    scalarList = []
    for i , color in enumerate(colors):
        (r,g,b) = color
        x = a - r
        y = b2 - g
        z = c - b
        scalar = (x**2) + (y**2) + (z**2)
        scalarList.append((scalar, i))
    nearest = sorted(set(scalarList))[0]
    firstNearestColor = colors[nearest[1]]
    return firstNearestColor
#################################
def convert_image(pic, filePath):
    im = Image.open(pic)
    img = im.load()
    [xs,ys] = im.size  
    for x in range(0, xs):
        for y in range(0, ys):
            try:
                [r,g,b,Fuck] = img[x,y]
            except ValueError:
                [r,g,b] = img[x,y]
            [i,j,k] = nearest(r,g,b) 
            value = (i,j,k)
            im.putpixel((x, y), value)
    imagename = pic.split("\\")[-1]
    newPath = f"{filePath}\\Processed"
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    im.save(f'{newPath}\\{imagename}.png')

#########################
def main(List, filePath):
    for file in List:
        print(f'CONVERTING: {file}')
        convert_image(file, filePath)
        print(f'Saved Image {file}')

###############################
def execute(fileList, filePath):
	executor = concurrent.futures.ProcessPoolExecutor(6)
	futures = [executor.submit(main, group) for group in grouper(5, fileList, filePath)]
	concurrent.futures.wait(futures)

if __name__ == "__main__":
    execute()