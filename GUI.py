import tkinter as tk
from tkinter import CENTER, ttk
from tkinter import filedialog as fd
from VideoImage import frame

class gui:
    filePath = ' '
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('AI Music Video Interpretor')
        self.root.resizable(False, False)
        self.root.geometry('500x250')
        
        #Create Label Object
        self.labelHow = ttk.Label(self.root, borderwidth = 1, relief = "ridge", text = 'Please Choose The Location Where You Would Like To Store Your Images')
        self.label = ttk.Label(self.root, borderwidth = 1, relief = "ridge", text = 'C:\\Desktop')

        #Create Button Object
        self.button = ttk.Button(self.root,text = "Choose Directory",command = self.selectFolder)
        self.button.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.buttonBegin = ttk.Button(self.root,text = "Start Conversion",command = self.begin)
        self.buttonBegin.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        #Pack Everything up
        self.labelHow.pack()
        self.label.pack(padx = 0, pady = 10)
        self.button.pack()
        self.buttonBegin.pack()
        self.root.mainloop()

    #######################
    def selectFolder(self):
        folderPath = fd.askdirectory()
        self.label['text'] = folderPath
        self.filePath = folderPath

    def begin(self):
        frame(self.filePath)

GUI = gui()







