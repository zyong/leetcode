#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start


# class Trie(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = {} 
#         self.end_of_word = "#"

#     def insert(self, word):
#         """
#         Inserts a word into the trie.
#         :type word: str
#         :rtype: None
#         """
#         node = self.root
#         for char in word:
#             # 巧妙的实现，setdefault每次设置值如果值存在就返回值
#             # 不存在就返回默认值
#             node = node.setdefault(char, {}) 
#             # 词尾用终止符标识
#         node[self.end_of_word] = self.end_of_word

#     def search(self, word):
#         """
#         Returns if the word is in the trie.
#         :type word: str
#         :rtype: bool
#         """
#         node = self.root
#         for char in word:
#             if char not in node:
#                 return False
#             node = node[char]
        
#         return self.end_of_word in node

#     def startsWith(self, prefix):
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         :type prefix: str
#         :rtype: bool
#         """
#         node = self.root
#         for char in prefix:
#             if char not in node:
#                 return False
#             node = node[char]
#         return True
        

from collections import defaultdict

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.p = defaultdict()
        self.end_of_word = '#'

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.p
        for c in word:
            node = node.setdefault(c, defaultdict())
        
        node[self.end_of_word] = self.end_of_word


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.p
        for c in word:
            if c not in node:
                 return False
            node = node[c]
        return self.end_of_word in node
  

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.p
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

