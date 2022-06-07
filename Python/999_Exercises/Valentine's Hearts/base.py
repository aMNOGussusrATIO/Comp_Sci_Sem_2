import random

people_list = []
comp_list = []

with open('People.txt') as f:
    for line in f:
        l1 = line.strip()
        people_list.append(l1)
        
with open('Compliment.txt') as f:
    for line in f:
        l2 = line.strip()
        comp_list.append(l2)

num1 = random.randrange(100)
rand_comp = comp_list[num1]

num2 = random.randrange(24)
rand_people = people_list[num2]

print(rand_people + ", " + rand_comp)

f.close()
