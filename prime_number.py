n = int(input("整数値")) 

import math
def prime_number(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    upper_limit = math.isqrt(n)
    for number in range(3, upper_limit+1, 2):
        if n % number == 0:
            return False
    return True


result = prime_number(n)
print(result)