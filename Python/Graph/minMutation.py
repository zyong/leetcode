#
# @lc app=leetcode.cn id=433 lang=python
#
# [433] 最小基因变化
# 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
# 假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
# 例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
# 与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。

# 现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，
# 请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。

# 注意:
# 起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
# 所有的目标基因序列必须是合法的。
# 假定起始基因序列与目标基因序列是不一样的。
# 示例 1:

# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]

# 返回值: 1

#

# 解题思路
# 1.BFS 通过几步能找到你需要的元素
#   1.而广度遍历是不断构建每层的可能性，然后搜索这层的下一层是否满足,只要找到满足就停止
#   2.同时需要保证每次先进入的孩子，优先被弹出，然后检查它的下一层是否满足，只有这样才能保证检查的顺序是一层层的
#   3。满足的条件就是当前字符串和变化字符串就差一个元素

# @lc code=start

import collections

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        queue = collections.deque()
        queue.append([start, start, 0]) # current , previous, step
        visited = {}
        while queue:
            current, previous, step = queue.popleft()
            if current == end:
                return step
            visited[current] = True

            for string in bank:
                if string not in visited and self.validMutation(current, string) and string != previous:
                    queue.append([string, current, step+1])
                    
        return -1
                
    def validMutation(self, current_gene, next_gene):
        changes = 0
        length = len(current_gene)
        for i in range(length):
            if current_gene[i] != next_gene[i]:
                changes += 1
        return changes == 1
        

#  BFS 简短实现
# class Solution(object):
    
#     def differOne(self, str1, str2):
#         return len([c1 for c1,c2 in zip(str1,str2) if c1 != c2]) <= 1
    
#     def bfs(self, start, end, bank):
#         q = collections.deque()
#         q.append((start, 0)) #(gene, level)
#         while q:
#             g = q.popleft()
#             if g[0] == end:
#                 return g[1]
#             #explore genes reachable from this one
#             ex = [(gx, g[1]+1) for gx,visited in bank.items() if not visited and self.differOne(g[0], gx)]
#             q.extend(ex)
#             for x in ex:
#                 bank[x[0]] = True
#         return -1
    
#     def minMutation(self, start, end, bank):
#         return self.bfs(start, end, {g: False for g in bank})


# @lc code=end

