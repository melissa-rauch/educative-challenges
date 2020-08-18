# Implement a function called maxMin(lst) which will re-arrange the elements of a 
# sorted list such that the first position will have the largest number, the second 
# will have the smallest, and the third will have second largest, and so on. In other 
# words, all the odd-numbered indices will have the largest numbers in the list in 
# descending order and the even numbered indices will have the smallest numbers in 
# ascending order.

def max_min_1(lst):
    result = []
    # iterate half list
    for i in range(len(lst)//2):
        # Append corresponding last element
        result.append(lst[-(i+1)])
        # append current element
        result.append(lst[i])
    if len(lst) % 2:
        # if middle value then append
        result.append(lst[len(lst)//2])
    return result
print(max_min_1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

def max_min_2(lst):
    """Example:
            Input: a sorted list
                lst = [1,2,3,4,5]
            Output: a list with elements stored in max/min form
                lst = [5,1,4,2,3]
    """
    if (len(lst) is 0):
        return[]
    
    max_idx = len(lst) - 1
    min_idx = 0
    max_elem = lst[-1] + 1

    for i in range(len(lst)):
        if i % 2 == 0:
            lst[i] += (lst[max_idx] % max_elem) * max_elem
            max_idx -= 1
        else:
            lst[i] += (lst[min_idx] % max_elem) * max_elem
            min_idx += 1
    for i in range(len(lst)):
        lst[i] = lst[i] // max_elem
    
    return lst

print(max_min_2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

def foo(value, lst):
    value = 1
    lst[0] = 44
 
v = 3
lst = [1, 2, 3]
foo(v, lst)
print(v, lst[0])