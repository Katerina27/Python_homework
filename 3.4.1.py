x = int(input('enter x > 0 '))
y = int(input('enter y as integer < 0 '))
if x <= 0 or y >= 0:
    print('enter correct numbers')
else:
    def my_func(x, y):
        return 1/(x**abs(y))

    print(my_func(x,y))
