# 解题思路
# 1.链表循环+list排序二分查找
#   1.循环链表，将每个节点添加到list
#   2.将list排序,使用排序函数
#   3.二分查找中间值

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        # res = []
        # node = head
        # while node:
        #     res.append(node)
        #     node = node.next

        # mid = len(res)//2
        
        # return res[mid]
        # fast跑的速度是low的两倍，这样fast到终点了，low在中间
        low = fast = head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
        return low