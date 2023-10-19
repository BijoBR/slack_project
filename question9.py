#  9)Write a program to reverse a stack.

class stack:
    def __init__(self):
        self.item =[]
        self.reversse_slack = []
    def is_empty(self):
        return len(self.item) ==0
    def push(self,item=None):
        self.item.append(item)
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
    def peek(self):
        return self.item[-1]
    def itemss (self):
        return self.item
    def reverse(self):
        size =int(input("Enter the size of the slack: "))
        for i in range(size):
            value =int(input("Enter the value to be append: "))
            obj.push(value)
        reversed_stack = []
        while not self.is_empty():
            reversed_stack.append(self.pop())

        return reversed_stack
            
obj = stack()
reversed_stack = obj.reverse()

print("Reversed stack:", reversed_stack)