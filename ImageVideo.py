import os
import cv2
import moviepy.editor as mp
import subprocess


def convert_avi_to_mp4():
    avi_file_path = os.getcwd() + "\\render.avi"
    output_name = os.getcwd() + "\\render.mp4"

    subprocess.call(["ffmpeg", "-i", avi_file_path,output_name])


def audio():
    inaudio = os.getcwd() + "\\output.mp3"
    invideo = os.getcwd() + "\\render.mp4"
    output = os.getcwd() + "\\final_render.mp4"
    os.system(f"ffmpeg -i {invideo} -i {inaudio} -c copy -map 0:v:0 -map 1:a:0 {output}")


def generate_video(framerate):
    image_folder = "C:\\Users\\jojop\\Desktop\\AI Convert Fast\\Oliver Tree - Cowboys dont cry\\OUT"
    images = [img for img in os.listdir(image_folder)]
    images.sort(key = lambda x: int(x.split(".")[0]))

    video = cv2.VideoWriter("render.avi", 0, framerate, (1024,1024))
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        #os.remove(image)
    cv2.destroyAllWindows()
    video.release()
    #convert_avi_to_mp4()
    #audio()

if __name__ ==  "__main__":
    generate_video(24)
