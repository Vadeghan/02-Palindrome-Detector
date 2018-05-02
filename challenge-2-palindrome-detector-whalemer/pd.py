#!/usr/bin/env python3

strict_palindrome = lambda x: str(x) == str(x)[::-1] #pretty simple, just uses string slicing to reverse

def nonstrict_palindrome(x):
    x_strip = [i.lower() for i in str(x) if i.isalpha()] #why does isalpha exist?
    if not x_strip: return False #"" is not a palindrome
    return x_strip == x_strip[::-1]
