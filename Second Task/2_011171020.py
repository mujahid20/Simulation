# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tkqSD9_e5W-PkYya_e2sqb87nGH8oo96
"""

import math
import random
import matplotlib.pyplot as plt

#size of rectangle

areatri=[]



lst = [100,1000,5000,10000] 
  
# number of elemetns as input 
for m in lst:
  hits=0
  hitx=[]
  hity=[]
  missx=[]
  missy=[]
  for i in range (m):
    x=random.uniform(0,3)
    y=random.uniform(0,5)
    if y<=x+2:
      hits=hits+1
      hitx.append(x)
      hity.append(y)

    else:
      missx.append(x)
      missy.append(y)


  areatric=15*(hits/m)
  print(areatric)
  areatri.append(areatric)
  plt.scatter(hitx, hity, label= "Hit", color= "red")
  plt.scatter(missx, missy, label= "miss", color= "Green")
  plt.legend() 
  plt.show()