# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
# 题目理解
# 1. 对二叉树翻转的认知首先是左子树和右子树交换位置
# 2。对每个子树下的左右元素交换位置
# 解题思路
# 1。首先翻转根的左和右子树
# 2. 递归左子树和右子树，实现两者的孩子进行交换
# 3. 递归结束条件，如果孩子为空就结束了
# 4. 如何没有根没有孩子也结束了

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        left = root.left
        right = root.right
        if left:    
            self.invertTree(left)
        if right:
            self.invertTree(right)

        root.left = right
        root.right = left    

        return root

# @lc code=end