def first_non_repeating_char(my_string):
    dictionary = {}
    
    for x in my_string :
        dictionary[x] = dictionary.get(x, 0) + 1
    
    nrc = []
  
    for x,y in dictionary.items():
        if y==1:
            nrc.append(x)
    
    if len(nrc)==0:
        return None
    else:
        return nrc[0]
    
    
            
    

print(first_non_repeating_char('leetcode'))

print(first_non_repeating_char('hello'))

print(first_non_repeating_char('aabbcc'))



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""