class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)

        if self.head is None :
            self.head = new_node
            self.tail = new_node
            self.length +=1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

            self.tail = new_node
            self.length +=1
        
        return True

  



my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(8)
my_doubly_linked_list.append(9)
my_doubly_linked_list.append(3)


print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length)



