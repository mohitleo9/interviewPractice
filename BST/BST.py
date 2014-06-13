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


def search(root, data):
    if not root:
        return -1

    if root.data == data:
        return root

    if data > root.data:
        return search(root.right, data)
    else:
        return search(root.left, data)


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
    # then the find the parent of which this one is a left subtree (think in
    # terms of inorder traversal)
    parent = node.parent
    while not parent.left == node:
        node = node.parent
        parent = node.parent

    return parent


def predecessor(node):
    """Given a node return the just smaller element"""

    # if the node has a left tree then
    # the pre must be the last right one
    if node.left:
        tmp = node.left
        while tmp.right.right:
            tmp = tmp.right
        return tmp.right

    parent = node.parent
    while not parent.right == node:
        node = node.parent
        parent = node.parent
    return parent


def isBalanced(root):
    """ A tree is balanced if height of two subtrees is never greater than 1"""
    if not root:
        return True

    heightLeft = height(root.left)
    heightRight = height(root.right)

    diff = heightLeft - heightRight

    if diff in range(-1, 2):
        return isBalanced(root.left) and isBalanced(root.right)
    else:
        return False


def checkHeight(root):
    """
    this function does the same thing as isBalanced but a little different
    this one does that with a little panache it returns the height of the tree if
    the tree is balanced otherwise returns -1
    """

    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    leftHeight = 1 + height(root.left)
    rightHeight = 1 + height(root.right)

    if leftHeight == 0 or rightHeight == 0:
        return -1

    diff = abs(leftHeight - rightHeight)

    if diff > 1:
        return -1
    return max(leftHeight, rightHeight)


def height(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    leftHeight = 1 + height(root.left)
    rightHeight = 1 + height(root.right)

    return max(leftHeight, rightHeight)


def commonAncestor(root, node1, node2, found1=False, found2=False):
    if not root:
        return None

    if root == node1:
        found1 = True
    if root == node2:
        found2 = True

    ans = commonAncestor(root.left, node1, node2, found1, found2)
    answ = commonAncestor(root.right, node1, node2, found1, found2)

    if found1 and found2:
        return root
    if ans:
        return ans
    else:
        return answ


def main():
    root = Node(2)
    n = Node(3)
    insert(root, n)
    insert(root, Node(0))
    insert(root, Node(6))
    insert(root, Node(5))
    insert(root, Node(1))
    insert(root, Node(7))
    insert(root, Node(4))
    insert(root, Node(4))
    insert(root, Node(4))
    insert(root, Node(4))

    levelOrder(root)
    print 'asdfasdf'

    print 'height = ' + str(height(root))
    print isBalanced(n)
    print checkHeight(n)
    # print commonAncestor(root, n, search(root, 7))


if __name__ == '__main__':
    main()
