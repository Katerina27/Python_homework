from itertools import cycle
from random import randint

i = 0
for el in cycle([randint(0, 25) for _ in range(randint(1, 5))]):
    if i > 10:
        break
    else:
        print(el)
    i += 1
