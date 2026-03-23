def item_in_common(list1, list2) :
    if len(list1) and len(list2) == 0 :
        return False
    else :
        for x in list1:
            if x in list2:
                return True
        return False
    




list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""