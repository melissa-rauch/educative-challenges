# Implement a function, find_first_unique(lst) that returns 
# the first unique integer in the list.
def find_first_unique(lst):
    """Example:
            Input: [9,2,3,2,6,6]
            Output: 9
    """
    counts = {} # Create a dictionary
    #initialize dictionary with pairs like (lst[0], 0)
    counts = counts.fromkeys(lst, 0)

    for ele in lst:
        counts[ele] += 1

    for ele in lst:
        if counts[ele] <= 1:
            return ele

    return None
print(find_first_unique([4,5,1,2,0,4]))