import math

h = int(input('h='))
y = int(input('y='))

a = (math.tan(y ** 3 - h ** 4) + h ** 2) / (math.sin(h) ** 2 + y)
print(a)
