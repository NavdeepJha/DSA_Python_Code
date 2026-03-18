def selection_sort(my_list) :
    for i in range(len(my_list)-1) :
        
        min_index = i
        j = i 

        for j in range(i+1, len(my_list)) :
            
            if my_list[j] < my_list[min_index] :
                my_list[min_index], my_list[j] = my_list[j], my_list[min_index]

    return my_list

        





print(selection_sort([4,2,6,5,1,3]))


 
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

