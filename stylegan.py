from tkinter import *
from PIL import ImageTk,Image
import time
import os

targetImageWidth = 850
targetImageHeight = 400

inputImageWidth = 0
inputImageHeight = 0

currentScale = 1.0
inputDirectory = "images/"
outputDirectory = "images/output/"

root = Tk()
root.title("hyper crops")
canvas = Canvas(root, width = 1920, height = 1080)
canvas.pack()
rect = canvas.create_rectangle(1920/2, 1080/2, 150, 75, fill="", width=5)
imagePaths = []

fNumber = 0
currentOpenImagePath = ""
currentImage = 0
numCapturesOfCurrentImage = 0

statusLabelText = StringVar()
statusLabel = Label( root, textvariable=statusLabelText, relief=RAISED )

if not os.path.exists(outputDirectory):
    os.makedirs(outputDirectory)

def log(s):
    global statusLabelText
    global statusLabel

    statusLabelText.set(s)

def openImage():
    global fNumber
    global currentOpenImagePath
    global currentImage
    global inputImageWidth
    global inputImageHeight
    global currentScale

    currentScale = 1.0
    currentOpenImagePath = inputDirectory + imagePaths[fNumber]
    image = Image.open(currentOpenImagePath)
    img = ImageTk.PhotoImage(image)
    imageObject = canvas.create_image(0, 0, anchor=NW, image=img)

    if fNumber > 0:
        canvas.delete(currentImage)

    inputImageWidth = img.width()
    inputImageHeight = img.height()

    currentScale = float(inputImageWidth) / float(targetImageWidth)

    if currentScale*targetImageHeight > inputImageHeight:
        currentScale = float(inputImageHeight) / float(targetImageHeight)

    currentImage = imageObject
    root.mainloop()

def motion(event):
    global currentScale
    global statusLabel

    x = max(currentScale*targetImageWidth/2, min(event.x, inputImageWidth - currentScale*targetImageWidth/2) )
    y = max(currentScale*targetImageHeight/2, min(event.y, inputImageHeight - currentScale*targetImageHeight/2) )

    #print('{}, {}'.format(x, y))
    canvas.coords(rect,(x - currentScale*targetImageWidth/2,y - currentScale*targetImageHeight/2,x + currentScale*targetImageWidth/2, y + currentScale*targetImageHeight/2))
    canvas.tag_raise(rect)

def keyPress(event):
    global numCapturesOfCurrentImage
    global fNumber

    print(event.char)
    if event.char == ' ':
        fNumber=fNumber+1
        numCapturesOfCurrentImage = 0
        openImage()

def click(event):
    global canvas
    canvas.itemconfig(rect, outline='white')

def onClicked(event):
    global fNumber
    global currentOpenImagePath
    global currentScale
    global numCapturesOfCurrentImage
    global canvas

    canvas.itemconfig(rect, outline='black')
    outputFileName = outputDirectory + str(fNumber) + "_" + str(numCapturesOfCurrentImage) + ".jpg"

    x = max(currentScale*targetImageWidth/2, min(event.x, inputImageWidth - currentScale*targetImageWidth/2) )
    y = max(currentScale*targetImageHeight/2, min(event.y, inputImageHeight - currentScale*targetImageHeight/2) )

    command = "convert \"" + currentOpenImagePath + "\" -crop " + str(targetImageWidth*currentScale) + "x" + str(targetImageHeight*currentScale) + "+"+str(x-targetImageWidth*currentScale/2)+"+"+str(y-targetImageHeight*currentScale/2)+" -resize " + str(targetImageWidth) + "x" + str(targetImageHeight)+ " " +outputFileName
    numCapturesOfCurrentImage+=1
    log("saved " + outputFileName)
    os.system(command)

def mouse_wheel(event):
    global currentScale
    global canvas
    if event.delta > 0:
        currentScale -= 0.01
    else:
        currentScale += 0.01

    x = max(currentScale*targetImageWidth/2, min(event.x, inputImageWidth - currentScale*targetImageWidth/2) )
    y = max(currentScale*targetImageHeight/2, min(event.y, inputImageHeight - currentScale*targetImageHeight/2) )

    canvas.coords(rect,(x - currentScale*targetImageWidth/2,y - currentScale*targetImageHeight/2,x + currentScale*targetImageWidth/2, y + currentScale*targetImageHeight/2))
    canvas.tag_raise(rect)

def deleteImage(event):
    global fNumber
    global currentOpenImagePath
    global numCapturesOfCurrentImage

    command = "rm \"" + currentOpenImagePath + "\""
    fNumber=fNumber+1
    numCapturesOfCurrentImage = 0
    os.system(command)
    log("deleted " + currentOpenImagePath)
    openImage()

root.bind('<Motion>', motion)
root.bind("<Button 1>", click)
root.bind("<ButtonRelease-1>", onClicked)
root.bind("<MouseWheel>", mouse_wheel)
root.bind('<KeyPress>', keyPress)
root.bind("<BackSpace>", deleteImage)
root.lift()

statusLabel.place(relx=0.0, rely=0.0, anchor=NW)
imagePaths = os.listdir(inputDirectory)
openImage()
