# Implement a function find_second_maximum(lst) which returns 
# the second largest element in the list.
def find_second_maximum(lst):
    """Example:
        Input: a list
            [9,2,3,6]
        Output: second largest element in the list
            6
    """
    lst.sort()
    if len(lst) >= 2:
        return lst[-2]
    else:
        return None
            
print(find_second_maximum([9,2,3,6]))