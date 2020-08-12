# In this problem, you have to implement the find_sum(lst,k) function which will 
# take a number k as input and return two numbers that add up to k.

def find_sum_a(lst, k):
    """BRUTE FORCE
        Example 
        Input:
                lst = [1,21,3,14,5,60,7,6]
                k = 81
        Output: 
                lst = [21,60]"""
    idx1= 0
    idx2= 0
    two_nums = []

    while idx2 < len(lst) -1:
        while idx1 < len(lst)-1:
            
            if (lst[idx1] + lst[idx2]) == k:
                two_nums.append(lst[idx2])
                two_nums.append(lst[idx1])
                return two_nums
            else:
                idx1 += 1
                
        if (lst[idx1] + lst[idx2]) == k:
            return two_nums
        else:    
            idx1 = 0
            idx2 += 1  

print(find_sum_a([1,21,3,14,5,60,7,6], 81))

def find_sum_b(lst, k):
    """SORT & MOVE INDICES
        Example 
        Input:
                lst = [1,21,3,14,5,60,7,6]
                k = 81
        Output: 
                lst = [21,60]"""
    lst.sort()
    index1 = 0
    index2 = len(lst) -1
    result = []

    while (index1 != index2):
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    return False

print(find_sum_b([1,21,3,14,5,60,7,6], 81))
