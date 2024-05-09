a = 61

script1 = "は素数です"
script2 = "は素数ではありません"

import math
stop = math.floor(a ** 0.5)
investigation = list(range(2, stop+2))

for index, number in enumerate(investigation):
    if a%number == 0:
        break
    else:
        number += 1
        continue

if investigation[index] >= (a ** 0.5):
    print(str(a)+script1)
else:
    print(str(a)+script2)
    

b = 10

script1_ = "は素数です"
script2_ = "は素数ではありません"

import math
stop_ = math.floor(b ** 0.5)
investigation_ = list(range(2, stop_+2))

for index_, number_ in enumerate(investigation_):
    if b%number_ == 0:
        break
    else:
        number_ += 1
        continue

if ( investigation_[index_] >= (b ** 0.5) ) and b!=1:
    print(str(b)+script1_)
else:
    print(str(b)+script2_)