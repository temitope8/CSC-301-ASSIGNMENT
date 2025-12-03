from assignment2 import LinkedList

ll = LinkedList()

# Insert 5 values
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_end(50)

print("Initial List:")
ll.display_list()

# Delete one node
ll.delete_node(30)
print("\nAfter deleting 30:")
ll.display_list()