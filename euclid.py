a = int(input("aの値"))
b = int(input("bの値"))

def euclid(a,b):
    if a > b:

        while True:
            if a % b == 0:
                break
            else:
                a, b= b, a%b
        return b
    elif a == b:
        return a
    else:
        while True:
            if b % a == 0:
                break
            else:
                b, a= a, b%a
        return a


def euclid_plus(a,b):
    return euclid(a,b)==1

result1 = euclid(a,b)
result2 = euclid_plus(a,b)
print(result1,result2)