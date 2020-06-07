#
# @lc app=leetcode.cn id=199 lang=python
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        # dfs的思路
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        # 在递归的每一层都取了右子树没有而左子树有的情况，
        # 所以再最外层也这样取就补齐了右侧能看到的所有节点
        # 每一层都是先根输出+右边节点输出，如果某层右边没有的左边输出
        # 左边输出的层数一定是大于右边的各层节点
        return [root.val] + right + left[len(right):]
    
    
# from collections import deque

# class Solution(object):
#     def rightSideView(self, root):
#         rightmost_value_at_depth = dict() # 深度为索引，存放节点的值
#         max_depth = -1

#         queue = deque([(root, 0)])
#         while queue:
#             node, depth = queue.popleft()

#             if node is not None:
#                 # 维护二叉树的最大深度
#                 max_depth = max(max_depth, depth)

#                 # 由于每一层最后一个访问到的节点才是我们要的答案，因此不断更新对应深度的信息即可
#                 rightmost_value_at_depth[depth] = node.val

#                 queue.append((node.left, depth+1))
#                 queue.append((node.right, depth+1))

#         return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]


        
# @lc code=end

