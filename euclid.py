def euclid(x,y):
    if x > y:

        while True:
            if x % y == 0:
                break
            else:
                x, y= y, x%y
        print(y)
    elif x == y:
        print(x)
    else:
        while True:
            if y % x == 0:
                break
            else:
                y, x= x, y%x
        print(x)


def euclid_plus(a,b):
    print(euclid(a,b) == 1)


result = euclid_plus()