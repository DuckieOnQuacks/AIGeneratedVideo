import os
import cv2

def generate_video():
    image_folder = 'C:\\Users\\jojop\\Desktop\\AI Convert\\OUT'
    video_name = 'OliverTreeAI.mp4'
    os.chdir("C:\\Users\\jojop\\Desktop\\AI Convert\\FinalVideo")

    images = [img for img in os.listdir(image_folder)]
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') 
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    video = cv2.VideoWriter(video_name, fourcc, 24, (1024, 1024))

    # Appending the images to the video one by one 
    for i, image in enumerate(images):
        video.write(cv2.imread(os.path.join(image_folder,image)))

    # Deallocating memory taken for window creation 
    cv2.destroyAllWindows()
    video.release()  # releasing the video generated 
    
generate_video()
