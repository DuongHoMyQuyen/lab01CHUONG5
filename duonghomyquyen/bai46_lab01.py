# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 06:49:49 2024

@author: Student
"""

ds=[]
for x in range(1, 490):
    for y in range(1,140):
        for z in range(1,109):
            if 2*x + 7*y + 9*z == 979:
                ds+= [(x,y,z)]
if ds:
    print(f"{ds}")
        