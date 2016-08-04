fibs = [0,1]
numZS = input('\nHow many Fibonacci numbers do you want?\n')
for i in range(numZS-2):
    fibs.append(fibs[-2]+fibs[-1])
print fibs
