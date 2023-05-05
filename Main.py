from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os
from tkinter import ttk
import requests
import cv2

main = Tk()
main.title("Image Processor using Flask Service API")
main.geometry("1300x1200")

global filename

def uploadImage():
    global filename
    filename = askopenfilename(initialdir = ".")
    tf1.insert(END,filename)

def callService():
    global filename
    flip_input = fliplist.get()
    rotate_input = rotatelist.get()
    rotate_degrees = degreeslist.get()
    grey_input = greylist.get()
    resize_height = heightlist.get()
    resize_width = widthlist.get()
    thumbnail_input = thumbnaillist.get()
    left_right = lrlist.get()

    fname = os.path.basename(filename)
    url = 'http://127.0.0.1:5000/upload' #URL to access FLASK Rest service
    #create query parameters with image name and image processing functions
    files = {
        'form': (fname+","+flip_input+","+rotate_input+","+rotate_degrees+","+grey_input+","+resize_height+","+resize_width+","+thumbnail_input+","+left_right,open(filename, 'rb'),'image/jpg'),
    }
    #send request to service with given URL and file
    output = requests.post(url, files=files)
    #if received output is OK then saved processed image and show the processed image to user
    if output.status_code == 200:
        with open("test.jpg", 'wb') as f:
            f.write(output.content)
        f.close()
        img = cv2.imread("test.jpg")
        cv2.imshow("Processed Image",img)
        cv2.waitKey(0)
    

font = ('times', 15, 'bold')
title = Label(main, text='Image Processor using Flask Service API')
title.config(bg='bisque', fg='purple1')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)

font1 = ('times', 13, 'bold')

l1 = Label(main, text='Image Path:')
l1.config(font=font1)
l1.place(x=50,y=100)

tf1 = Entry(main,width=20)
tf1.config(font=font1)
tf1.place(x=220,y=100)

browseButton = Button(main, text="Browse Image", command=uploadImage)
browseButton.place(x=440,y=100)
browseButton.config(font=font1)

l1 = Label(main, text='Flip Image:')
l1.config(font=font1)
l1.place(x=50,y=150)

flip = ['Choose Option','Horizontal','Vertical']
fliplist = ttk.Combobox(main,values=flip,postcommand=lambda: fliplist.configure(values=flip)) 
fliplist.place(x=220,y=150)
fliplist.current(0)
fliplist.config(font=font1)

l2 = Label(main, text='Rotate Image:')
l2.config(font=font1)
l2.place(x=50,y=200)

rotate = ['Choose Option','+','-']
rotatelist = ttk.Combobox(main,values=rotate,postcommand=lambda: rotatelist.configure(values=rotate)) 
rotatelist.place(x=220,y=200)
rotatelist.current(0)
rotatelist.config(font=font1)

degrees = ['Choose Degrees']
start = 10
while start < 110:
    degrees.append(str(start))
    start += 10
degreeslist = ttk.Combobox(main,values=degrees,postcommand=lambda: degreeslist.configure(values=degrees)) 
degreeslist.place(x=440,y=200)
degreeslist.current(0)
degreeslist.config(font=font1)

l3 = Label(main, text='Greyscale:')
l3.config(font=font1)
l3.place(x=50,y=250)

grey = ['Choose Option','Greyscale']
greylist = ttk.Combobox(main,values=grey,postcommand=lambda: greylist.configure(values=grey)) 
greylist.place(x=220,y=250)
greylist.current(0)
greylist.config(font=font1)

l4 = Label(main, text='Resize:')
l4.config(font=font1)
l4.place(x=50,y=300)

height = ['Height']
start = 1
while start <= 2000:
    height.append(str(start))
    start += 1
heightlist = ttk.Combobox(main,values=height,postcommand=lambda: heightlist.configure(values=height)) 
heightlist.place(x=220,y=300)
heightlist.current(0)
heightlist.config(font=font1)

width = ['Width']
start = 1
while start <= 2000:
    width.append(str(start))
    start += 1
widthlist = ttk.Combobox(main,values=width,postcommand=lambda: widthlist.configure(values=width)) 
widthlist.place(x=440,y=300)
widthlist.current(0)
widthlist.config(font=font1)

l5 = Label(main, text='Generate Thumbnail:')
l5.config(font=font1)
l5.place(x=50,y=350)

thumbnail = ['Choose Option','Thumbnail']
thumbnaillist = ttk.Combobox(main,values=thumbnail,postcommand=lambda: thumbnaillist.configure(values=thumbnail)) 
thumbnaillist.place(x=220,y=350)
thumbnaillist.current(0)
thumbnaillist.config(font=font1)

l5 = Label(main, text='Rotate Left/Right:')
l5.config(font=font1)
l5.place(x=50,y=400)

lr = ['Choose Option','Left','Right']
lrlist = ttk.Combobox(main,values=lr,postcommand=lambda: lrlist.configure(values=lr)) 
lrlist.place(x=220,y=400)
lrlist.current(0)
lrlist.config(font=font1)

callButton = Button(main, text="Call Image Processing Service API", command=callService)
callButton.place(x=140,y=450)
callButton.config(font=font1)

main.config(bg='cornflower blue')
main.mainloop()
