from math import sin
import math

a = 0
b = math.pi*0.5

section = (b-a) / 100
value_list = []

for x in list(range(a, 100)):
    area = section * (sin(a+(x-1)*section) + sin(x*section)) * 0.5
    value_list.append(area)
    
answer = sum(value_list)
print(answer)