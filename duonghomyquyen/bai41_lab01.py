# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:49:14 2024

@author: Student
"""

s=0
n=int(input("Nhap n:"))
while n<=0:
    n=int(input("nhap lai n:"))
for i in range (1, 2*(n+1)):
    s+= 1/ 2*i+1
print(round(s,2))