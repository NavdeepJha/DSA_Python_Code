class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

        
    def partition_list(self, x):
        # ------------------------------------------------
        # If the list is empty, return immediately
        # Nothing to partition
        # ------------------------------------------------
        if not self.head:
            return None
 
        # ------------------------------------------------
        # Create two dummy nodes to serve as the starting
        # points for the two new partitions
        # dummy1 → nodes with values < x
        # dummy2 → nodes with values ≥ x
        # ------------------------------------------------
        dummy1 = Node(0)
        dummy2 = Node(0)
    
        # ------------------------------------------------
        # prev1 tracks the end of the < x partition
        # prev2 tracks the end of the ≥ x partition
        # ------------------------------------------------
        prev1 = dummy1
        prev2 = dummy2
    
        # Start at the head of the original list
        current = self.head
    
        # ------------------------------------------------
        # Traverse the original list and divide nodes
        # into two separate partitions based on their value
        # ------------------------------------------------
        while current:
            if current.value < x:
                # ----------------------------------------
                # Append current node to the < x list
                # Update pointers to maintain .next/.prev
                # ----------------------------------------
                prev1.next = current
                current.prev = prev1
                prev1 = current
            else:
                # ----------------------------------------
                # Append current node to the ≥ x list
                # Update pointers to maintain .next/.prev
                # ----------------------------------------
                prev2.next = current
                current.prev = prev2
                prev2 = current
 
            # Move to the next node in the original list
            current = current.next
 
        # ------------------------------------------------
        # Terminate the ≥ x list to prevent cycle or
        # trailing data from previous .next values
        # ------------------------------------------------
        prev2.next = None
    
        # ------------------------------------------------
        # Connect the two partitions:
        # Link the end of the < x list to the beginning
        # of the ≥ x list
        # ------------------------------------------------
        prev1.next = dummy2.next
    
        # ------------------------------------------------
        # If the ≥ x list has at least one node,
        # update its .prev to point to the < x list
        # ------------------------------------------------
        if dummy2.next:
            dummy2.next.prev = prev1
    
        # ------------------------------------------------
        # Update the head of the list to the start of
        # the < x partition (after dummy1)
        # ------------------------------------------------
        self.head = dummy1.next
    
        # ------------------------------------------------
        # Ensure the new head has no previous pointer
        # (important for DLL structure)
        # ------------------------------------------------
        self.head.prev = None



    
# -------------------------------
# Test Cases:
# -------------------------------

print("\nTest Case 1: Partition around 5")
dll1 = DoublyLinkedList(3)
dll1.append(8)
dll1.append(5)
dll1.append(10)
dll1.append(2)
dll1.append(1)
print("BEFORE: ", end="")
dll1.print_list()
dll1.partition_list(5)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest Case 2: All nodes less than x")
dll2 = DoublyLinkedList(1)
dll2.append(2)
dll2.append(3)
print("BEFORE: ", end="")
dll2.print_list()
dll2.partition_list(5)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest Case 3: All nodes greater than x")
dll3 = DoublyLinkedList(6)
dll3.append(7)
dll3.append(8)
print("BEFORE: ", end="")
dll3.print_list()
dll3.partition_list(5)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest Case 4: Empty list")
dll4 = DoublyLinkedList(1)
dll4.make_empty()
print("BEFORE: ", end="")
dll4.print_list()
dll4.partition_list(5)
print("AFTER:  ", end="")
dll4.print_list()

print("\nTest Case 5: Single node")
dll5 = DoublyLinkedList(1)
print("BEFORE: ", end="")
dll5.print_list()
dll5.partition_list(5)
print("AFTER:  ", end="")
dll5.print_list()

