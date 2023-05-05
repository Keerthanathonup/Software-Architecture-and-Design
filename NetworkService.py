#Flask based web service which can be deployed on cloud server also
from flask import Flask, render_template, request, redirect, url_for, session, Response
import cv2
from ImageProcessor import ImageProcessor #importing ImageProcessor class
import os
from flask import send_file

app = Flask(__name__)

app.secret_key = 'welcome'

global processor
processor = None

#function to check if processor object None then create its object single time and if already created then its previous reference will returned back
def getImageProcessor():
    global processor
    if processor is None: #if none then create object
        processor = ImageProcessor()
    return processor    

#function to receive uploaded image and image processing functions from user and then apply those operations and return processed image back to user
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print(request)
    if request.method == 'POST':
        print(request.files)
        file = request.files['form']
        data = request.files['form'].read()
        arr = file.filename.split(",")
        fname = arr[0]
        flip_input = arr[1]
        rotate_input = arr[2]
        rotate_degrees = arr[3]
        grey_input = arr[4]
        resize_height = arr[5]
        resize_width = arr[6]
        thumbnail_input = arr[7]
        left_right = arr[8]
        #print(fname+" "+flip_input+" "+rotate_input+" "+rotate_degrees+" "+grey_input+" "+resize_height+" "+resize_width+" "+thumbnail_input+" "+left_right)
        out_file = open("test.jpg", "wb")
        out_file.write(data)
        out_file.close()
        processor = getImageProcessor()
        img = cv2.imread("test.jpg")
        if flip_input != 'Choose Option':
            if flip_input == 'Horizontal':
                img = processor.flipHorizontal(img)
            if flip_input == 'Vertical':
                img = processor.flipVertical(img)
        if rotate_input != 'Choose Option':
            if rotate_input == '+':
                img = processor.rotatePositive(img, int(rotate_degrees))
            if rotate_input == '-':
                img = processor.rotateNegative(img, -abs(int(rotate_degrees)))    
        if grey_input != 'Choose Option':
            img = processor.greyConversion(img)
        if resize_height != 'Height' and resize_width != 'Width':
            img = processor.resize(img, int(resize_width), int(resize_height))
        if  thumbnail_input != 'Choose Option':
            img = processor.thumbnail(img)
        if left_right != 'Choose Option':
            if left_right == 'Left':
                img = processor.rotateLeft(img)
            if left_right == 'Right':
                img = processor.rotateRight(img)
        cv2.imwrite("test.jpg",img)
        return send_file("test.jpg", mimetype='image/jpg')
        

if __name__ == '__main__':
    app.run()
