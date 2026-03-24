def find_pairs(arr1, arr2, target) :
    
    lst = []
    
    arr1_set = set(arr1)
    
    for x in arr2 :
        complement = target - x
        
        if complement in arr1_set :
            lst.append((complement, x))
    return lst
            
    




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""