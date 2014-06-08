# Q implement a BST
from Queue import Queue
class Node:

    """This is Different Node for the Binary Search Tree"""

    def __init__(self, data=0):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)


def insert(root, node, parent=None):
    if not root:
        root = node
        root.parent = parent
        return

    if node.data > root.data:
        if root.right:
            insert(root.right, node, root)
        else:
            root.right = node
            root.parent = parent
    else:
        if root.left:
            insert(root.left, node, root)
        else:
            root.left = node
            root.parent = parent


def levelOrder(root):
    """
    This does the cool level order traversal of a tree 
    more usefull than the other one(inorder) for debugging
    it is kinda bfs
    """
    if not root:
        return
    currentLevel = Queue()
    nextLevel = Queue()
    currentLevel.put(root)


    while not currentLevel.empty():
        string = ""
        while not currentLevel.empty():
            curretNode = currentLevel.get()
            string += str(curretNode)
            if curretNode.left:
                nextLevel.put(curretNode.left)
            if curretNode.right:
                nextLevel.put(curretNode.right)

        print string
        # swap the two levels
        currentLevel, nextLevel = nextLevel, currentLevel


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root
    inorder(root.right)


def successor(node):
    """Given a node return the next largest"""

    if node.right:
        tmp = node.right
        while tmp.left.left:
            tmp = tmp.left
        return tmp.left

    # if the node does not has a right sub tree
    # then the find the parent of which this one is a left subtree (think in terms of inorder traversal)
    parent = node.parent
    while not parent.left == node:
        node = node.parent
        parent = node.parent

    return parent


def predecessor(node):
    """Given a node return the just smaller element"""
    pass


def main():
    root = Node(2)
    n = Node(3)
    insert(None, root)
    insert(root, n)
    insert(root, Node(5))
    insert(root, Node(1))
    insert(root, Node(0))
    insert(root, Node(4))

    levelOrder(root)
    print 'asdfasdf'

    print n
    print successor(n)

if __name__ == '__main__':
    main()
