# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:52:53 2024

@author: Student
"""

s=0
n=int(input("Nhap n:"))
while n<=0:
    n=int(input("nhap lai n:"))
for i in range (1, 2*n):
    s+= 1/ 2*n
print(round(s,2))