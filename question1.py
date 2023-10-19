# Write a program to find all pairs of an integer array whose sum is equal to a given number?


def sum_pair():
    size = int(input("Enter the size of the list: "))
    lst = []
    
    for i in range(size):
        value = int(input(f"Enter the value for list {i + 1}: "))
        lst.append(value)
        
    target_number = int(input("Enter the number to find pairs that sum to: "))
    
    unique_pairs = set()
    
    for i in range(size):
        for j in range(i + 1, size):
            if lst[i] + lst[j] == target_number:
                pair = (lst[i], lst[j])
                unique_pairs.add(pair)
    if unique_pairs:
        for pair in unique_pairs:
            print(pair)
    else:
        print("No pairs found that sum to", target_number)

sum_pair() 