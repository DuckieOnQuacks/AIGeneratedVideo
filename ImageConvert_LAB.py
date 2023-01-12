import os
from PIL import Image
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




###########################################################################################################

def convert_image(pic):
    imagename = pic.split("\\")[-1]
    imagename = imagename.replace(".jpg",".png")

    im = cv2.imread(pic)
    lab = cv2.cvtColor(im, cv2.COLOR_BGR2LAB)
    cv2.imwrite(f'{out}\\{imagename}', lab)

###########################################################################################################

def main(List):
    for file in List:
        print(f'CONVERTING: {file}')
        convert_image(file)  
        print(f'Saved Image {file}')





def execute():
	items = get_files()
	executor = concurrent.futures.ProcessPoolExecutor(5)
	futures = [executor.submit(main, group) for group in grouper(5, items)]
	return concurrent.futures.wait(futures,timeout=None)




if __name__ == "__main__":
    execute()


'''
as long as we can add in puts into await nearest()
'''