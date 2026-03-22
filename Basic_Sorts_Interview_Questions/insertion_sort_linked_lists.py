def insertion_sort(self):
    # Check if the length of the list is less than 2
    if self.length < 2:
        return
    
    # Set the pointer to the first element of the sorted list
    sorted_list_head = self.head
    
    # Set the pointer to the second element of the list
    unsorted_list_head = self.head.next
    
    # Remove the first element from the sorted list
    sorted_list_head.next = None
    
    # Iterate through the unsorted list
    while unsorted_list_head is not None:
        # Save the current element
        current = unsorted_list_head
        
        # Move the pointer to the next element in the unsorted list
        unsorted_list_head = unsorted_list_head.next
        
        # Insert the current element into the sorted list
        if current.value < sorted_list_head.value:
            # If the current element is smaller than the first element 
            # in the sorted list, it becomes the new first element
            current.next = sorted_list_head
            sorted_list_head = current
        else:
            # Otherwise, search for the appropriate position to insert the current element
            search_pointer = sorted_list_head
            while search_pointer.next is not None and current.value > search_pointer.next.value:
                search_pointer = search_pointer.next
            current.next = search_pointer.next
            search_pointer.next = current
    
    # Update the head and tail of the list
    self.head = sorted_list_head
    temp = self.head
    while temp.next is not None:
        temp = temp.next
    self.tail = temp