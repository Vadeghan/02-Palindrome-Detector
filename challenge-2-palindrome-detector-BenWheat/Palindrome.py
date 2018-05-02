phrase = input("Give me a phrase: ")

def palindrome(phrase):
    is_palindrome = True
    no_spaces = phrase.replace(" ", "")
    no_spaces = no_spaces.lower()
    length = len(no_spaces)
    for i in range(length//2):
        if no_spaces[i] != no_spaces[length-i-1]:
            is_palindrome = False
            
    if is_palindrome == False:
        print(phrase + " ain't a palindrome")
    if is_palindrome == True:
        print(phrase + " is a palindrome")

palindrome(phrase)

