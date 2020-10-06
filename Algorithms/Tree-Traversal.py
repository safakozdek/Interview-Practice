class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def iterativeInorderTraverse(root):
    if root is None:
        return ""

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
        return ""

    recursiveInorderTraversal(root.left)
    print(root.val, end=" ")
    recursiveInorderTraversal(root.right)
    return ""


def iterativePreorderTraverse(root):
    if root is None:
        return ""

    stack = [root]

    while stack:
        current = stack.pop()
        print(current.val, end=" ")
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return ""


def recursivePreorderTraversal(root):
    if root is None:
        return ""

    print(root.val, end=" ")
    recursivePreorderTraversal(root.left)
    recursivePreorderTraversal(root.right)
    return ""


def iterativePostorderTraverse(root):
    if root is None:
        return ""

    result_stack = []
    iteration_stack = [root]

    while iteration_stack:
        current = iteration_stack.pop()
        result_stack.append(current)
        if current.left:
            iteration_stack.append(current.left)
        if current.right:
            iteration_stack.append(current.right)

    while result_stack:
        current = result_stack.pop()
        print(current.val, end=" ")

    return ""


def recursivePostorderTraversal(root):
    if root is None:
        return ""

    recursivePostorderTraversal(root.left)
    recursivePostorderTraversal(root.right)
    print(root.val, end=" ")

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
    print(iterativePreorderTraverse(root))
    print(recursivePreorderTraversal(root))
    print(iterativePostorderTraverse(root))
    print(recursivePostorderTraversal(root))
