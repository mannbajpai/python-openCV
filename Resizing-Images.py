# Python Script to resize all images in a Folder to 400x400 pixel images
import cv2
import glob

# Using glob to access all jpg files in dir as images object
images = glob.glob("images/*.jpg")

# iterate over all the images one by one and resizing them
for image in images:

    # Reading
    # Resizing 
    # Writing/Saving
    img = cv2.imread(image, 1)
    resize_img = cv2.resize(img, (400,400))
    cv2.imwrite("re_images/"+image[7:-4]+"-resize.jpg",resize_img)