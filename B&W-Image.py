# Working with OpenCV in Python 
# use pip install opencv-python to get the module  
import cv2

# An image variable storing image pixels as numpy array 
# imread(<path of image>, band) here 0 => Greyscale
img = cv2.imread("images\galaxy.jpg", 0)

print (type(img)) #<class 'numpy.ndarray'>
print(img)
print (img.shape) # widht x height tuple
print(img.ndim) # dimension

# Resizing the image to half the width and height of original image
resize_img= cv2.resize(img,(img.shape[0]//2,img.shape[1]//2))

# Showing the Resized Greyscale Image in an External Window named "Galaxy"

cv2.imshow("Galaxy",resize_img)
cv2.waitKey(0) # waitKey => any key 
cv2.destroyAllWindows()

# Saving the Formatted Image locally
cv2.imwrite("re_images/bnw_resize_galaxy.jpg", resize_img)