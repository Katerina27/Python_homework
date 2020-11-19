a=int(input('enter number of km today '))
b=int(input('enter number of km desire '))

day =1
i=a
while True:
    i=0.1*i+i
    day +=1
    if i>=b:
        break
    if i<b:
        continue
print(day)
