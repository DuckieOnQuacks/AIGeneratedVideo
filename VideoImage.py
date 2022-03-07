import cv2
import os

def frame(filePath, videoPathYep):
  videoPath = videoPathYep
  vidcap = cv2.VideoCapture(videoPathYep)
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
  


