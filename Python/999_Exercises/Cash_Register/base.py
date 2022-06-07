amnt = int(input("How many items do you want to buy? "))
itemslist = []
pricelist = []

for x in range(0,amnt):
    item = input("What item are you buying? ")
    price = float(input("What is the price of the item? "))
    itemslist.append(item)
    pricelist.append(price)

for x in itemslist:
    print(x)
print ("your total: ", end = "")
total = 0
for x in pricelist:
    total = total+x
print(total)