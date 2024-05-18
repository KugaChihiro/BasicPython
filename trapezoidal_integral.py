import math

def trapezoidal_integral(f=math.sin,a=0,b=1,n=100):
    section = (b-a) / n
    value_list = []
    for x in list(range(1, n+1)):
        area = section * (f(a + (x-1)*section) + f(a + x*section)) * 0.5
        value_list.append(area)
    return(sum(value_list))

    
result_1 = trapezoidal_integral(math.sin,0,math.pi*0.5,50)
print(result_1)


def function_1(x):
    return 4/(1 + x**2)
F1 = function_1
result_2 = trapezoidal_integral(F1,0,1,100)
print(result_2)

def function_2(x):
    return (math.pi**0.5) * (math.e**((x**2)*(-1)))
F2 = function_2
result_3 = trapezoidal_integral(F2,-100,100,1000)
print(result_3)