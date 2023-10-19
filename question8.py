#  8)Write a program to check if all the brackets are closed in a given code snippet.


code =input("Enter the code: ")
def are_brackets_closed(code):
    brackets = {'(': ')', '[': ']', '{': '}'}
    key_stack =[]
    value_stack = []


    for char in code:
        if char in brackets.keys():
            key_stack.append(char)
    for char in code:        
        if char in brackets.values():
            value_stack.append(char)
    if len(key_stack)==len(value_stack):
        print("All the bracket are closed")
    else:
        print("All the barcket are not properly closed")  
are_brackets_closed(code)  
