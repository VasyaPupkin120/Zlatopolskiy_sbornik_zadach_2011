import math as mt

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

s12 = mt.sqrt((x2-x1)**2 + (y2-y1)**2)
s13 = mt.sqrt((x3-x1)**2 + (y3-y1)**2)
s23 = mt.sqrt((x3-x2)**2 + (y3-y2)**2)

p = s12 + s13 + s23
p2 = (s12 + s13 + s23) / 2

s = mt.sqrt(p2 * (p2-s12) * (p2-s13) * (p2-s23))
print('s = ', s, '    p = ', p)
