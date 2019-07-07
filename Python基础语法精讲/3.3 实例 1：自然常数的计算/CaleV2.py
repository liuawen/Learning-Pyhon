#CaleV2.py
from random import *
DARTS = 1024*1024
count = 0
for i in range(DARTS):
    x = uniform(1,2)
    y = uniform(0,1)
    if x*y < 1:
        count += 1
e = pow(2, DARTS/count)
print("{}".format(e))