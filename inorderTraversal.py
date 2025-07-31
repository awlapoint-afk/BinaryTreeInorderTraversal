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
        stack.append((root, True, True))

        while stack:
            current, left, right = stack.pop()
            if left == True and right == True:
                stack.append((current, False, True))
                if current.left:
                    current = current.left
                    stack.append((current, True, True))
                else: # current.left is None
                    continue
            elif left == False and right == True:
                # process current val
                result.append(current.val)
                stack.append((current, False, False))
                if current.right:
                    current = current.right
                    stack.append((current, True, True))
            elif left == False and right == False:
                continue

        return result


solution = Solution()

testcase1 = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
testcase1_pass = [4, 2, 6, 5, 7, 1, 3, 9, 8]
testcase1_root = build_tree_from_list(testcase1)
print(solution.inorderTraversal(testcase1_root) == testcase1_pass)
print(solution.inorderTraversal(testcase1_root))
