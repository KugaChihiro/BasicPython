

import math
def prime_number(n):
    upper_limit = math.floor(n ** 0.5)
    for index, number in enumerate(list(range(2, upper_limit+2))):
        remain = n % number
        if  remain == 0:
            break
        else:
            number += 1
            continue 
    print(list(range(2, upper_limit+2))[index] >= (n ** 0.5) and (n != 1))
    
result = prime_number()