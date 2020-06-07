# 解题思路
# 1. 重复的逻辑就是每个左子树 or 右子树都进行递归验证二叉搜索树的特征
#   要求满足二叉搜索树的特征，根大于左子树，小于右子树，左子树和右子树都是二叉搜索树
# 复杂度分析
# 时间复杂度 : O(N)。每个结点访问一次。
# 空间复杂度 : O(N)。我们跟进了整棵树。

#   根要大于所有左子树，同时要小于所有右子树，存在着左右边界问题
# 2. 迭代法求解，使用stack来解题，算法和1基本一致，仅仅把递归改为迭代逻辑
# 时间复杂度 : O(N)。每个结点访问一次。
# 空间复杂度 : O(N)。我们跟进了整棵树。



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True


# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         return self.valid(root)
        
        
#     def valid(self, node, lower = float('-inf'), upper = float('inf')):
#         # recursion terminator
#         if not node:
#             return True
        

#         # process logic in current level
#         if node.val <= lower or node.val >= upper:
#             return False
                
#         # drill down    
#         if not self.valid(node.right, node.val, upper):
#             return False
        
#         if not self.valid(node.left, lower, node.val):
#             return False
        
#         return True
#         # reverse the current level status if needed