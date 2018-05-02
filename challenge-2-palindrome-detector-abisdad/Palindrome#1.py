# Create a function to check if input is a palindrome...
# Palindrome#1.py
# By Rob Thomas
# 6/11/2017
# Ver 1.0

def palindrome(phrase):
    palin=False
    print("Phrase len/2 is",len(phrase)/2)
    for i in range(int(len(phrase)/2)):
        print(phrase[i], end="")
        print(phrase[len(phrase)-i-1])
        if phrase[i]==phrase[len(phrase)-i-1]:
            print("Match!")
            palin=True
        else:
            palin=False
            break
    if palin:
        print("PALINDROME!")
        return True
    else:
        print("NOT")
        return False
        
while True:
    word=input("Enter a word: ")
    palindrome(word)
        
        
