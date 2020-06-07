# 解题思路
# 前序遍历，也叫先根遍历，先访问根节点然后访问左子树，然后是右子树
# 顺带：
#   中序遍历，首先遍历左子树，然后访问根结点，最后遍历右子树。
#   后序遍历 首先遍历左子树，然后遍历右子树，最后访问根节点。
# 最简单的遍历方式就是迭代法

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        res = []
        self._preorder(root, res)
        return res
    
    def _preorder(self, node, res=[]):
        res.append(node.val)
        if node.children is None:
            return
        for i in range(len(node.children)):
            self._preorder(node.children[i], res)
            
                
            
            
        
        