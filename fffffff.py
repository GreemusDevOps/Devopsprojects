class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def _hash(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))
    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (existing_key, existing_value) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    break
    def search(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for existing_key, existing_value in self.table[index]:
                if existing_key == key:
                    return existing_value
        return None
hash_table = HashTable(10)
hash_table.insert("apple", 20)
hash_table.insert("banana", 30)
hash_table.insert("cherry", 40)
print("Search 'banana':", hash_table.search("banana"))
print("Search 'grape':", hash_table.search("grape"))
hash_table.delete("banana")
print("Search 'banana' after deletion:", hash_table.search("banana"))


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class BinaryTree:
    def __init__(self):
        self.root = None
    def in_order_traversal(self, node):
        result = []
        if node:
            result = self.in_order_traversal(node.left)
            result.append(node.val)
            result = result + self.in_order_traversal(node.right)
        return result
    def pre_order_traversal(self, node):
        result = []
        if node:
            result.append(node.val)
            result = result + self.pre_order_traversal(node.left)
            result = result + self.pre_order_traversal(node.right)
        return result
    def post_order_traversal(self, node):
        result = []
        if node:
            result = self.post_order_traversal(node.left)
            result = result + self.post_order_traversal(node.right)
            result.append(node.val)
        return result
if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print("In-order traversal:", tree.in_order_traversal(tree.root))
    print("Pre-order traversal:", tree.pre_order_traversal(tree.root))
    print("Post-order traversal:", tree.post_order_traversal(tree.root))

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


