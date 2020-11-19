my_list = [9, 8, 7, 5, 5, 4]

n = int(input('enter a number '))

if n > my_list[0]:
    my_list.insert(0, n)
    print(my_list)
elif n < my_list[-1]:
    my_list.insert((len(my_list) + 1), n)
    print(my_list)
elif my_list.index(n) > 0:
    my_list.insert((my_list.index(n) + my_list.count(n)), n)
    print(my_list)
else:
    i = 0
    while True:
        i += 1
        if my_list[i] > n:
            continue
        if my_list[i] < n:
            break
        print(i)
    my_list.insert((i - 1), n)
    print(my_list)
