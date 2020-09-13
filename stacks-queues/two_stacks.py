from stack import Stack

# Implement the following functions using a single array such that for sorting
# elements, both stacks should use the same array.

class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * n
        self.top_stack1 = -1
        self.top_stack2 = self.size
    
    # Method to push an element to stack 1:
    def push1(self, value):
        # if stack1 is less than stack 2 -1
        if self.top_stack1 < self.top_stack2 - 1:
            # add 1 to stack 1
            self.top_stack1 = self.top_stack1 + 1
            # assign the space in the array where stack 1 is to the value
            self.arr[self.top_stack1] = value
        # otherwise print an error message of stack overflow    
        else:
            print("Stack Overflow")
            exit(1)

    #method to push an element to stack 2 (opposite of push1)
    def push2(self, value):

        if self.top_stack2 < self.top_stack1 - 1:
            self.top_stack2 = self.top_stack2 - 1 # here it needs to subtract 1
            self.arr[self.top_stack2] = value
        else:
            print("Stack Overflow")
            exit(1)     

    # Method to remove and element from the first stack:
    def pop1(self):

        if self.top_stack1 >= 0 :
            value = self.arr[self.top_stack1]
            self.top_stack1 = self.top_stack1 - 1
            return value
        else:
            print("Stack Underflow")
            exit(1)

    def pop2(self):

        if self.top_stack2 < self.size: # because this is its parameter
            value = self.arr[self.top_stack2]
            self.top_stack2 = self.top_stack2 + 1
            return value
        else:
            print("Stack Underflow")
            exit(1)

