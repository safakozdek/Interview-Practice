class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def iterativeInorderTraverse(root):
    if root is None:
        return

    stack = []
    current = root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print(current.val, end=" ")
            current = current.right

    return ""


def recursiveInorderTraversal(root):
    if root is None:
        return

    recursiveInorderTraversal(root.left)
    print(root.val, end=" ")
    recursiveInorderTraversal(root.right)
    return ""


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(iterativeInorderTraverse(root))
    print(recursiveInorderTraversal(root))
