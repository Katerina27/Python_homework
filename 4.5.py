from functools import reduce

def func (p_el, el):
    return p_el*el

my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(my_list)
print(reduce(func, my_list))
