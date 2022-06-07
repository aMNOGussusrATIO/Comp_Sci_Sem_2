favnumsentence = input("state your favorite number in an independent sentence (max 3 digits): ")
age = input("state your age: ")

number1 = 0
number2 = 0
number3 = 0
num1 = 0
num2 = 0
num3 = 0
if int(len(favnumsentence)) == 23:
    for x in range (0,9):
        if int(favnumsentence[22:23]) == num:
            number1 = num
            break
        num = num + 1
    print(number1)
    
if int(len(favnumsentence)) == 24:
    for x in range (0,9):
        if int(favnumsentence[22:23]) == num1:
            number1 = num1
            break
        num1 = num1 + 1
    for x in range (0,9):
        if int(favnumsentence[23:24]) == num2:
            number2 = num2
            break
        num2 = num2 + 1
    print(number1, end = "")
    print(number2)
 
if int(len(favnumsentence)) == 25:
    for x in range (0,9):
        if int(favnumsentence[22:23]) == num1:
            number1 = num1
            break
        num1 = num1 + 1
    for x in range (0,9):
        if int(favnumsentence[23:24]) == num2:
            number2 = num2
            break
        num2 = num2 + 1
    for x in range (0,9):
        if int(favnumsentence[23:24]) == num3:
            number3 = num3
            break
        num3 = num3 + 1
    print(number1, end = "")
    print(number2, end = "")
    print(number3)
    
    
    
