def decide(word):
    if word[0] == word[-1]:
        if word[1] == word[-2]:
            if word[2] == word[-3]:
                if word[3] == word[-4]:
                    if word[4] == word[-5]:
                        print("It is a Paladrome")
    else:
        print("It is not a Paladrome")

while True:
    userInput = list(input('input a string'))
    decide(userInput)
