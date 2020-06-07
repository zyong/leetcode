#-*- coding:utf-8 -*-
# @lc app=leetcode.cn id=820 lang=python
#
# [820] 单词的压缩编码
# 
# 解题思路
# 问题的几种情况
# 1.有重复单词
# 2.有单词是其他词后缀
# 3.没有重复和后缀的情况

# 1.set + 后缀检查
#   1.将所有元素放入set
#   2.loop 集合里面每个元素，判断他的子集是否在set中
#   3.将重复的子集去掉
#   4.剩下的set元素的从长度+元素个数-1
# 2.前缀Trie
#   1.构建一个空前缀trie树
#   2.每次逆序插入单词，如果是新单词就返回true，不是就返回false
#   3.记录新单词的长度+1的和为结果值

# @lc code=start
# 前缀Trie
# import collections

# class Solution(object):
#     def minimumLengthEncoding(self, words):
#         """
#         :type words: List[str]
#         :rtype: int
#         """
        
#         trie = collections.defaultdict()
        
#         def insert(word):
#             node = trie
#             w = word[::-1]
#             is_new = False
#             for c in w:
#                 if c not in node:
#                     is_new = True
#                 node = node.setdefault(c, collections.defaultdict())
#             return is_new
#         words.sort(key=lambda x: len(x), reverse=True)
#         return sum(len(w) + 1 for w in words if insert(w))
        
import collections
from functools import reduce

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        # 首先用trie初始化初值，类似于 function(accum_value, x)中的accum_value,
        # x为words逆序的字母，从trie里面找这个元素是否存在，而trie会一直返回新的trie
        # 所以不会报错。当全新元素添加到trie里面的时候，比如time->emit 
        # 构成e->m->i->t的dict结构，第二次找的时候，比如e->m找到了，但是后面的i和t没有
        # 所以这个时候找到的结果里面是i-t的返回值；如果找一个单词逆序里面没有返回值，
        # 证明是一个新的单词，就需要计算到最后的压缩字符串中
        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]
        print(trie)
        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)

# set 
# class Solution(object):
#     def minimumLengthEncoding(self, words):
#         """
#         :type words: List[str]
#         :rtype: int
#         """
#         if not words:
#             return 0

#         new = set(words)
#         for word in words:
#             for i in range(1,len(word)):
#                 new.discard(word[i:])
#         return sum(len(w) + 1 for w in new)
 

        
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    alert = lambda x,y: "ret={} ret is {}".format(x==y, y)
    ret = obj.minimumLengthEncoding(["time", "time", "time", "time"])
    print(alert(5, ret))
    ret = obj.minimumLengthEncoding([])
    print(alert(0, ret))
    ret = obj.minimumLengthEncoding(["me", "time", "bell"])
    print(alert(10, ret))
    ret = obj.minimumLengthEncoding(["time","me"])
    print(alert(5, ret))
    ret = obj.minimumLengthEncoding(["time", "atime", "btime"])
    print(alert(12, ret))
    