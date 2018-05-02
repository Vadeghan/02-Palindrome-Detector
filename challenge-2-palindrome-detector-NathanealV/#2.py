# IMPORTS
import sys, os ,string

# A palindrome is a word or a number which reads backwards and forwards

#Define is_palindrome function
def is_palindrome(rword):
    #get rid of all whitespaces
    nwword = rword.replace(' ', '') #nwword is for No Whitespace Word

    #FOR DEBUG
    #print(nwword)

    #put all punctuation into a variable
    punct = set(string.punctuation)
    # remove all punctuation from word
    word = ''.join(x for x in nwword if x not in punct)

    #FOR DEBUG
    #print(word)
    
    #make new empty list
    palindrome_list_backwards = []

    #make a list from the word starting from the last letter and add to list
    for c in word[::-1]:
        palindrome_list_backwards.append(c) #c is for character

    #FOR DEBUG
    #print(palindrome_list_backwards)

    #concatenate the list into one word
    back_word = ''.join(palindrome_list_backwards)

    #FOR DEBUG
    #print(back_word)

    #check if the word spelled backwards is the same as the word
    if back_word == word:
        if word.isdigit():
            print("Yes. :)")
            print("The number, " + word.upper() + ", is a palindrome.")
        #if it is say that the word is a palindrome
        else:
            print("Yes. :)")
            print("The word, " + word.upper() + ", is a palindrome.")
    else:
        if word.isdigit():
            print("NO. :)")
            print("The number, " + word.upper() + ", is not a palindrome.")
        #if it is not say that the word is not a palindrome
        else:
            print("No. :(")
            print("The word, " + word.upper() + ", is not a palindrome.")

#On Loop
while True:

    print("####################################################")
    print("This palindrome checker works with words and numbers")
    print("####################################################")
    print("\n\n")

    #Get input from user of which word to check
    root_word = input("Palindrome to be checked: ")
    print("--------------------------------------")

    #Convert word to lower case and run above function
    is_palindrome(root_word.lower())
    print("--------------------------------------")

    #Ask if they have another word to check
    restart = input("Run again (y/n): ")

    #If not, exit
    if restart == "n":
        sys.exit()

    #Else continue and start again
    else:
        os.system("cls")
        continue

