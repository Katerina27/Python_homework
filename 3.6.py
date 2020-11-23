words=input('enter a few words ')

words=words.split()
a=len(words)

el_1=words[0]
el_1 = list(el_1)
for item in el_1:
    if ord(item)>=97 and ord(item)<=122:
        print(1)
    else:
        print(0)




print(el_1)