import tkinter as tk
from tkinter import CENTER, ttk
from tkinter import filedialog as fd
from VideoImage import frame

class gui:
    filePath = ' '
    videoPathYep = ' '
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('AI Music Video Interpretor')
        self.root.resizable(False, False)
        self.root.geometry('500x250')
        
        #Create Label Object
        self.labelHow = ttk.Label(self.root, text = 'Please Choose The Location Where You Would Like To Store Your Images')
        self.label = ttk.Label(self.root, text = 'C:\\Desktop')

        self.labelWhere = ttk.Label(self.root, text = 'Please Choose The Location Of Your Youtube Video')
        self.label2 = ttk.Label(self.root, text = 'C:\\Desktop')

        #Create Button Object
        self.button = ttk.Button(self.root,text = "Choose Directory",command = self.selectFolder)
        self.button.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        #Create Button Object to choose youtube link location
        self.button2 = ttk.Button(self.root,text = "Choose Video File",command = self.selectVideo)
        self.button2.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.buttonBegin = ttk.Button(self.root,text = "Start Conversion",command = self.begin)
        self.buttonBegin.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        #Pack Everything up
        self.labelHow.pack()
        self.label.pack(padx = 0, pady = 5)
        self.button.pack()

        self.labelWhere.pack(padx = 0, pady = 10)
        self.label2.pack(padx = 0, pady = 5)
        self.button2.pack()

        self.buttonBegin.pack()
        self.root.mainloop()

    #######################
    def selectFolder(self):
        folderPath = fd.askdirectory()
        self.label['text'] = folderPath
        self.filePath = folderPath
    
    def selectVideo(self):
        videoPath = fd.askopenfilename(title = "Select A File", filetypes = (("mov files", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi")))
        self.label2['text'] = videoPath
        self.videoPathYep = videoPath

    def begin(self):
        frame(self.filePath, self.videoPathYep)
        

GUI = gui()







