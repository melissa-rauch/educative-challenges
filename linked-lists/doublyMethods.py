from doublyLinked import Node, LinkedList


def get_head(self):
    return self.get_head
    
def is_empty(self):

    if (self.head) is None:
        return True
    else:
        return False

def insert_at_head(self,data):

    temp_node = Node(data)

    if (self.is_empty():
        self.head = temp_node
        return self.head
    
    temp_node.next = self.head
    self.head.previous = temp_node
    self.head = temp_node

    return self.head

def print_list(self):
    if (self.is_empty()):
        print("List is empty, no data to print")
        return False
    
    temp = self.head

    while temp.next is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print(temp.data, " -> None ")
    return True 
