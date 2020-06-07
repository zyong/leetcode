# 590. N叉树的后序遍历
# 给定一个 N 叉树，返回其节点值的后序遍历。
# 解题思路
# 1.递归法，不论多少还是，都是左子树和右子树，然后根节点的顺序，
# 只把最右遍的子树当成右子树就可以了

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        self._postorder(root, res)
        
        return res
    
    def _postorder(self, node, res=[]):
        if node.children is not None:
            for i in range(len(node.children)):
                self._postorder(node.children[i], res)
        res.append(node.val)

    