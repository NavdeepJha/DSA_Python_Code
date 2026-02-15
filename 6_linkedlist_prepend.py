class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):

        pre = self.head
        temp = self.head

        #1. when the list is empty
        if self.length==0:
            return None
        
        #2. When there is a single item
        elif self.length==1 :
            self.head = None
            self.tail = None
            self.length = 0
            return temp.value 
        
        
        #3. when there are atleast two items
        elif self.length>=2 :
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length +=-1
            return temp.value
    
    def prepend(self,value):
        new_node = Node(value)
        

        
        

        

my_linked_list = LinkedList(11)
#my_linked_list.append(3)
#my_linked_list.append(23)
#my_linked_list.append(7)

my_linked_list.print_list()

print("popped value = ", my_linked_list.pop())
print("list after...popping")

my_linked_list.print_list()

