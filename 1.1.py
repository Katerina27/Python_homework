city = input('Enter city ')
hour = int(input('Enter current hour '))

if city == 'Kaliningrad':
    print(hour -1)
elif city == 'Vladivostok':
    print(hour+7)
elif city == 'Krasnoyarsk':
    print(hour+4)
elif city == 'Samara':
    print(hour + 1)
else:
    print('find it in the catalog')
