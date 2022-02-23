import os
import asyncio
from datetime import datetime
from distutils.command.upload import upload
from tkinter.ttk import Style
from PIL  import Image
from convertAI import convert
from tkinter import *


in1 = "C:\\Users\\jojop\\Desktop\\AI Convert\\INPUT"
out = "C:\\Users\\jojop\\Desktop\\AI Convert\\OUTPUT"
in2 = "C:\\Users\\jojop\\Desktop\\AI Convert\\IN\\"
out2 = "C:\\Users\\jojop\\Desktop\\AI Convert\\OUT\\"

fileList = []

#Loops through 
for root, dirs, files in os.walk(os.path.abspath(in1)):
    for file in files:
        fileList.append(os.path.join(root, file)) #Appends all of the files into the fileList list.
fileList.sort(key = lambda x: os.path.getmtime(x)) #Sorts the fileList based on the time it was added to the new folder.

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
def nearest(a,b2,c):
    scalarList = []
    for i , color in enumerate(colors):
        (r,g,b) = color
        x = a - r
        y = b2 - g
        z = c - b
        scalar = (((x**2) + (y**2) + (z**2)) **.5)  #FIX THIS
        scalarList.append((scalar, i))
    # scalarList = set(scalarList)
    # nearest = sorted(scalarList)[0]
    # firstNearestColor = colors[nearest[1]]                                                REFACTORING
    nearest = sorted(set(scalarList))[0]
    firstNearestColor = colors[nearest[1]]
    return firstNearestColor

###########################################################################################################
def convert_image(pic, imagename):
    im = Image.open(pic)
    img = im.load()
    imdata = []
    [xs,ys] = im.size  
    for x in range(0, xs):
        for y in range(0, ys):
            try:
                [r,g,b,Fuck] = img[x,y]
            except ValueError:
                [r,g,b] = img[x,y]
            [i,j,k] = nearest(r,g,b) #need to await this somehow... asyncio.run() cannot be called from a running event loop -> error
            value = (i,j,k)
            imdata.append(value)
            im.putpixel((x, y), value)
    im.save(f'{out}\\{imagename}.png')

###########################################################################################################
for i, file in enumerate(fileList):
        convert_image(file, i)  #you cant await this one it will wait until complete
        print(f'Saved Image {i}')



'''
as long as we can add in puts into await nearest()
'''