import cv2
import numpy as np
import matplotlib.pyplot as plt
large=3
im1=cv2.imread('lena.png',0)
[m,n]=im1.shape

im2=np.ones((m*large,n*large))

for i in range(m):
    for j in range(n):
        block=(np.ones((large,large)))*im1[i,j]
        im2[i*large:i*large+large,j*large:j*large+large]=block
