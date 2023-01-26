from fileinput import filename
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import tkinter
import VideoImage, ImageConvert_HSV_MAPS, ImageVideo, GauganSend

class gui():
    def __init__(self):
        self.filetypes = (('Video Files', '*.mp4'),('All files', '*.*'))
        self.root = tk.Tk()
        self.root.title('AI Music Video Interpretor')
        self.root.resizable(False, False)
        self.root.geometry('500x200')
        self.root.attributes('-alpha',1)
        self.b1 = tk.Button(self.root,text="SELECT FOLDER", command = self.selectFolderPath)
        self.b1.place(relx = .46, rely = .5, anchor = CENTER)
        self.b1.pack()
        self.button_start = tk.Button(self.root,text=" START ENTIRE ", command = self.StartMain)
        self.file_label = Label(self.root)
        self.file_label.pack()
        self.button_start.pack()
        self.partial_button = tk.Button(self.root,text="START PARTIAL", command = self.PartialStart).pack()
        self.Progress = Label(self.root)
        self.Progress.pack()
        self.console = "WAITING..."
        self.console_loop()
        self.root.mainloop()

    def console_loop(self):
        output = self.console
        self.Progress.configure(text=output)
        self.root.after(2000, self.console_loop)

    # START PARTIAL =====================================================================================================
    def PartialStart(self):
        self.window = tk.Toplevel(self.root)
        self.window.title('Run Parts Of Interpretor')
        self.window.resizable(False, False)
        self.window.geometry('250x150')
        self.window.attributes('-alpha', 1)
        self.VideoImage_button = tk.Button(self.window,text="Convert Video To Image", command = self.Video_Image).pack()
        self.ImageConvert_button = tk.Button(self.window,text="Convert Images", command = self.Image_Convert).pack()
        self.GuaganSend_button= tk.Button(self.window,text="Send Images to AI", command = self.GuaganSend).pack()
        self.ImageVideo_button = tk.Button(self.window,text="Convert Image To Video", command = self.Image_Video).pack()
        self.partial_window = Label(self.window,text="Select Frame Rate For Image To Video").pack()
        self.frame_variable = IntVar(self.window)
        self.frame_variable.set(25.0)
        self.FrameSelect = OptionMenu(self.window, self.frame_variable, 24.0, 25.0, 30.0, 50.0, 60.0)
        self.FrameSelect.pack()
        self.window.mainloop()

    def Video_Image(self):
        self.console = "VIDEO TO IMAGE: STARTING"
        if self.folderPath:
            filename = self.folderPath
        else:
            filename = filedialog.askopenfilename(title="Select Video To Process", initialdir='/', filetypes = self.filetypes)
        VideoImage.convert(filename)
        self.console = "VIDEO TO IMAGE: COMPLETE"
    def Image_Convert(self):
        self.console = "IMAGE CONVERT: STARTING"
        k = ImageConvert_HSV_MAPS.execute()
        if k:
            print("Done....")
            self.console = "IMAGE CONVERT: COMPLETE"
    def GuaganSend(self):
        GauganSend.execute()
    def Image_Video(self):
        self.console = f"GENERATING VIDEO AT {self.frame_variable.get()} FPS"
        ImageVideo.generate_video(self.frame_variable.get())
        self.console = f"VIDEO GENERATION COMPLETE"

    # START PARTIAL =====================================================================================================

    def selectFolderPath(self):
        self.folderPath = str(filedialog.askopenfilename(title="Select Video To Process",initialdir='/',filetypes = self.filetypes))
        self.file_label.configure(text = self.folderPath)
        
    # START ENTIRE ======================================================================================================

    def StartMain(self):
        print("Splitting video")
        self.console = "VIDEO TO IMAGE: STARTING"
        VideoImage.convert(self.folderPath)
        self.console = "VIDEO TO IMAGE: COMPLETE"
        print("complete")
        fps = VideoImage.videofps(self.folderPath)
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
        ImageVideo.generate_video(fps)
        self.console = f"VIDEO GENERATION COMPLETE"
        print("complete")
    # START ENTIRE ======================================================================================================= 


if __name__ == "__main__":
    GUI = gui()







