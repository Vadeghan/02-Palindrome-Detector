#Made by Marika Colby (12.10)

text = "kayak"

def is_palindrome(text):
    if str(text) == str(text)[::-1]:
        return True
    return False

print(is_palindrome(text))
