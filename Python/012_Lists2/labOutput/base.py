import random
numberamnt = int(input("Amount of random numbers: "))
numberlist = []
for x in range(0,numberamnt):
    numberlist.append(random.randrange(1,10))
for x in range(0, numberamnt-1):
    print(numberlist[x], end=", ")
print(numberlist[numberamnt-1])