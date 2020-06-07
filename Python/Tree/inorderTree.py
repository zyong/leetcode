# 解题思路：
# 1、二叉树的中序遍历顺序就是先递归左子树，找到左子树的最小的节点，如果这个节点是null就返回，然后访问中间节点，然后访问右节点，如果为null(表示没有右子节点)就返回，再访问父节点。然后访问root节点。再遍历右子树，遍历依然从右子树的左节点优先访问，然后是中间节点然后是右节点。就是先左子树 or 左节点，然后中间节点，然后右边节点。
# 解题的关键问题是python递归方法要带上list变量，要不处理很麻烦



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        self.traversal_inorder(root, res)

        return res
            
    # 二叉树中序遍历
    def traversal_inorder(self, node, res):
        if node.left is not None:
            self.traversal_inorder(node.left, res)
        res.append(node.val)
        if node.right is not None:
            self.traversal_inorder(node.right, res)