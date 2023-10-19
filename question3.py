# 3)Write a program to check if two strings are a rotation of each other

string1 =input("Enter the string1: ")
string2 =input("Enter the string2: ")
def roation():
    if len(string1)!=len(string2):
        print("Both are not rotational")
    else:
        add =string1+string2
        if string2 in add:
            print("Both the string are rotational")    
roation()