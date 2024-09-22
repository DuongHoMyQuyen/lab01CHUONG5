# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:54:15 2024

@author: Student
"""


s=0
n=int(input("Nhap n:"))
while n<=0:
    n=int(input("nhap lai n:"))
for i in range (1, n):
    s+= 1/ n
print(round(s,2))