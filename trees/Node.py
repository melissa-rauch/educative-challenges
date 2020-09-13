class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.parent = None
    
    def insert(self,val):
        current = self
        parent = None

        # while current isn't Nothing
        while current:
            # set parent to the current node
            parent = current
            # if the input val is less than the current node val
            if val < current.val:
                # set leftChild to the current
                current = current.leftChild
            else:
                # set rightChild to current
                current = current.rightChild
        
        # If the input val is less than parent val
        if  (val < parent.val):
            # set parent's leftChild to Node(val)
            parent.leftChild = Node(val)
            
        else:
            # set parents rightChild to Node(Val)
            parent.rightChild = Node(val)