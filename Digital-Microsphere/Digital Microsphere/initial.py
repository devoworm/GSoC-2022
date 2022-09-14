from multiprocessing.connection import wait
from cv2 import imread
import numpy as np
import cv2 as cv
import cv2 
import sys
import os
import pandas as pd
# from skimage import io
# from PIL import Image, ImageDraw, ImageOps
# import matplotlib.pylab as plt
# import cvzone
# from cvzone.SelfiSegmentationModule import SelfiSegmentation

# segmentor = SelfiSegmentation()

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
        # blue, green, red = cv2.split(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3,3), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        image_copy = image.copy()
        maskImage = np.zeros(image_copy.shape, dtype=np.uint8)
        cv2.drawContours(maskImage, contours, -1, (255,255,255),-1)
        
        newImage = cv2.bitwise_and(image_copy, maskImage)
        cv2.imshow("maskdfadgae",newImage)
        cv2.waitKey(0)
        for cnt in contours:
            # rect = cv2.minAreaRect(cnt)
            # box = cv2.boxPoints(rect)
            # box = np.int0(box)
            # cv2.drawContours(image_copy,[box],0,(0,0,255),2)
            # epailon = 0.01*cv2.arcLength(cnt,True)
            # approx = cv2.approxPolyDP(cnt,epailon,True)
            # cv2.drawContours(image_copy,[approx],0,(0,0,255),2)
            if ((cv2.arcLength(cnt,True) > 500) and (cv2.arcLength(cnt,True) < 1100)):
                (x,y,w,h) = cv2.boundingRect(cnt)
                box = cv2.rectangle(newImage, (x,y), (x+w,y+h), (255,0,0), 2)
                cropped_image = image_copy[y:y+h, x:x+w]
                # cv2.imshow("cropped",cropped_image)
            else:
                continue



        # (x,y),radius = cv.minEnclosingCircle(cnt)
        # center = (int(x),int(y))
        # radius = int(radius)
        # cv.circle(image_copy,center,radius,(0,255,0),2)
        # cv2.imshow("outline",newImage)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return cropped_image
        # cv2.imshow("thresh",thresh)
        # plt.xlim(0, 750)
        # plt.ylim(0, 750)
        # out=plt.contour(thresh)
        # plt.show()
        
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
        
        # cv2.imshow("masked",imgr3)
        # cv2.waitKey(0)
        return imgr3

    # def mask_circular(self,im):
    #     mask = Image.new("L",im.size,0)
    #     draw = ImageDraw.Draw(mask)
    #     draw.ellipse((0,0) + im.size, fill=255)
    #     out = ImageOps.fit(im,np.mask.size,centering=(0.5,0.5))
    #     out.putalpha(mask)
    #     return out
    def joinImages(self,img1, img2):
        # img1 = cv2.resize(img1, (0,0), fx=0.5, fy=0.5)
        # img2 = cv2.resize(img2, (0,0), fx=0.5, fy=0.5)
        img3 = cv2.hconcat([img1, img2])
        return img3

    def main(self,image_location):
        image = cv2.imread(image_location)
        image = cv2.resize(image,(0,0),fx=0.2,fy=0.2)
        output = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 120, param1 = 50,
                    param2 = 30, minRadius = 95, maxRadius = 155)
        # ensure at least some circles were found
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                
                # cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(output, (x - r, y - r), (x + r, y + r), (0, 128, 255), 0)
                return output[y-r:y+r,x-r:x+r]
                
            # # show the output image
            # cv2.imshow("output", np.hstack([image, output]))
            # cv2.waitKey(0)
            

    def run(self,file1,file2):
        img1 = self.main(file1)
        img2 = self.main(file2)
        # img1 = cv2.imread(file1)
        # img1 = self.resize(img1)
        # img1 = self.outline(img1)
        img1 = cv2.resize(img1,(500,500))
        # img2 = cv2.imread(file2)
        # img2 = self.resize(img2)
        # img2 = self.outline(img2)
        img2 = cv2.resize(img2,(500,500))
        img3 = self.joinImages(img1, img2)
        # cv2.destroyAllWindows()
        cv2.imwrite("./obj/outline.jpg",img3)
        # return "result\outline.jpg"
        return img3

# i = imread("./resources/DSC_4472.JPG")
# x = img_prcocess()
# i=x.resize(i)
# x.outline(i)

x = img_prcocess()
# i=x.resize(i)
# x.outline(i)
x.run(sys.argv[1],sys.argv[2])


# print(b.shape())
# plt.show()
# cv2.imwrite('result.jpg',c)
