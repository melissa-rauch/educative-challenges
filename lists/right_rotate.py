# Implement a function right_rotate(lst, n) which will rotate the given list by k. 
# This means that the right-most elements will appear at the left-most position 
# in the list and so on. You only have to rotate the list by one element at a 
# time.

def right_rotate(lst,n):
    """Example:
        Input: a list and a number by which to rotate that list
            lst = [10,20,30,40,50]
            n = 3
        Output: the given list rotated by k elements
            [30,40,50,10,20]
    """
    # n = n % len(lst)
    # print(n)
    return lst[-n:] + lst[:-n]

print(right_rotate([300, -1, 3, 0], 3))