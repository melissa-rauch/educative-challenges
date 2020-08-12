# Implement a function that removes all the even elements from a given list. 
# Name it remove_even(list).

def remove_even(list):
    """ Input: my_list = [1,2,3,4,5,10,6,3]
        Output: my_list = [1,5,3]"""
    return [item for item in list if item % 2 !=0]

print(remove_even([1,2,3,4,5,10,6,3]))