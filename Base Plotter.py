# Base plotter program
# This program accepts a depth data image and provides us with
# the intensity and distance data from it
# Reference for this code is from the website https://summations.github.io

# Library Definitions
import fire
import numpy as np
import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.mplot3d import Axes3D

# Image process
img_normal = cv2.imread('image_16_depth.png')
img_gr = cv2.cvtColor(img_normal, cv2.COLOR_BGR2GRAY)
plt.imshow(img_gr, cmap='gray')

# Graph/Plot process
x_val, y_val = np.mgrid[0:img_gr.shape[0], 0:img_gr.shape[1]]
plot = plt.figure(figsize=(15, 15))
axis = plot.gca(projection='3d')
axis.plot_surface(x_val, y_val, img_gr, rstride=1, cstride=1, cmap=plt.cm.gray, linewidth=2)
axis.view_init(80, 30)
plt.show()

# Rotating the plot
'''
for angle in range(0, 360):
    axis.view_init(30, angle)
    plt.draw()
    plt.pause(.001)
'''
