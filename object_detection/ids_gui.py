import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import run_model, run_model_video, cv2
from utils import visualization_utils
from tkinter import messagebox as mb

# Create Instance
win = tk.Tk()

# Title to gui
win.title("IDS GUI")

# Initial window sise
win.geometry("500x500")

# IDS logo
logoCanvas = tk.Canvas(win, width=340, height=50)
logoCanvas.pack()
img = ImageTk.PhotoImage(Image.open('idslogo2.jpg'))
logoCanvas.create_image(50, 10, anchor='nw', image=img)

# Variables
filename = ""

# GUI Buttons

# Information Button
def openFile():
    os.system("info.txt")

infoBtn = tk.Button(win, text='Info', width=10, command=openFile)
infoBtn.pack()
infoBtn.place(x=10, y=50, bordermode='outside')


# Upload Button
def fileUpload():
    filename1 = filedialog.askopenfilename(initialdir="/", title="Select File",
                                           filetypes=(("Images", "*.png .*jpg"), ("All files", "*.*"),
                                                      ("Videos", "*.mp4")))
    if filename1:
        try:
            displayPhoto(filename1)
            global filename
            filename = filename1
        except:
            try:
                filename = filename1
                videoInput(filename)
            except:
                mb.showinfo('Warning', 'Invalid file.')


uploadBtn = tk.Button(win, text='Upload', width=10, command=fileUpload)
uploadBtn.pack()
uploadBtn.place(x=10, y=100, bordermode='outside')


def runImage(filename, result, outputFrame):
    print("image processing!" + filename)
    if filename != "":
        try:
            run_model.main(filename, result, outputFrame)
        except:
            mb.showinfo('Warning', 'Invalid file!')

    else:
        mb.showinfo('Warning', 'No file detected')


# Image Button

imgBtn = tk.Button(win, text='Run Image', width=10, command=lambda: runImage(filename, result, outputFrame))
imgBtn.pack()
imgBtn.place(x=10, y=150, bordermode='outside')


def processVideo(filename, result, outputFrame):
    if filename != "":

        cv2video = cv2.VideoCapture(filename)
        framecount = cv2video.get(cv2.CAP_PROP_FRAME_COUNT)
        frames_per_sec = cv2video.get(cv2.CAP_PROP_FPS)
        duration = framecount / frames_per_sec
        print("Video duration (sec):", duration)
        if duration > 10:
            mb.showinfo('Warning', 'The program can only process video that is under 10 seconds.')
        if duration == 0.04:
            mb.showinfo('Warning', 'Invalid file!')
        else:
            run_model_video.main(filename, result, outputFrame)

    else:
        mb.showinfo('Warning', 'No file detected.')


# Video Button
videoBtn = tk.Button(win, text='Run Video', width=10, command=lambda: processVideo(filename, result, outputFrame))
videoBtn.pack()
videoBtn.place(x=10, y=200, bordermode='outside')

# Exit Button
def endProgram():
    win.destroy()
exitBtn = tk.Button(win, text='Exit',command = endProgram, width = 10)
exitBtn.pack()
exitBtn.place(x=10, y=250, bordermode='outside')


# Frames for Image & Outputs

# Image
def displayPhoto(filename):
    img = Image.open(filename)
    img = img.resize((300, 245), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(img)
    photoLabel = tk.Label(win, image=tkimage)
    photoLabel.image = tkimage
    photoLabel.pack()
    photoLabel.place(x=150, y=52)


# Video
def videoInput(filename):
    cap = cv2.VideoCapture(filename)

    try:
        if not os.path.exists('frames'):
            os.makedirs('frames')
    except OSError:
        print("Error: Creating directory data")

    currentFrame = 0

    ret, frame = cap.read()

    name = './frames/frame' + str(currentFrame) + '.jpg'
    cv2.imwrite(name, frame)

    displayPhoto(name)

    cap.release()
    cv2.destroyAllWindows()


# Frame for Output
outputFrame = tk.Frame(win, height=100, width=300, relief='sunken', borderwidth=2, bg='white')
outputFrame.pack()
outputFrame.place(x=150, y=325)

#Label Frame1
textFrame1 = tk.Frame(win)
textFrame1.pack()
textFrame1.place(x = 150, y = 300)

#Label Frame2
textFrame2 = tk.Frame(win)
textFrame2.pack()
textFrame2.place(x = 275, y = 300)

#Label Frame 3
textFrame3 = tk.Frame(win)
textFrame3.pack()
textFrame3.place(x = 385, y = 300)

#Label Frame Text
textFrameLabel1 = tk.Label(textFrame1,text = "Insect").pack();
textFrameLabel2 = tk.Label(textFrame2,text = "Count").pack();
textFrameLabel3 = tk.Label(textFrame3,text = "Pesticide").pack();

#display result
result = tk.StringVar()
result.set("display result here")

if not visualization_utils.resultList:
   result.set("No insect detected")

label = tk.Label(outputFrame, textvariable=result,bg = "white", width = 300)
label.pack()
outputFrame.pack_propagate(False)

# start the gui/create the main loop
win.mainloop()
