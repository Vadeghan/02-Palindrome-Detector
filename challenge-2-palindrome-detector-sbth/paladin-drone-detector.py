# Import regex.
import re

# As per README, palindromes are made up of letters and numbers, and ignore
# punctuation and spacing.
# [^0-9a-z] is a regular expression:
#     0-9 means "match any characters that range from 0 to 9"
#     a-z means "match any characters from lowercase a to lowercase z"
#     ^ means "match all that are not in the expression"
#
# This means, "match anything that isn't a-z or 0-9", and replace it with ''.
# This removes anything that isn't alphanumerical.
#
# The string to be regex'd is inputted by the user and converted to lowercase.
s = re.sub('[^0-9a-z]', '', input('Enter a string: ').lower())

# Compare s to itself reversed, print bool result.
print(s == s[::-1])

