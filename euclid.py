x_list = [10, 14, 91]
y_list = [20, 91, 14]

for x,y in zip(x_list, y_list):
    
    if x > y:
        while True:
            if x % y == 0:
                break
            else:
                x, y= y, x%y
        print(y)
    elif x == y:
        break
        print(x)
    else:
        while True:
            if y % x == 0:
                break
            else:
                y, x= x, y%x
        print(x)
