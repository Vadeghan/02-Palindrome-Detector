#Made by Marika Colby (12.10)

import re

QueryEnd = "\n  > "

#Test the text, including spaces; numbers; punctuation; and/or capitalised letters, to see if it is a palindrome.
def StrongPalindrome(text):
    if text == text[::-1]:
        return True
    return False

#Test only the letters and numbers in the text for palindrome-ness.
def WeakPalindrome(text):
    #Remove anything not in the range of a-z, A-Z, or 0-9.
    text = re.sub("[^a-zA-Z0-9]", "", text)
    #Make the text lower case.
    text = text.lower()
    if text == text[::-1]:
        return True
    return False

#Take an input of length greater than zero and return it as a string.
def StringInput(question):
    output = str(input(question + QueryEnd))
    while len(output) == 0:
        print("invalid input\n")
        output = str(input(question + QueryEnd))
    return output

#Accept one input from a specified list of inputs.
def CustomInput(question, inputs):
    extension = "("
    #Display available options as specified, but accept upper and lower case inputs.
    for index, item in enumerate(inputs):
        extension += item + "/"
        inputs[index] = inputs[index].lower()
    #Replace the final '/' of the extension with ')'
    extension = extension[0:-1] + ")"
        
    output = str(input(question + extension + QueryEnd))
    #Continue asking for input until the input is in the specified list.
    while not output.lower() in inputs:
        print("invalid input\n")
        output = str(input(question + extension + QueryEnd))
    return output


#script
while True:
    #Input the string to be tester.
    text = StringInput("\nWhat string would you like to test as a palindrome?")

    #If the string is not a palindrome through strong or weak testing, don't bother continuing.
    if not StrongPalindrome(text) and not WeakPalindrome(text):
        print("\nThe string '%s' is not at all a palindrome." % (text))
    #If the string is a palindrome through strong AND weak testing, don't bother continuing.
    elif StrongPalindrome(text) and WeakPalindrome(text):
        print("\nThe string '%s' is absolutely a palindrome!" % (text))

    #If the string is only a palindrome through strong or weak testing, then continue.
    else:
        #Ask if the string should be tested strongly or not.
        if CustomInput("\nShould this string be strictly tested?", ["Y", "N"]) == "y":

            if StrongPalindrome(text):
                print("\nThe string '%s' is a palindrome!" % (text))
            else:
                print("\nThe string '%s' is not a palindrome..." % (text))

        else:
            #If a weak test results in modifying the input before testing, also print what that modification was.
            if WeakPalindrome(text):

                if text == re.sub("[^a-zA-Z0-9]", "", text):
                    print("\nThe string '%s' is a palindrome!" % (text))
                else:
                    print("\nThe string '%s' (as '%s') is a palindrome!" % (text, re.sub("[^a-zA-Z0-9]", "", text)))

            else:
                if text == re.sub("[^a-zA-Z0-9]", "", text):
                    print("\nThe string '%s' is not a palindrome..." % (text))
                else:
                    print("\nThe string '%s' (as '%s') is not a palindrome..." % (text, re.sub("[^a-zA-Z0-9]", "", text)))

    print("\n------------------------------------------------\n")
