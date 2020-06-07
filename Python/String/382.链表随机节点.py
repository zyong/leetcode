#
# @lc app=leetcode.cn id=382 lang=python
#
# [382] 链表随机节点
#
# 蓄水池抽样算法
# https://leetcode-cn.com/problems/linked-list-random-node/solution/xu-shui-chi-chou-yang-suan-fa-by-jackwener/

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random

class Solution(object):

    head = None
    
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        i = 0
        res = 0
        cur = self.head
        while cur:
            i += 1
            m = random.randint(1, i)
            if m == i:
                res = cur.val
            cur = cur.next
        
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

