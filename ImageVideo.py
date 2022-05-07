import os
import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import moviepy.editor as mp

############
def audio():
    inaudio = os.getcwd() + "\\output.mp3"
    invideo = os.getcwd() + "\\render.mp4"
    output = os.getcwd() + "\\final_render.mp4"
    os.system(f"ffmpeg -i {invideo} -i {inaudio} -c copy -map 0:v:0 -map 1:a:0 {output}")

##############################
def generate_video(framerate, filepath, videoPath):
    image_folder = f'{filepath}\\AiImages'
    images = [img for img in os.listdir(image_folder)]
    images.sort(key = lambda x: int(x.split(".")[0]))
    fourcc = VideoWriter_fourcc(*'MP4V')
    video = cv2.VideoWriter("render.mp4", fourcc, framerate, (1024,1024))
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    cv2.destroyAllWindows()
    video.release()
    os.chdir(filepath)
    audio(videoPath)
    os.remove("render.mp4")

###########################
if __name__ ==  "__main__":
    generate_video(30)