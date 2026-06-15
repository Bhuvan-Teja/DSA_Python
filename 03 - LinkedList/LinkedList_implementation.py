class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node =Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_linkedlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print("***********************************")

    def append(self, value):
        append_node = Node(value)
        if self.length == 0:
            self.head = append_node
            self.tail = append_node
        else:
            self.tail.next = append_node
            self.tail = append_node
        self.length+= 1
        return True


    def prepend(self, value):
        prepend_node = Node(value)
        if self.length == 0:
            self.head = prepend_node
            self.tail = prepend_node
        else:
            prepend_node.next = self.head
            self.head = prepend_node
        self.length+=1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        pop_f = self.head
        self.head = self.head.next
        pop_f.next = None
        self.length-=1
        if self.length == 0:
            self.tail = None
        return pop_f.value

    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value
    
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return temp.value
    
    def insert(self, index, value):
        pass
        


my_linked_list = LinkedList(4)

my_linked_list.append(5)

my_linked_list.prepend(3)

my_linked_list.print_linkedlist()

print(my_linked_list.get_node(1))

my_linked_list.set_value(1, 1)

my_linked_list.print_linkedlist()

# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())

# my_linked_list.print_linkedlist()




# print(my_linked_list.head.value)