# -*- coding: utf-8 -*-
"""Lib_Triadic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gAaW5qAe13ok87QMXdXW95yKyjuV_p15
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2
import math
from lib_color_conv import *

def MatchTriadic(Color):
  #Converting RGB values in to HSV
  Color1_HSV = rgb_to_hsv(Color)

  H_1 = abs((Color1_HSV[0]+120)%360)
  HSV_C1 = list(Color1_HSV)
  HSV_C1[0] = H_1

  #Color 2 from Triadic
  H_2 = abs((Color1_HSV[0]-120)%360)
  HSV_C2 = list(Color1_HSV)
  HSV_C2[0] = H_2

  HSV_B = list(Color1_HSV)

  Base_RGB = hsv_to_rgb(HSV_B)
  Triadic1_RGB = hsv_to_rgb(HSV_C1)
  Triadic2_RGB = hsv_to_rgb(HSV_C2)

  Palette = []
  Palette.append(Base_RGB)
  Palette.append(Triadic1_RGB)
  Palette.append(Triadic2_RGB)

  chart = np.zeros((50, 300, 3), dtype = "uint8")
  start = 0

  for i in range(len(Palette)):
    end = start + 100
    r = Palette[i][0]
    g = Palette[i][1]
    b = Palette[i][2]
    cv2.rectangle(chart, (int(start), 0), (int(end), 50), (r,g,b), -1)
    start = end	

  plt.figure()
  plt.axis("off")
  plt.imshow(chart)
  plt.show()

  return Palette