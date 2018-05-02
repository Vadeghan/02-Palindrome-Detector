#Made by Marika Colby (12.10)

def is_palindrome(text):
    if str(text) == str(text)[::-1]:
        return True
    return False

def StringInput(question):
    output = str(input(question))
    while len(output) == 0:
        print("invalid input")
        output = str(input(question))
    return output

while True:
    text = StringInput("\nWhat string would you like to test as a palindrome?\n  > ")
    if is_palindrome(text):
        print("\nThe string '%s' is a palindrome!" % (text))
    else:
        print("\nThe string '%s' is not a palindrome..." % (text))
