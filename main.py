import GauganSend, ImageConvert, ImageVideo, VideoImage


def run(videofile):
    print("Splitting video")
    try:
        VideoImage.convert(videofile)
        print("complete")
    except:
        print("VIDEO TO IMAGE FAILED.... CONTINUING")
    fps = VideoImage.videofps(videofile)
    print(f'FPS = {fps}')
    print("Converting Image")
    k = ImageConvert.execute()
    if k :
        print("done")
    print("Complete")
    print("Sending files to server")
    GauganSend.execute()
    print("Sending files to server complete")
    print("Creating Video")
    ImageVideo.generate_video(fps)
    print("complete")

if __name__ == "__main__":
    videofile = input("Input Video: ")
    run(videofile)
