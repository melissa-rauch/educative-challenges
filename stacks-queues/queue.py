# Implementation of a Queue, using the example of a waitlist

class Queue():

    # Initialize an empty waitlist
    def __init__(self):
        self.waitlist = []

    # function to return a boolean the waitlist is empty or not
    def is_empty(self):
        # done by seeing if the size is equal to 0
        return self.size() == 0

    # function to return the size of the waitlist
    def size(self):
        # using length method return the size of the queue
        return len(self.waitlist)

    # function to return the element at the front of the waitlist
    def front(self):
        # if the waitlist is empty then return None
        if self.is_empty():
            return None
        # otherwise use the array[0] notation to return the element at front
        # of the queue (aka the first element in the array)
        return self.waitlist[0]

    # funtion to return the element at the back of the waitlist
    def back(self):
        # first, check if empty if so return none
        if self.is_empty():
            return None
        # return the element from back using array[-1] notation 
        # (aka the last element in the array)    
        return self.waitlist[-1]

    # function to add an element to the back of the queue
    def enqueue(self, value):
        # using array.append(value) method works for this
        self.waitlist.append(value)

    def dequeue(self):
        #first check if waitlist is empty, if so return none
        if self.is_empty():
            return None
        # using the self.front method to identify element to remove
        front = self.front()
        self.waitlist.remove(self.front())
        #return the removed element
        return front