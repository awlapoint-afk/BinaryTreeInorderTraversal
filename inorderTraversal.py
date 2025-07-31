# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(arr):
    """
    Build a binary tree from a level-order list representation.
    None/null values represent missing nodes.
    """
    if not arr or arr[0] is None:
        return None

    # Create root node
    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while queue and i < len(arr):
        node = queue.pop(0)

        # Add left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        # Add right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        if not root:
            return result

        stack = []
        current = root
        stack.append(current)
        while current.left:
            stack.append(current.left)
            current = current.left

        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.right:
                current = current.right
                stack.append(current)
                while current.left:
                    stack.append(current.left)
                    current = current.left

        return result


solution = Solution()

testcase1 = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
testcase1_pass = [4, 2, 6, 5, 7, 1, 3, 9, 8]
testcase1_root = build_tree_from_list(testcase1)
print(solution.inorderTraversal(testcase1_root) == testcase1_pass)
print(solution.inorderTraversal(testcase1_root))
