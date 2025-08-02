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

    def is_tree_balanced(self, root: TreeNode):
        def get_depth(node) -> int:
            if node.left:
                l = get_depth(node.left)
            else:
                l = 1
            if node.right:
                r = get_depth(node.right)
            else:
                r = 1

            if not l or not r:
                return -1
            elif abs(l - r) > 1:
                return -1
            else:
                return max(l, r) + 1

        rc = get_depth(root)
        if rc == -1:
            return False
        else:
            return True

    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        result_p = []
        result_q = []

        def list_nodes(root, result):
            if not root:
                return

            result.append(root.val)
            if not root.left:
                result.append("null")
            else:
                list_nodes(root.left, result)
            if not root.right:
                result.append("null")
            else:
                list_nodes(root.right, result)

        list_nodes(p, result_p)
        list_nodes(q, result_q)
        return result_p == result_q


solution = Solution()

# testcase1 = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
# testcase1_pass = [4, 2, 6, 5, 7, 1, 3, 9, 8]
# testcase1_root = build_tree_from_list(testcase1)
# print(solution.inorderTraversal(testcase1_root) == testcase1_pass)
# print(solution.inorderTraversal(testcase1_root))
# print(solution.is_tree_balanced(testcase1_root))

p_list = [5,4,1,None,1,None,4,2,None,2]
q_list = [5,1,4,4,None,1,None,None,2,None,2]
p = build_tree_from_list(p_list)
q = build_tree_from_list(q_list)
print(solution.isSameTree(p, q))