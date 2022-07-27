# Python script to detect Faces in an image and Drawing a rectangle around it
import cv2 as cv

# https://github.com/opencv/opencv/tree/master/data/haarcascades Github for haarcascade xml
face_cascade = cv.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")

img = cv.imread('images\\face1.jpg')

# Converting image to grayscale for more acurate detection
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Scaling an image multiple time for accurate detection 
faces=face_cascade.detectMultiScale(grey_img,scaleFactor = 1.1, minNeighbors = 5)

print(faces) # Prints Start x, Start y, Width, Height as numpy array

for x, y, w, h in faces:

        # rectangle(starting pixel coord, end pix coord, color in BGR, Width of rectangle )
        image = cv.rectangle(img, (x,y),(x+w,y+h),(0,255,255),10)

resize_im = cv.resize(image, (800,600))

cv.imshow("Face Detection",resize_im) 
cv.waitKey(0)
cv.destroyAllWindows()