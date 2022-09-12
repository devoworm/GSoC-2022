import numpy as np
import pandas as pd
import cv2
import cv2 as cv
from google.colab.patches import cv2_imshow
from skimage import io
from PIL import Image 
import matplotlib.pylab as plt
import plotly.graph_objects as go


def resize(image):
  reimage = cv2.resize(image, (0, 0), fx = 0.3, fy = 0.3)
  return reimage

def grayscale(image):
  gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
  return gray_image

def blur(img):
  arr=[]
  kernel = np.array([[1,2,1],
                     [2,4,2],
                     [1,2,1]]) * 0.0625
  image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
  arr=image_sharp
  return arr
  #cv2_imshow(image_sharp)

def mask(imgr3):
  #imgr3=resize(image33)
  # Load the img and convert to HSV colourspace
  #img = cv.imread(reimg)
  #cv2_imshow(img)
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

  """
  kernel = np.array([[1,2,1],
                     [2,4,2],
                     [1,2,1]]) * 0.0625
  imgr3 = cv2.filter2D(src=imgr3, ddepth=-1, kernel=kernel)"""
  #cv2_imshow(imgr3)
  return imgr3

def outline(b):
  gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (3,3), 0)
  thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
  plt.xlim(0, 2500)
  plt.ylim(0, 2500)
  out=plt.contour(thresh)
  return out

outline_set=[]
for i in range(33,41):
  image=eval('image'+str(i))
  a=image

  b=a
  for i in range(1):
    b=blur(b)
  b=mask(b)
  for i in range(1):
    b=blur(b)
  #cv2_imshow(b)
  c=outline(b)
  outline_set.append(c)
  plt.show(c)

def frame_generate()
  for i in range(33,41):

    angle=angle_list[i-33]
    image=eval('image'+str(i))
    a=image

    b=a
    for i in range(10):
      b=blur(b)
    b=mask(b)
    for i in range(10):
      b=blur(b)
    #cv2_imshow(b)
    c=outline_opcv(b)
    plt.show(c)
    print(c)

    contour_set.append(c)
    M = cv.moments(c[0])
    #print(M)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print(cx,cy)

    spatial_list=[]
    for i in range(len(c[0])):
      tx=c[0][i][0][0]
      c[0][i][0][0]=tx-cx
      ty=c[0][i][0][1]
      c[0][i][0][1]=ty-cy
      sla=np.sin(angle)
      slb=np.cos(angle)
      sl=[(tx-cx)*slb,ty-cy,(tx-cx)*sla]
      #print(sl)
      spatial_list.append(sl)
      final.append(sl)

    print(spatial_list)
    print(c)

  def Model_Frame(contour_Mset)
  x=[]
  y=[]
  z=[]
  for i in range(len(contour_Mset)):
    x.append(contour_Mset[i][0])
    y.append(contour_Mset[i][1])
    z.append(contour_Mset[i][2])
  fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])
  fig.show()
  fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, color='blue', opacity=0.50)])
  fig.show()