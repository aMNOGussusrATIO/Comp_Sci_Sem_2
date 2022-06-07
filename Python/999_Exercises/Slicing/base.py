name = input("What is your first and last name? ")

lastletter = len(name)
namestart = 0
nameend = 1

for x in range (0, lastletter):
    nameslicer = name[namestart:nameend]
    print(nameslicer)
    namestart = namestart + 1
    nameend = nameend + 1
    
for space in range(0,len(name)):
    y = name[space:space + 1]
    x = " "
    if y == x:
        name1 = name[space:len(name)]
        name2 = name[0:space]
        print(name1 + ", " + name2)