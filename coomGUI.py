import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
import VideoImage, ImageConvert_HSV_MAPS, ImageVideo, GauganSend
import os


class gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('AI Music Video Interpretor')
        self.root.resizable(False, False)
        self.root.geometry('500x250')
        
        #Create Label Object
        self.labelHow = tk.Label(self.root, text = 'Please Choose The Location Where You Would Like To Store Your Images')
        self.label = tk.Label(self.root, text = '')

        self.labelWhere = tk.Label(self.root, text = 'Please Choose The Location Of Your Youtube Video')
        self.label2 = tk.Label(self.root, text = 'C:\\Desktop')

        #Create Button Object
        self.button = tk.Button(self.root,text = "Choose Directory",command = self.selectFolder)
        self.button.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        #Create Button Object to choose youtube link location
        self.button2 = tk.Button(self.root,text = "Choose Video File",command = self.selectVideo)
        self.button2.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.buttonPartial = tk.Button(self.root,text = "Start Partial",command = self.PartialStart)
        self.buttonPartial.place(relx = 1, rely = 1, anchor = CENTER)

        self.buttonBegin = tk.Button(self.root,text = "Start Conversion",command = self.StartMain)
        self.buttonBegin.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        #Pack Everything up
        self.labelHow.pack()
        self.label.pack(padx = 0, pady = 5)
        self.button.pack()

        self.labelWhere.pack(padx = 0, pady = 10)
        self.label2.pack(padx = 0, pady = 5)
        self.button2.pack()

        self.buttonBegin.pack()
        self.buttonPartial.pack()
        self.root.mainloop()

    def fileCheck(self):
        filelist = ["./AiImages","./Processed","./Frames"]
        for files in filelist:
            if os.path.exists(files):
                #check what files are here
                pass
            else:
                os.makedirs(files)

    #######################
    def selectFolder(self):
        folderPath = fd.askdirectory()
        self.label['text'] = folderPath
        self.filePath = folderPath
        os.chdir(self.filePath)
        self.fileCheck()

    ######################
    def selectVideo(self):
        videoPath = fd.askopenfilename(title = "Select A File", filetypes = (('Video Files', '*.mp4'),('All files', '*.*')))
        self.label2['text'] = videoPath
        self.videoPathYep = videoPath

    # START PARTIAL =====================================================================================================
    def PartialStart(self):
        self.window = tk.Toplevel(self.root)
        self.window.title('Run Parts Of Interpretor')
        self.window.resizable(False, False)
        self.window.geometry('250x150')
        self.VideoImage_button = tk.Button(self.window,text="Convert Video To Image", command = self.videoImage).pack()
        self.ImageConvert_button = tk.Button(self.window,text="Convert Images", command = self.convertImage).pack()
        self.GuaganSend_button= tk.Button(self.window,text="Send Images to AI", command = self.gauganSend).pack()
        self.ImageVideo_button = tk.Button(self.window,text="Convert Image To Video", command = self.imageVideo).pack()
        self.partial_window = Label(self.window,text="Select Frame Rate For Image To Video").pack()
        self.frame_variable = IntVar(self.window)
        print(self.frame_variable)
        self.frame_variable.set(25)
        print(self.frame_variable)
        self.FrameSelect = OptionMenu(self.window, self.frame_variable, 24, 25,30,50,60)
        self.FrameSelect.pack()
        self.window.mainloop()

    ##################
    def getPath(self):
        return self.filePath

    #####################
    def gauganSend(self):
        GauganSend.execute()

    #######################
    def convertImage(self):
        ImageConvert_HSV_MAPS.execute()
        
    def imageVideo(self):
        ImageVideo.generate_video(self.frame_variable, self.filePath)

    def videoImage(self):
        VideoImage.convert(self.filePath, self.videoPathYep)

########################
    def StartMain(self):
        print("Splitting video")
        self.console = "VIDEO TO IMAGE: STARTING"
        try:
            VideoImage.convert(self.filePath, self.videoPathYep)
            self.console = "VIDEO TO IMAGE: COMPLETE"
            print("complete")
        except:
            print("VIDEO TO IMAGE FAILED.... CONTINUING")
            self.console = "VIDEO TO IMAGE: FAILED"
        fps = VideoImage.videofps(self.videoPathYep)
        print(f'FPS = {fps}')
        print("Converting Image")
        self.console =f"IMAGE CONVERT: STARTING\nVIDEO FPS: {fps}"
        k = ImageConvert_HSV_MAPS.execute()
        if k :
            print("done")
            self.console = "IMAGE CONVERT: COMPLETE"
        print("Complete")
        print("Sending files to server")
        self.console = "SENDING FILES TO SERVER"
        GauganSend.execute()
        print("Sending files to server complete")
        print("Creating Video")
        self.console = "RECEIVED ALL FILES"
        self.console = f"GENERATING VIDEO AT {fps} FPS"
        ImageVideo.generate_video(fps, self.filePath)
        self.console = f"VIDEO GENERATION COMPLETE"
        print("complete")

if __name__ == "__main__":
    GUI = gui()        







