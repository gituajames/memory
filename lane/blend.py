'''
i did all this in a jupyter notebook
'''

# image library
import cv2 as cv
# ploting library
import matplotlib.pyplot as plt

# open and read candidate images
one = cv.imread('data/1.jpg')
two = cv.imread('data/2.jpg')

def converttoRGB(image):
    '''
    helper function to convert bgr colorspace to rgb
    so matplotlib can plot the image
    '''
    return cv.cvtColor(image, cv.COLOR_BGR2RGB)

def blend(img1, img2, img1_weight = 0.5, img2_weight = 0.5):
    '''
    this where the blending is done
    you can adjust the weights for img1 and img2
    '''
    return cv.addWeighted(one, img1_weight, two, img2_weight, 0)

def show_image(blend):
    ''' function to plot the image'''
    return plt.imshow(converttoRGB(blend))

# usage
# however this step will work in jupyter notebook
show_image(blend(one, two, 0.5, 0.5))

# to save the image to hard disk
cv.imwrite('pic.jpg', blend(one, two))