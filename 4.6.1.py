from itertools import count
from random import randint

for el in count(randint(1, 100), 5):
    if el > 100:
        break
    else:
        print(el)
