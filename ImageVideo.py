import os
import cv2
import moviepy.editor as mp
import subprocess

def audio():
    video = mp.VideoFileClip(os.getcwd() + "\\render.mp4")
    audio = mp.AudioFileClip(os.getcwd() + "\\audio.mp3")
    output = os.getcwd() + "\\final_render.mp4"
    video = video.set_audio(audio)
    video.write_videofile(output)
    print("Video and audio combined successfully.")


def generate_video(framerate):
    image_folder = './out'
    images = [img for img in os.listdir(image_folder)]
    images.sort(key = lambda x: int(x.split(".")[0]))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter("render.mp4", fourcc, framerate, (1024,1024))
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    cv2.destroyAllWindows()
    video.release()
    audio()
    os.remove("render.mp4")


if __name__ ==  "__main__":
    generate_video(24)
