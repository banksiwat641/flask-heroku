import cv2 as cv
from cv2 import imread
import numpy as np
import matplotlib.pyplot as plt
import glob
from pathlib import Path
import os

img=cv.imread("dok.jpg")

#LINE_ALBUM_test size0_220802
#img=cv.imread("LINE_ALBUM_test size0_220802.jpg")
imgre=cv.resize(img,(400,500))
g_img=cv.cvtColor(imgre,cv.COLOR_BGR2GRAY)
thresh,th=cv.threshold(g_img,60,255,cv.THRESH_BINARY)

kernel = np.ones((2,2),np.uint8)
images=cv.dilate(th,kernel,iterations=2)
sumpix=np.sum(images==255)
sumbix=np.sum(images==0)
sums=np.sum(images)
sum2=images.sum()
print(sumpix ,sumbix, sums, sum2)
plt.imshow(images,cmap="gray")
plt.imshow(th,cmap="gray")
plt.xticks([])
plt.yticks([])
    
plt.show()
#path = "uploads"
#files = os.listdir(path)

#for file in files:
    # make sure file is an image
 #   if file.endswith(('.jpg', '.png', 'jpeg')):
 #       img_path =  file
 #       img=cv.imread(str(img_path))
  #      cv.imshow('',img)
  #      print(str(img_path))
  #      cv.waitKey(0)
   #     cv.destroyAllWindows()
#cv.destroyAllWindows()


#cv.imshow("output",th)
cv.waitKey(0) 
cv.destroyAllWindows()