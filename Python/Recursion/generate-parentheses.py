# -*- coding:utf-8 -*-

# 解题思路
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        s = ""
        self._generateParenthesis(n, 0, 0, s, res)
        return res
        
    def _generateParenthesis(self, n, left, right, s, res=[]):
        # recursion terminator
        if left == n and right == n:
            # print的left 和right都等于n的情况会出现很多次，递归到叶节点的right时候就会产生这个情况
            print(s)
            return res.append(s)

        
        # process logic in current level
        if left < n:
            self._generateParenthesis(n, left + 1, right, s + "(", res) 
            
        # drill down 
        # 左边大于右边是为了保证先输出左边的括号，再是右边，如果右边输出多了，肯定是有问题的
        if right < n and left > right: 
            self._generateParenthesis(n, left, right + 1, s + ")", res)
        # reverse the current level status if needed


if __name__ == "__main__":
    obj = Solution()
    print(obj.generateParenthesis(3))