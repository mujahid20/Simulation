# -*- coding: utf-8 -*-
"""simuc4task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DiDeUvV2CjUpuyGQX71W4vul1mLCLaWO
"""

import math
import random
import matplotlib.pyplot as plt

lst = [100,1000,5000,10000] 
  
# number of elemetns as input 
for m in lst:
  sum=0
  sqsum=0

  for i in range (m):
    x=random.uniform(0,8)
    if x<=4:
      func= math.sqrt(4*x)
      sum=sum+func
      sqsum=sqsum+ (func**2)

    else:
      func= 8-x
      sum=sum+func
      sqsum=sqsum+ (func**2)
  
  funcavg=sum/m
  sqfuncavg= sqsum/m
  intvalue= funcavg*(8-0)
  error=((8-0)/ math.sqrt(m))*math.sqrt(sqfuncavg-(funcavg**2))
  print("area: " ,intvalue)
  print("Estimated error:" ,error)