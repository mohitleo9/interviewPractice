from BST import Node, insert, levelOrder

def baltree(root, list):
    if not list:
        return

    mid = len(list) / 2
    root.data = list[mid]

    root.left = Node()
    root.right = Node()

    baltree(root.left, list[0: mid])
    baltree(root.right, list[mid + 1:])

def main():
    arr = [i for i in range(0, 8)]
    root = Node()
    baltree(root, arr)
    levelOrder(root)


main()




