n=input('enter a few words ')

n=n.split()

for ind, el in enumerate(n, 1):
    print(ind, el[0:9:1])