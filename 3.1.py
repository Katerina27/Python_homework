def my_func():
  return var_1 / var_2

try:
    var_1 = int(input('enter first number '))
    var_2 = int(input('enter second number '))
    print(var_1/var_2)
except ValueError:
    print('You should enter integer')
except ZeroDivisionError:
    print("Impossible divide in 0")