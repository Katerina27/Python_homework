def my_func():
    var_1 = int(input('enter first number '))
    var_2 = int(input('enter second number '))
    var_3 = int(input('enter third number '))

    return var_1 + var_2 + var_3 - min(var_1, var_2, var_3)


print(my_func())
