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
    tree.root.left = Node(10)
    tree.root.right = Node(30)
    tree.root.left.left = Node(40)
    tree.root.left.right = Node(50)
    tree.root.right.left = Node(60)
    tree.root.right.right = Node(70)
    print("In-order traversal:", tree.in_order_traversal(tree.root))
    print("Pre-order traversal:", tree.pre_order_traversal(tree.root))
    print("Post-order traversal:", tree.post_order_traversal(tree.root))