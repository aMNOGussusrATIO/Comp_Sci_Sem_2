sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
word = ""
whalecounter = 0

for x in range (len(sentence)):
    word = word + sentence[x]
    if sentence[x] == " ":
        if "Whale" in word or "whale" in word:
            whalecounter = whalecounter + 1
            word = ""
print("Amount of whales in sentence:" + str(whalecounter))

with open('moby.txt') as dick:
    whalecounter = 0
    for line in dick:
        sentence = line.strip()
        word = ""

        for x in range(len(sentence)):
            word = word + sentence[x]
            if sentence[x] == " ":
                if "Whale" in word or "whale" in word:
                    whalecounter = whalecounter + 1
                    word = ""
    print("Amount of whales in moby.txt:" + str(whalecounter))
    
dick.close()