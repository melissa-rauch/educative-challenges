# We need to insert a new object at the end of the linked list. You can naturally guess, 
# that this newly added node will point to None as it is at the tail.

from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Inserts a value at the end of the list
class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


def insert_at_tail(lst, value):
    """Example:
                Input: A linked list and an integer value
                Output: The updated linked list with the value inserted
        Sample input:
            lst = 0->1->2
            value = 3
        Sample output:
            lst 0->1->2->3
    """
    #Create a new node
    new_node = Node(value)

    #Check if list is empty, if so point head to new node
    if lst.is_empty():
        lst.head_node = new_node
        return
    else:
        current = lst.get_head()
        while current.next_element:
            current = current.next_element
        current.next_element = new_node

        return 