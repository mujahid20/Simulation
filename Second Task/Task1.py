# -*- coding: utf-8 -*-
"""simulationlabc3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xqvTwhw3_IP2xy5AEYubZtk7Dyv-XXdt
"""

import math
import random
import matplotlib.pyplot as plt

#size of rectangle

pi=[]
areacircle=[]



lst = [100,1000,5000,10000] 
  
# number of elemetns as input 
for m in lst:
  hits=0
  hitx=[]
  hity=[]
  missx=[]
  missy=[]
  for i in range (m):
    x=random.uniform(-5,5)
    y=random.uniform(-5,5)
    if math.sqrt(x**2+y**2)<=3:
      hits=hits+1
      hitx.append(x)
      hity.append(y)

    else:
      missx.append(x)
      missy.append(y)


  PIe= (100/9)* (hits/m)
  pi.append(PIe)
  areacirclec=100*(hits/m)
  areacircle.append(areacirclec)
  plt.scatter(hitx, hity, label= "Hit", color= "red",  marker= ".", s=200)
  plt.scatter(missx, missy, label= "miss", color= "Green",  marker= ".", s=200)
  plt.legend() 
  plt.show()

lst=[str(i) for i in lst]
plt.bar(lst, pi, width = 0.4, color = ['red', 'green']) 
plt.show()

plt.bar(lst, areacircle, width = 0.4, color = ['red', 'green']) 
plt.show()
print(pi)
print(areacircle)