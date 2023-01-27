import os
import cv2
import moviepy.editor as mp
from moviepy.editor import *
import concurrent.futures

############
def audio():
    video = mp.VideoFileClip(os.getcwd() + "\\render.mp4")
    audio = mp.AudioFileClip(os.getcwd() + "\\audio.mp3")
    output = os.getcwd() + "\\final_render.mp4"
    video = video.set_audio(audio)
    video.write_videofile(output)
    splitscreen("Crazy.mp4","final_render.mp4")
    print("Video and audio combined successfully.")

##############################
def generate_video(framerate):
    image_folder = './out'
    images = [img for img in os.listdir(image_folder)]
    images.sort(key = lambda x: int(x.split(".")[0]))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter("render.mp4", fourcc, framerate, (1024,1024))
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # submit the image processing task to the process pool
        futures = [executor.submit(process_image, os.path.join(image_folder, image)) for image in images]
        for future in concurrent.futures.as_completed(futures):
            video.write(future.result())
    cv2.destroyAllWindows()
    video.release()
    audio()
    os.remove("render.mp4")

##############################
def process_image(image_path):
    return cv2.imread(image_path)

###########################################
def splitscreen(originalVid, processedVid):
    # create a thread pool with 2 workers
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # submit the two video processing tasks to the thread pool
        future1 = executor.submit(VideoFileClip, originalVid)
        future2 = executor.submit(VideoFileClip, processedVid)

        # wait for both tasks to complete
        clip1, clip2 = future1.result(), future2.result()

    # combine the two clips
    combined = clips_array([[clip1, clip2]])
    combined.write_videofile("final_video.mp4")
    # create clips for the two input videos
    #clip1 = VideoFileClip(originalVid)
    #clip2 = VideoFileClip(processedVid)
    #combined = clips_array([[clip1, clip2]])
    #combined.write_videofile("final_video.mp4")

if __name__ ==  "__main__":
    generate_video(25)
