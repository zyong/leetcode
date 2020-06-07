# 解题思路
# 1、将一个字符串的每个字母都存到数组中，然后loop另一个字符串看是否覆盖每个字母
# 2、将字符串放到数组中并排序，loop数组看是否一样
# 3、使用hash-map 统计计数，也可以使用ascii码计数

# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         s = sorted(s)
#         t = sorted(t)
#         length = len(s)

#         if length != len(t):
#             return False
        
#         for i in range(length):           
#             if s[i] != t[i]:
#                 return False
            
#         return True


# # use hash map to static number of alphabet
# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         d1 = dict()
#         d2 = dict()
#         for i in s:
#             d1[i] = d1.get(i, 0) + 1
#         for j in t:
#             d2[j] = d2.get(j, 0) + 1
#         return d1 == d2
        

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

