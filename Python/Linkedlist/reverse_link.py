class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        def reverse(node, cur):
            # print(node.val)
            tempNode = ListNode(node.val)
            tempNode.next = cur

            if node.next:
               return reverse(node.next, tempNode)

            return tempNode
        

        return reverse(head, None)

# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head:
#             return None
        
#         tempNode = ListNode(None)
#         cur = None
#         while head:
#             tempNode = ListNode(head.val)
#             tempNode.next = cur
#             cur = tempNode
#             head = head.next
#         return cur
        
        
#         node = ListNode(None)
        
        
#         if head is None:
#             return node
        
#         res = []
#         while head:
#             res.append(head)
#             head = head.next
        
#         res.reverse()
#         root = node
#         for i in range(len(res)):
#             # print(res[i].val)
#             node.next = res[i]
#             node = node.next

    
    
    
if __name__ == "__main__":
    node = ListNode(-1)
    root = node
    for i in range(1, 6):
        node.next = ListNode(i)
        node = node.next
    
    root = root.next
    obj = Solution()
    ret = obj.reverseList(root)
    while ret:
        print(ret.val)
        ret = ret.next
    print(ret)