# Implement a function rearrange(lst) which rearranges the elements such that 
# all the negative elements appear on the left and positive elements appear 
# at the right of the list. Note that it is not necessary to maintain the 
# order of the input list.
def rearrange(lst):
    """Example:
        Input: a list
            [10,-1,20,4,5,-9,-6]
        Output: a list with negative elements at the left end and positive on right
            [-1,-9,-6,10,20,4,5]
    """
    neg = []
    pos = []

    for i in lst:
        if i < 0:
            neg.append(i)

    for i in lst:
        if i >= 0:
            pos.append(i)

    return neg + pos

print(rearrange([10,-1,20,4,5,-9,-6]))
