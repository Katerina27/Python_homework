from sys import argv

name, WorkTime, rate, bonus = argv

salary = int(WorkTime)*int(rate)+int(bonus)


print('salary = ' + str(salary))
