# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:29:50 2024

@author: Student
"""

s=0
ts=1
ms=0
n= int(input("nhap n:"))
while n<=0:
    n=int(input("nhap lai n:"))
x= float(input("nhap x:"))
for i in range(1, n+1):
    ts= x**1
    ms=ms +i
    s+= ts/ms
print(round(s,2))