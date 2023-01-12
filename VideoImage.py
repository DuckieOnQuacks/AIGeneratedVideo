from msilib.schema import IniFile
from pydub import AudioSegment
import cv2
import sys
import subprocess
import os


def audio(video_file):
    filename, ext = os.path.splitext(video_file)
    subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

def convert(infile):
  print(infile)
  #audio(infile)
  out = ".\images"
  vidcap = cv2.VideoCapture(infile)
  #success,image = vidcap.read()
  count = 0
  success = True
  while success:
    success,image = vidcap.read()
    try:
      cv2.imwrite(out+"\\" + "%d.jpg" % count, image)    # save frame as JPEG file
      print(f"Saved Image {count}")
    except:
      print("IMAGE EMPTY")
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
        break
    count += 1

def videofps(infile):
  vidcap = cv2.VideoCapture(infile)
  fps = vidcap.get(cv2.CAP_PROP_FPS)
  return fps

if __name__ == "__main__":
  convert("test.mp4")