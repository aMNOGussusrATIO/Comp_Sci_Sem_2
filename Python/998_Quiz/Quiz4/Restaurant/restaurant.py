import random

restaurant = ["McDonalds", "Taco Bell", "In-N-Out"]

McDonaldsMenu = ["Big Mac", "McNuggets", "French Fries"]
TacoBellMenu = ["Taco", "Quesadilla", "Burrito"]
InNOutMenu = ["In N Out Burger", "In N Out Fries", "In N Out Shake"]

restaurantinput = input("What restaurant do you want? The options are: McDonalds, Taco Bell, In-N-Out ")

if restaurantinput == "McDonalds":
    print("Suggested item:")
    print(McDonaldsMenu[random.randrange(0,2)])
    McDonaldsMenuInput = input("What menu item do you want? The options are: Big Mac, McNuggets, French Fries ")

if restaurantinput == "Taco Bell":
    print("Suggested item:")
    print(TacoBellMenu[random.randrange(0,2)])
    TacoBellMenuInput = input("What menu item do you want? The options are: Taco, Quesadilla, Burrito ")
    
if restaurantinput == "In-N-Out":
    print("Suggested item:")
    print(InNOutMenu[random.randrange(0,2)])
    InNOutMenuInput = input("What menu item do you want? The options are: In N Out Burger, In N Out Fries, In N Out Shake ")