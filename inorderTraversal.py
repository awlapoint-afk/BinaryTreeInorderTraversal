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

    def inorderTraversalLlama(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        if not root:
            return result

        stack = []
        current = root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                result.append(current.val)
                current = current.right

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
        def comp_nodes(root_a, root_b):
            if not root_a and not root_b:
                return True
            if (root_a is None) != (root_b is None):
                return False

            if root_a.val != root_b.val:
                return False

            return comp_nodes(root_a.left, root_b.left) and comp_nodes(root_a.right, root_b.right)

        return comp_nodes(p, q)

    def isSymmetricRec(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def comp_nodes(root_a, root_b):
            if not root_a and not root_b:
                return True
            if (root_a is None) != (root_b is None):
                return False

            if root_a.val != root_b.val:
                return False

            return comp_nodes(root_a.left, root_b.right) and comp_nodes(root_a.right, root_b.left)

        return comp_nodes(root.left, root.right)


    def isSymmetricOld(self, root):
        result_a = []
        result_b = []

        if not root:
            return []

        root_a = root.left
        root_b = root.right

        if not root_a and not root_b:
            return True
        if (root_a is None) != (root_b is None):
            return False

        stack_a = []
        current = root_a
        stack_a.append(current)
        while current.left:
            stack_a.append(current.left)
            current = current.left

        while stack_a:
            current = stack_a.pop()
            result_a.append(current.val)
            if current.right:
                current = current.right
                stack_a.append(current)
                while current.left:
                    stack_a.append(current.left)
                    current = current.left
                    if not current.left:
                        result_a.append('null')
            else:
                result_a.append('null')

        stack_b = []
        current = root_b
        stack_b.append(current)
        while current.right:
            stack_b.append(current.right)
            current = current.right

        while stack_b:
            current = stack_b.pop()
            result_b.append(current.val)
            if current.left:
                current = current.left
                stack_b.append(current)
                while current.right:
                    stack_b.append(current.right)
                    current = current.right
                    if not current.right:
                        result_b.append('null')
            else:
                result_b.append('null')

        print(f"result_a: {result_a} result_b: {result_b}")
        return result_a == result_b

    def isSymmetric(self, root):
        if not root:
            return True
        if (root.left is None) != (root.right is None):
            return False

        stack = []

        if root.left and root.right:
            stack.append((root.left, root.right))

        while stack:
            current_a, current_b = stack.pop()
            if current_a.val != current_b.val:
                return False

            if (current_a.left is None) != (current_b.right is None):
                return False
            if (current_a.right is None) != (current_b.left is None):
                return False
            if current_a.left and current_b.right:
                stack.append((current_a.left, current_b.right))
            if current_a.right and current_b.left:
                stack.append((current_a.right, current_b.left))

        return True
    
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_depth = 0
        if not root:
            return max_depth

        stack = [(root, 1)]
        while stack:
            current, depth = stack.pop()

            if current.left:
                stack.append((current.left, depth + 1))
            if current.right:
                stack.append((current.right, depth + 1))

            max_depth = max(max_depth, depth)

        return max_depth
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def create_tree(left, right):
            if (right - left + 1) == 1:
                return TreeNode(nums[left])
            elif (right - left + 1) == 0:
                return None

            mid = left + (right - left) // 2

            current = TreeNode(nums[mid])
            current.left = create_tree(left, mid - 1)
            current.right = create_tree(mid + 1, right)

            return current

        l = 0
        r = len(nums) - 1

        return create_tree(l, r)

    def sortedArrayToBST_iter(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None

        stack = []
        root = TreeNode()
        stack.append((root, 0, len(nums) - 1))
        # stack = (node, left, right)
        while stack:
            current, left, right = stack.pop()

            mid = left + (right - left) // 2
            current.val = nums[mid]

            if left < mid:
                current.left = TreeNode()
                stack.append((current.left, left, mid - 1))

            if right > mid:
                current.right = TreeNode()
                stack.append((current.right, mid + 1, right))

        return root

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        l_node = self.lowestCommonAncestor(root.left, p, q)
        r_node = self.lowestCommonAncestor(root.right, p, q)

        if l_node and r_node:
            return root
        elif l_node:
            return l_node
        else:
            return r_node


solution = Solution()

# InorderTraversal tests
# testcase1 = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
# testcase1_pass = [4, 2, 6, 5, 7, 1, 3, 9, 8]
# testcase1_root = build_tree_from_list(testcase1)
# print(solution.inorderTraversal(testcase1_root) == testcase1_pass)
# print(solution.inorderTraversal(testcase1_root))
# print(solution.is_tree_balanced(testcase1_root))

# isSameTree tests
# p_list = [5,4,1,None,1,None,4,2,None,2]
# q_list = [5,1,4,4,None,1,None,None,2,None,2]
# p = build_tree_from_list(p_list)
# q = build_tree_from_list(q_list)
# a_list = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
# b_list = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
# a = build_tree_from_list(a_list)
# b = build_tree_from_list(b_list)
# print(solution.isSameTree(p, q))
# print(solution.isSameTree(a, b))

# isSymmetric tests
# test1_list = [1,2,2,3,4,4,3]
# test1 = build_tree_from_list(test1_list)
# print(solution.isSymmetric(test1))

# test2_list = [1,2,2,None,3,None,3]
# test2 = build_tree_from_list(test2_list)
# print(solution.isSymmetric(test2))

# test3_list = [1,0]
# test3 = build_tree_from_list(test3_list)
# print(solution.isSymmetric(test3))

# test4_list = [5,2,2,4,None,None,1,None,1,None,4,2,None,2,None]
# test4 = build_tree_from_list(test4_list)
# print(solution.isSymmetric(test4))

# test5_list = [1, 2, 2, None, 3, 3, None]
# test5_list = [1, 2, 2, 3, None, None, 3]
# test5_list = [1, 2, 2, 3, None, 3, None]
# test5 = build_tree_from_list(test5_list)
# print(solution.isSymmetric(test5))

# print(solution.maxDepth(test5))

# test6_list = [1,2,3,4,5,6,7,8,9]
# test6_root = solution.sortedArrayToBST_iter(test6_list)
# print(solution.is_tree_balanced(test6_root))
# print(solution.inorderTraversalLlama(test6_root))

test7_list = [3,5,1,6,2,0,8,None,None,7,4]
test7_root = build_tree_from_list(test7_list)
test7nodea = solution.lowestCommonAncestor(test7_root, TreeNode(5), TreeNode(1))
test7nodeb = solution.lowestCommonAncestor(test7_root, TreeNode(5), TreeNode(4))
test8_list = [1,2]
test8_root = build_tree_from_list(test8_list)
test8nodea = solution.lowestCommonAncestor(test8_root, TreeNode(1), TreeNode(2))

for test in [test7nodea, test7nodeb, test8nodea]:
    if test:
        print(f"{test.val}")