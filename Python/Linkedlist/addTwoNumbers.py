# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        1.输入为两个链表，输出为一个链表
        2.链表为逆序存储，每个节点只存储一位数字，数字不以0开头
        3.链表中存储非负整数
        输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
        输出：7 -> 0 -> 8
        原因：342 + 465 = 807
        """
    
        str1 = ""
        while l1 is not None:            
            str1 += l1.val
            l1 = l1.next
            
        while l2 is not None:    
            str2 += l2.val
            l2 = l2.next
            
        str1 = (int)str1[::-1]
        str2 = (int)str2[::-1]
        
        s = str1 + str2
        
        s = s[::-1]
        root = ListNode()
        node = root
        for i in s:
            node.val = i
            node.next = ListNode()
            node = node.next
            
        return root 