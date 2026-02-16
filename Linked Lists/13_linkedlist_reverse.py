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

        if self.length==0:
            self.head = new_node
            self.tail = new_node
            self.length +=1
        else:
            new_node.next=self.head
            self.head = new_node
            self.length +=1
        return True
    
    def popfirst(self):
        if self.length==0 :
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.length -=1

            if self.length==0 :
                self.tail = None
            return temp.value
        
    def get(self, index) :

        if index < 0 or index>=self.length :
            return None
        
        else:
            temp = self.head

            ptr = 0

            while ptr!=index:
                temp = temp.next 
                ptr +=1
            return temp
        
    def set_value(self,index,value):
        temp = self.get(index)
        temp.value = value
        
        return True
    
    def insert(self,index,value):
        new_node = Node(value)

        if index==0 :
            self.prepend(value)

        elif index==self.length-1 :
            self.append(value)

        else:
            temp = self.head
            pre = self.head

            ptr = 0

            while ptr!=index :
                pre = temp
                temp = temp.next
                ptr +=1

            new_node.next = pre.next
            pre.next = new_node
            self.length +=1
        return True
    
    def remove(self, index) :
        if index < 0 or index>=self.length :
            return None
        
        if index==0 :
            return self.popfirst()
        
        if index==self.length-1 :
            return self.pop()
        
        else:
            temp = self.get(index)
            pre = self.get(index-1)

            pre.next = temp.next
            temp.next = None
            self.length -=1

        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for i in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

    
 
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.print_list()

print("---after reverse---")
my_linked_list.reverse()
my_linked_list.print_list()



