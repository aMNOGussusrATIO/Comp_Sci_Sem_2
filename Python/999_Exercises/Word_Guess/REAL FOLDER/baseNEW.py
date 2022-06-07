wordlist = []

import random
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        wordlist.append(l)
        
num = random.randrange(12972)
answer = wordlist[num]

a = 0
guessamnt = 6
for i in range(0,6):
    guess = input("Guess a 5 letter word, you have " + str(guessamnt) + " tries! ")
    guessamnt = guessamnt - 1
    if guess == answer:
        print("You won!!!")
        a = 1
        break
    else:
        print("guess again!")
if a == 0:
    print("You lost, also, now you have a gambling addiction. L bozo, the word was " + answer)