from math import sin
import math

a = 0
b = math.pi*0.5
n = 100

section = (b-a) / n
value_list = []

for x in list(range(1, n+1)):
    area = section * (sin(a + (x-1)*section) + sin(a + x*section)) * 0.5
    value_list.append(area)
    
answer = sum(value_list)
print(answer)