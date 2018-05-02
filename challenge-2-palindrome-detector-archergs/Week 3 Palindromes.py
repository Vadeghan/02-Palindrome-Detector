def is_palindrome():
    palin = input("Enter your word to find out if it is a palindrome: ")
    is_it = palin[::-1]
    if is_it == palin:
        print("Your word is a palindrome!")

    if is_it != palin:
        print(palin + " is not a palindrome")

is_palindrome()
    
