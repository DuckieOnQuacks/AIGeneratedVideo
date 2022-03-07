import cv2
import os


def frame(filePath):
  
  videoPath = f"{filePath}\\Oliver Tree - Cowboys Don't Cry [Music Video] (1).mp4"
  vidcap = cv2.VideoCapture(videoPath)
  success,image = vidcap.read()
  count = 0
  newPath = f"{filePath}\\Frames"
  if not os.path.exists(newPath):
    os.makedirs(newPath)
  
  while success:
    cv2.imwrite(os.path.join(newPath, "%d.jpg") % count, image) # save frame as JPEG file      
    success , image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
