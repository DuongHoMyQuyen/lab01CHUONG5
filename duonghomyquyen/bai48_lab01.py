# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 07:43:07 2024

@author: Student
"""

nho_nhat= 979
bo_nghiem=0
for x in range (1,490):
    for y in range(1,140):
        for z in range(1,109):
            if 2*x + 7*y + 9*z== 979:
                tong = x+y+z
                if tong < nho_nhat:
                    nho_nhat= tong
                    bo_nghiem= (x,y,z)
if bo_nghiem:
     print(f"{bo_nghiem} voi { x+y+z}= {nho_nhat}")