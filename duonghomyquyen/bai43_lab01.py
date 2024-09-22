# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:36:17 2024

@author: Student
"""

s= 0
n= int(input(("nhap n:")))
while n<=0:
    n= int(input("nhap lai n:"))
for i in range (1, n+1):
    s+= i/ (i +1)
print(round(s,2))