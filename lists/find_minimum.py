# Implement a function findMinimum(lst) which finds the 
# smallest number in the given list.
def find_minimum(arr):
    """ O(nlogn) Runtime:
        Example:
                Input: arr = [9,2,3,6]
                Output: 2
    """
    if (len(arr) <= 0):
        return None
    arr.sort()
    return arr[0]

print(find_minimum([9,2,3,6]))

def find_minimum_b(arr):
    """ O(n) Runtime:
        Example:
                Input: arr = [9,2,3,6]
                Output: 2
    """
    if (len(arr) <= 0):
        return None
    minimum = arr[0]

    for ele in arr:
        if ele < minimum:
            minimum = ele

    return minimum

print(find_minimum_b([9,2,3,6]))