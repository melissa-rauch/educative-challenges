# Node class for a Doubly linked list

class Node:
    def __init__(self, data):

        self.data = data
        self.previous = None
        self.next = None