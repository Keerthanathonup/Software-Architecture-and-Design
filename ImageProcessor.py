import cv2
import imutils

class ImageProcessor:

    
    #function to create thumbnail on given image and user has to call this function as service to generate thumbnail
    def thumbnail(self, img):
        width, height, color = img.shape
        return cv2.resize(img,(width * 2, height * 2),interpolation=cv2.INTER_AREA)

    #can be called by user to resize image as per height and width given by user
    def resize(self, img, width, height):
        return cv2.resize(img,(width,height))

    #can be used to rotate images with positive degree values
    def rotatePositive(self, img, degrees):
        return imutils.rotate(img, degrees)

    #can be used to rotate images with negative degree values
    def rotateNegative(self, img, degress):
        return imutils.rotate(img, degrees)
    
    #can called or invoke this service to rotate left
    def rotateLeft(self, img):
        return imutils.rotate(img, 90)

    #can called or invoke this service to rotate right
    def rotateRight(self, img):
        return imutils.rotate(img, 270)

    #can called or invoke this service to convert image to grey format
    def greyConversion(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #called to rotate image vertically
    def flipVertical(self, img):
        return cv2.flip(img, 0)
    #called to rotate image horizontally
    def flipHorizontal(self, img):
        return cv2.flip(img, 1)
        
