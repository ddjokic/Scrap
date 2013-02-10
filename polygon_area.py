#!/usr/bin/env python
import inout

def area(corners, n):
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area
print("Corners must be ordered in Clockwise or Counter-Clockwise Direction!")
n=inout.get_integer("Number of corners or '0' for 3: ", 3)
corners=[]
for corner_nr in range(0, n,1):
	print ("Corner: "), corner_nr
	x=inout.get_float("Enter X coordinate: ", corner_nr)
	y=inout.get_float("Enter Y coordinate: ", corner_nr)
	coords=(x, y)
	corners.append(coords)
print("Polygon Area: "), area(corners,n)

