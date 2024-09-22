
"""
Created on Sun Sep 22 07:37:50 2024

@author: Student
"""

lon_nhat = 0
bo_nghiem = None
for x in range (1,490):
    for y in range (1,140):
        for z in range(1, 109):
            if 2*x + 7*y + 9*z ==979:
                tong = x+y+z
                if tong > lon_nhat:
                    tong= lon_nhat
                    bo_nghiem = (x,y,z)
if bo_nghiem:
    print(f"{bo_nghiem} voi { x+y+z}= {tong}")