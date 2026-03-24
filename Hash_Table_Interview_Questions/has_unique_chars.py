def has_unique_chars(strings) :
    distinct_val = set(strings)
    len_set = len(distinct_val)
    
    len_list = len(strings)
    
    if len_list == len_set :
        return True
    else:
        return False



print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""