import cv2
import os

fileList = []
####################################
def convert(filePath, videoPathYep):
  vidcap = cv2.VideoCapture(videoPathYep)
  success, image = vidcap.read()
  count = 0
  newPath = f"{filePath}\\Frames"
  if not os.path.exists(newPath):
    os.makedirs(newPath)
  
  while success:
    cv2.imwrite(os.path.join(newPath, "%d.jpg") % count, image) # save frame as JPEG file      
    success , image = vidcap.read()
    print('Read a new frame: ', success, count)
    count += 1

#######################
def videofps(filepath):
    cap = cv2.VideoCapture(filepath)
    framespersecond = int(cap.get(cv2.CAP_PROP_FPS))
    print("The total number of frames in this video is ", framespersecond)
    return framespersecond

  


