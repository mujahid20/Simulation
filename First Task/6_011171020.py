# -*- coding: utf-8 -*-
"""simu6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f0Hyne6JEN8_paDjJ5fUigxNYbYOkNfy
"""

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThird=[]

for i in range(len(listOne)):
  if(i%2==1):
    listThird.append(listOne[i])
print("Element at odd-index positions from list one:",listThird)
listEven=[]
for i in range(len(listTwo)):
  if(i%2==0):
    listEven.append(listTwo[i])
    listThird.append(listTwo[i])
print("Element at even-index positions from list two:",listEven)
print("Printing Final third list",listThird)

