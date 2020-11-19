winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

m=int(input('enter number of month '))
if winter.count(m) == True:
    print("it's winter")
elif spring.count(m) == True:
    print("it's spring")
elif summer.count(m) == True:
    print("it's summer")
elif autumn.count(m) == True:
    print("it's autumn")
else: print("incorrect number")
