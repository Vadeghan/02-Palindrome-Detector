def is_palindrome(str):
    newstr = ""
    for char in str.lower():
        if char in ['qwertyuiopasdfghjklzxcvbnm1234567890']:
            newstr += char
    return newstr == newstr[::-1]

