sec = int(input('enter seconds '))

hour = sec // 3600
minutes = sec % 3600 // 60
seconds = (sec % 3600) % 60
print(str(hour) + ':' + str(minutes) + ':' + str(seconds))
