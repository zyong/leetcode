# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。
# 转换需遵循如下规则：
# 1.每次转换只能改变一个字母。
# 2.转换过程中的中间单词必须是字典中的单词。

# 说明:
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 示例 1:

# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# 输出: 5

#
# 1.深度优先遍历 DFS 时间很长，剪枝优化也不一定过
#   1.从beginword开始顺序遍历字典，如果出现一个单词能从begin一步变化到wordlist里面的单词
# 就将这个单词设置为begin单词继续循环
#   2.单词和单词比较只能变化一个字母，就是单词1和单词2只有1个字母的差别，
# 所以比较单词的差别个数就可以
#   3.将所有可能的转化次数都记录下来，比较最小值
# 复杂度分析
# 时间复杂度：O(M*N），其中 M 是单词的长度 N 是单词表中单词的总数。找到所有的变换需要对每个单词做 M次操作。
# 同时，最坏情况下广度优先搜索也要访问所有的 N 个单词。
# 空间复杂度：O(M*N)，要在 all_combo_dict 字典中记录每个单词的 M 个通用状态。访问数组的大小是 N。
# 广搜队列最坏情况下需要存储 N 个单词。
# 
# 2.BFS
#   1.从begin单词开始变化，如果找到一个就向下转
#   2.如果不行就回来，每次干掉已经找到的word
# 
# 3.双向BFS
#   1.队列，word长度，剪枝visited
#   2.就是从两边向中间走，如果相遇就是答案

# @lc code=start

# two-ended bfs
# from collections import deque
# from collections import defaultdict

# class Solution(object):
#     def visitWord(self, queue, visited, other_visited):
#         word, step = queue.pop(0)            
#         for i in range(self.length):
#             inter_word = word[:i] + "*" + word[i+1:]
#             for w in self.all_combo_dict[inter_word]:
#                 if w in other_visited:
#                     return step + other_visited[w]
#                 if w in self.wordList and w not in visited:
#                     visited[w] = step + 1
#                     queue.append((w, step+1))
#         return None
        
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         if endWord not in wordList or not beginWord or not wordList:
#             return 0
                
#         q = [(beginWord, 1)]
#         p = [(endWord, 1)]
#         self.length = len(beginWord)
#         self.wordList = wordList
        
#         self.all_combo_dict = defaultdict(list) 
#         for word in wordList:
#             for i in range(self.length):
#                 self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        
#         visited_begin = {beginWord:1}
#         visited_end = {endWord:1}
#         ans = None
        
#         while q and p:                                    
#             ans = self.visitWord(q, visited_begin, visited_end)
#             if ans:
#                 return ans
#             ans = self.visitWord(p, visited_end, visited_begin)
#             if ans:
#                 return ans
                        
#         return 0


# DFS严重超时
# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         res = []
#         n = len(beginWord)
#         d = dict([(w,True) for w in wordList])
        
#         def DFS(word, visited, step):
#             # terminator
#             if word == endWord:
#                 if len(res) == 0:
#                     res.append(step + 1)
#                 elif res[0] > step + 1:
#                     res[0] = step + 1
#                 return
            
#             if len(res) > 0 and step + 1 > res[0]:
#                 return 
            
#             for i in range(n):
#                 for c in 'abcdefghijklmnopqrstuvwxyz':
#                     w = word[:i] + c + word[i+1:]
#                     if w in d and w not in visited:
#                         DFS(w, visited | {w}, step+1)
                        
#         DFS(beginWord, set(), 0)
#         return min(res) if len(res) > 0 else 0     

# from collections import deque
# from collections import defaultdict

# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         res = []
#         if beginWord == endWord:
#             return 0
#         if endWord not in wordList:
#             return 0
        

#         L = len(beginWord)
#         #通过单词的通用规则比如hit可以变换为h*t,*it,hi* 等情况找到字典里面所有的word对应关系
#         #这样就可以利用索引的方式来查找结果，时间复杂度O(1),这里的两遍循环的时间复杂度是O(n*m),m为单词的长度
#         all_combo_dict = defaultdict(list)
#         for word in wordList:
#             for i in range(L):
#                 # Key is the generic word
#                 # Value is a list of words which have the same intermediate generic word.
#                 all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

#         # Queue for BFS
#         queue = deque()
#         # current, previous, step
#         queue.append([beginWord, 1]) 
#         #为了防止出现环，使用访问数组记录
#         visited = {beginWord:True}
#         while queue:
#             current, step = queue.popleft()
#             # 单词长度相同
#             for i in range(L):
#                 intermediate_word = current[:i] + "*" + current[i+1:]
            
#                 for node in all_combo_dict[intermediate_word]:
#                     if node == endWord:
#                         return step + 1
#                     if node not in visited:
#                         visited[node] = True
#                         queue.append([node, step + 1])
#                 # 避免重复计算，可以不用
#                 # all_combo_dict[intermediate_word] = []
        
#         if len(res) > 0: return min(res)
#         return 0
        
        
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
#     ret = obj.ladderLength("qa",
# "sq",
# ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])
    ret = obj.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])
    print(ret)