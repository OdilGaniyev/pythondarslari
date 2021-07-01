# uchburchakning ikki tomoni bor a, b va ular orasidagi burchak berilgan
# uchburchakning uchunchi tomonini toping c=?

import math

a = int(input('a='))
b = int(input('b='))
x = int(input('x='))

x_radian = x / 180 * math.pi

c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(x_radian))
print(c)
