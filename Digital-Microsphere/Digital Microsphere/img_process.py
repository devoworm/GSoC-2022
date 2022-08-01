from cv2 import imread
import numpy as np
import cv2 as cv
import cv2 
import pandas as pd
from skimage import io
from PIL import Image, ImageDraw, ImageOps
import matplotlib.pylab as plt
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

segmentor = SelfiSegmentation()

class img_prcocess:
    @staticmethod
    def resize(image):
        resized_image = cv2.resize(image,(0,0),fx=0.2,fy=0.2)
        return resized_image

    def blur(self,img):
        arr=[]
        kernel = np.array([[1,2,1],
                        [2,4,2],
                        [1,2,1]]) *0.0625
        image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
        arr=image_sharp
        cv2.imshow("blur",arr)
        cv2.waitKey(0)
        return arr
        
    def outline(self,image):
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3,3), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[-1]
        cv2.imshow("thresh",thresh)
        plt.xlim(0, 750)
        plt.ylim(0, 750)
        out=plt.contour(thresh)
        plt.show()
        
    def mask(self,imgr3):

        hsv=cv.cvtColor(imgr3,cv.COLOR_BGR2HSV)
        #cv2_imshow(imgr3)
        # Define lower and uppper limits of color
        blue_lo=np.array([60,50,70])
        blue_hi=np.array([179,255,255])

        # Mask img to only select blue
        mask=cv.inRange(hsv,blue_lo,blue_hi)

        # Change img to white where we found blue
        imgr3[mask>0]=(255,255,255)
        #imgr3 = cv2.rotate(imgr3, cv2.cv2.ROTATE_90_CLOCKWISE)
        # img69 = segmentor.removeBG(imgr3,(255,0,255))
        
        cv2.imshow("masked",imgr3)
        cv2.waitKey(0)
        return imgr3

    def mask_circular(self,im):
        mask = Image.new("L",im.size,0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0,0) + im.size, fill=255)
        out = ImageOps.fit(im,np.mask.size,centering=(0.5,0.5))
        out.putalpha(mask)
        return out


i = imread("DSC_4473.jpg")
x = img_prcocess()
i=x.resize(i)
mask = np.zeros(i.shape[:2], dtype="uint8")
cv2.circle(mask, (190, 240), 140, 255, -1)
masked = cv2.bitwise_and(i, i, mask=mask)
# show the output images
# cv2.imshow("Circular Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

cv2.destroyAllWindows()

# print(b.shape())
# plt.show()
# cv2.imwrite('result.jpg',c)
