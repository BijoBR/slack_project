# 5) Write a recursive function to check if a given string is a palindrome.
word =input("Enter the word: ").lower()
rev =word
def palindrome(word):
    if word[::-1] == rev:
        print("Word is palindrome")
    else:
        print("Its not palindrome")
palindrome(word) 
