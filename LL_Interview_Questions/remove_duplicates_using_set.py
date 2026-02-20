class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))

    def remove_duplicates(self):

    #Initialize an empty set to store unique values
        values = set()

        prev = None

        current = self.head

        #Iterate through the list

        while current is not None:

            #If the current node's value is already in the set, remove the duplicate node

            if current.value in values:
                
                prev.next = current.next

                self.length -=1

            #Else, add the current node's value to the set and update previous

            else:
                values.add(current.value)
                prev = current

            #Move to the next node
            current = current.next





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(1)

print(my_linked_list.print_list())

my_linked_list.remove_duplicates()

print(my_linked_list.print_list())

