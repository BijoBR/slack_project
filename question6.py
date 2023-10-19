# 6)Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def postfix_to_prefix(post):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for opr in post.split():
        if opr not in operators:
            stack.append(opr)
        else:
            var2 = stack.pop()
            var1 = stack.pop()
            pre = opr + var1 + var2
            stack.append(pre)

    return stack[0]

post = input("Enter a postfix expression separated by spaces: ")
pre = postfix_to_prefix(post)
print("Th Prefix expression is:", pre)