from assignment1 import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        # Case 1: deleting head node
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Case 2: search for node
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # key not found
        if temp is None:
            return
        
        prev.next = temp.next
        temp = None

    def display_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")