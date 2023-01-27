import os
import concurrent.futures
import itertools
from more_itertools import grouper
import numpy as np
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


###########################################################################################################

def convert_image(pic):
    imagename = pic.split("\\")[-1]
    imagename = imagename.replace(".jpg",".png")

    im = cv2.imread(pic)
    hsv = cv2.cvtColor(im,cv2.COLOR_RGB2HSV)
    black_lower =np.array([0, 0, 0])
    black_upper = np.array([350,55,100])

    white_lower =np.array([0,0,178], dtype=np.uint8)
    white_upper =np.array([0,5,255], dtype=np.uint8)

    red_lower = np.array([0, 50, 50],np.uint8)
    red_upper = np.array([60, 255, 255],np.uint8)

    yellow_lower = np.array([61, 50, 50],np.uint8)
    yellow_upper = np.array([120, 255, 255],np.uint8)

    green_lower = np.array([121, 50, 50],np.uint8)
    green_upper = np.array([180, 255, 255],np.uint8)

    cyan_lower =np.array([181, 50, 50],np.uint8)
    cyan_upper =np.array([240, 255, 255],np.uint8)

    blue_lower =np.array([241, 50, 50],np.uint8)
    blue_upper =np.array([300, 255, 255],np.uint8)

    magenta_lower =np.array([301, 50, 50],np.uint8)
    magenta_upper =np.array([360, 255, 255],np.uint8)


    black_mask = cv2.inRange(hsv, black_lower, black_upper)
    white_mask = cv2.inRange(hsv, white_lower, white_upper)
    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)
    cyan_mask = cv2.inRange(hsv, cyan_lower, cyan_upper)
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
    magenta_mask = cv2.inRange(hsv, magenta_lower, magenta_upper)

    im[black_mask != 0] = [118,0,0]
    im[white_mask != 0] = [157,238,222]
    im[red_mask != 0] = [141,48,39]
    im[yellow_mask != 0] = [170,210,107]
    im[green_mask != 0] = [119,187,30]
    im[cyan_mask != 0] = [125,50,200]
    im[blue_mask != 0] = [94,91,197]
    im[magenta_mask != 0] = [174,42,117]
    cv2.imwrite(f'{out}\\{imagename}', im)

###########################################################################################################

def main(List):
    for file in List:
        print(f'CONVERTING: {file}')
        convert_image(file)  
        print(f'Saved Image {file}')


def execute():
    items = get_files()
    executor = concurrent.futures.ProcessPoolExecutor(10)
    groups = grouper(5, items, fillvalue=None)
    futures = [executor.submit(main, group) for group in groups]
    return concurrent.futures.wait(futures, timeout=None)

def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)


if __name__ == "__main__":
    execute()


'''
as long as we can add in puts into await nearest()
'''