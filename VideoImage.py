from msilib.schema import IniFile
from pydub import AudioSegment
from moviepy.editor import VideoFileClip
import cv2
import sys
import subprocess
import os


def audio(video_file):
  # Open the mp4 file
  clip = VideoFileClip(video_file)
  # Extract the audio from the file
  audio = clip.audio
  # Save the audio to a new file
  audio.write_audiofile("audio.mp3")

def convert(infile):
  print(infile)
  audio(infile)
  out = ".\images"
  vidcap = cv2.VideoCapture(infile)
  #success,image = vidcap.read()
  count = 0
  success = True
  while success:
    success,image = vidcap.read()
    try:
      cv2.imwrite(out + "\\" + "%d.jpg" % count, image)    # save frame as JPEG file
      print(f"Saved Image {count}")
    except:
      print("IMAGE EMPTY")
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
        break
    count += 1

def videofps(infile):
  vidcap = cv2.VideoCapture(infile)
  fps = vidcap.get(cv2.CAP_PROP_FPS)
  vidcap.release()
  return fps

if __name__ == "__main__":
  convert("test.mp4")