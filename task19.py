class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def delete(self, data):
        if self.head is None:
            print("Error: Linked list is empty. Cannot delete.")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = self.head
        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next
        print("Error: Node with data", data, "not found.")
    def display(self):
        """Display the elements of the linked list."""
        if self.head is None:
            print("Linked list is empty.")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()
linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(40)
print("Linked list after insertions:")
linked_list.display()
linked_list.delete(30)
print("Linked list after deletion of 3:")
linked_list.display()
linked_list.delete(2)
linked_list.delete(10)
print("Linked list after deletion of 1:")
linked_list.display()
