# Python Script to detect Human Faces in a Video on the go
import cv2

# VideoCapture with param as Camera No: 0, 1(ext) or path of video file
video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")

# Loop to get continous frames as video
while True:

    # Check(Boolean) , Frame { Image => numpy array } read through the video variable
    check, frame = video.read()

    # Using the same process of detection of face in an image as a frame is only an image
    grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(grey_img,scaleFactor = 1.15, minNeighbors = 5)

    for x, y, w, h in faces:

        frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,255),10)

    cv2.imshow("Video Capture", frame)
    key=cv2.waitKey(1)

    # Wait for User to press q and exit the loop of capturing continous frames
    if key==ord('q'):
        break

# Stop the Camera and the Close the Windows
video.release()
cv2.destroyAllWindows()