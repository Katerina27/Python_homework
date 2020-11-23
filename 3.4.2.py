x = int(input('enter x > 0 '))
y = int(input('enter y as integer < 0 '))
if x <= 0 or y >= 0:
    print('enter correct numbers')
else:
    def my_func(x, y):

        i = 0
        n = 1
        while abs(y) > i:
            n = n * (1 / x)
            i += 1
        return n

    print(my_func(x, y))
