# Implement a function, find_product(lst), which modifies a list so that each index has a 
# product of all the numbers present in the list except the number stored at that index.

def find_product(lst):
    """Example:
                Input: A list of numbers (could be floating points or integers)
                    arr = [1,2,3,4]
                Output: A list such that each index has a product of all the numbers 
                in the list except the number stored at that index.
                    arr = [24,12,8,6]
                """
    #get product starting from left
    product = []
    left = 1
    for element in lst:
        product.append(left)
        left = left * element
    #get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]
    
    return product
    
    
print(find_product([1,2,3,4]))