# 4)Write a program to print the first non-repeated character from a string?


word = input("Enter the string: ").lower()

def non_repeated(word):
    count = {}

    for i in word:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for i in word:
        if count[i] == 1:
            return i
    
    return None

result = non_repeated(word)
print("Non repetative character",result)

# Enter the string: king
# k
