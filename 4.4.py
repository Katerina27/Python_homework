from random import randint

my_list = [randint(0, 25) for _ in range(randint(1, 15))]
print(my_list)

new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)