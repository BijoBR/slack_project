#  Write a program to convert prefix expression to infix expression


prefix_expression =input("Enter the expression start with 2 operator and two charcter operator and two charcter")

def prefix_to_infix(prefix_expression):
    stack = []
    operators = set('+-*/^')
    
    for char in reversed(prefix_expression):
        if char not in operators:
            stack.append(char)
        else:
            operand1 = stack.pop()  
            operand2 = stack.pop()
            infix_expression = f"({operand1}{char}{operand2})"
            stack.append(infix_expression)

    return stack[0]

infix_expression = prefix_to_infix(prefix_expression)

print("Prefix Expression:", prefix_expression)
print("Infix Expression:", infix_expression)