
# 10) Write a program to find the smallest number using a stack.

class minstack:
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
    def minimum_value(self):
        size =int(input("Enter the sixe of the slack: "))
        for i in range(size):
            value =int(input("Enter the value to be append: "))
            obj.push(value)
        if self.item:    
            res= min(self.item) 
        print("minimum number is: ",res) 


obj=minstack()
obj.minimum_value()
