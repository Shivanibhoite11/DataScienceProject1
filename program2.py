# Program to check whether a string is palindrome

string = input("Enter a string: ")

reverse_string = string[::-1]

if string == reverse_string:
    print("The given string is a Palindrome")
else:
    print("The given string is not a Palindrome")