a = int(input())

b = a + 10
c = a + 20


a, b, c = b, c, a

print(a, ' ', b, ' ', c)
