# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=146 lang=python
#
# [146] LRU缓存机制
#
# 解题思路
# 1.需要hash数据结构解决O(1)随机访问
# 2.需要双端队列结构解决顺序访问和优先级排列
# 
# @lc code=start
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._cap = capacity
        self._size = 0

        self._table = {}

        self._head = Node(0, -1)
        self._tail = Node(0, -1)
        self._head.next = self._tail
        self._tail.prev = self._head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self._table:
            return -1
        
        node = self._table[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self._tail
        node.prev = self._tail.prev
        self._tail.prev.next = node
        self._tail.prev = node

        return node.val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.get(key) != -1:
            self._table[key].val = value
            return

        if self._size == self._cap:
            victim = self._head.next
            del self._table[victim.key]
            self._head.next = victim.next
            victim.next.prev = self._head
            self._size -= 1

        node = Node(key, value, self._tail.prev, self._tail)
        node.prev.next = node
        self._tail.prev = node

        self._table[key] = node

        self._size += 1        
        

class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# from collections import defaultdict
# class LRUCache(object):
#     capacity = None
#     loadfactor = 0.75
#     hashmap = None
#     queue = None
#     head = None
#     tail = None
    
#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#         self.hashmap = defaultdict()
#         self.size = 0
#         self.head = DNode(None, None)
#         self.tail = DNode(None, None)

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key in self.hashmap:
#             node = self.hashmap[key]
#             self.popToTail(node)
#             return node.value

#         return -1

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         if key in self.hashmap:
#             node = self.hashmap[key]
#             node.value = value
#             self.hashmap[key] = node
#             self.popToTail(node)
#         else:
#             node = DNode(key, value)
#             if self.capacity <= self.size:
#                 self.removeFirst()
#             self.hashmap[key] = node
#             self.addToTail(node)
#             self.size += 1
#             return
        
#     def removeFirst(self):
#         node = self.head.next
#         next = node.next
#         self.head.next = next
#         next.prev = self.head
#         del self.hashmap[node.key]
#         return node
    
#     def popToTail(self, node):
#         next = node.next
#         prev = node.prev
#         prev.next = next
#         next.prev = prev
#         last = self.tail.prev
#         last.next = node
#         node.prev = last
#         node.next = self.tail
#         self.tail.prev = node
        
#     def addToTail(self, node):
#         if self.tail.prev == None:
#             self.tail.prev = DNode(None, None)
#         last = self.tail.prev
#         last.next = node
#         self.tail.prev = node
#         node.prev = last
#         node.next = self.tail
#         if self.head.next == None:
#             self.head.next= DNode(None, None)
#             self.head.next = node
#             node.prev = self.head
            
    
# class DNode(object):
#     def __init__(self, value, key):
#         self.prev = None    # 前驱
#         self.next = None    # 后继
#         self.value = value  # 值
#         self.key = key



# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)
# # @lc code=end

    