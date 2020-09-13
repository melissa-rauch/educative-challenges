# Implement a stack, using the example of cars in a driveway

class Stack():
    # initialize a carStack object
    def __init__(self):
        self.car_list = []
    
    # function to return Boolean whether the list of objects is empty or not
    def is_empty(self):
        # use .size() function for stacks to get the size of the stack
        return self.size() == 0
    
    # function to return the object at the top of the stack
    def top(self):
        # first, if the stack is empty, return None
        # otherwise return the very last object in the array(first item of the stack)
        if self.is_empty():
            return None
        return self.car_list[-1]

    # function to return the size of the stack
    def size(self):
        # by finding the length of the car list
        return len(self.car_list)
    
    # function to add an element to the top of the stack
    def push(self,value):
        # needs to append to the list a value
        self.car_list.append(value)

    # function to remove and return the top element from the stack
    def pop(self):
        # first check if the stack is empty, if so return None
        if self.is_empty():
            return None
        # otherwise remove last object in the array as you would normally do
        return self.car_list.pop()
