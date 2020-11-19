n = int(input('enter n '))

i = 0
while True:
    r = n % 10
    n = n // 10
    if r <= i:
        i=r
    if r > i:
        break
        print(r)
