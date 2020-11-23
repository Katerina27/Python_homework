my_list = []

# здесь должен быть общий цикл, который будет повторять ввод новых зачений
new=input('enter a few numbers, to stop program print "q" ')
new=new.split()   # убираем пробелы
a=len(new)      # вычисляем длину списка


# если в списке есть q, находим его индекс, значения до него суммируем и вставляем в общий список
# здесь написала slice, но он не работает со списками, не получилось просуммировать значения до
q=new.count('q')
if q!=0:
    new.index('q')
    i=0
    while q<i:
        new[i]=int(new[i])
        i+=1


    my_list.extend(new.slice[0:i:])
    print('total sum = ' + str((sum(my_list))))

# если q в списке нет, то просто переводим все значения в числа и суммируем, потом добавляем в новый список

else:
    i=0
    while a>i:
        new[i]=int(new[i])
        i+=1

    my_list.extend(new)
    print('sum of new list = ' + str((sum(new))) + ', total sum = ' + str((sum(my_list))))