revenue = int(input('enter revenue '))
costs = int(input('enter costs '))
profit = revenue-costs
print('Financial result = ' + str(profit))

if profit >0:
    ROR = profit/revenue*100
    empl = int(input('enter number of employees '))
    PpP = profit/empl
    print('ROR = ' + str(ROR) + ' %')
    print('Profit per person = ' + str(PpP))

