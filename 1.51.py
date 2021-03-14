import math as mt

def area_of_a_triangle (x1, y1, x2, y2, x3, y3):
    s12 = mt.sqrt((x2-x1)**2 + (y2-y1)**2)
    s13 = mt.sqrt((x3-x1)**2 + (y3-y1)**2)
    s23 = mt.sqrt((x3-x2)**2 + (y3-y2)**2)

    p = s12 + s13 + s23
    p2 = (s12 + s13 + s23) / 2

    s = mt.sqrt(p2 * (p2-s12) * (p2-s13) * (p2-s23))
    
    return s


x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

x4 = int(input())
y4 = int(input())

s = area_of_a_triangle(x1, y1, x2, y2, x3, y3) + area_of_a_triangle(x1, y1, x4, y4, x3, y3)
print('s = ', s)
