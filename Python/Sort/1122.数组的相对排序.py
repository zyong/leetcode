#
# @lc app=leetcode.cn id=1122 lang=python
#
# [1122] 数组的相对排序
#
# 解题思路
# 1.循环查找 
#   1. 1遍循环*logN查找+自带排序
# 时间复杂度：O(N*M)
# 空间复杂度：O(N)

# 2.计数排序+两遍循环
#   1. 计数排序就是生成一个与数字最大数还大，同时个数还要长的数
#   2. 原有数组里面的每个数映射到索引里面，如果元素有多个就给数组值+1
#   3. 循环第二个数组，如果这个数在计数数组里面就添加到新数组
#   4. 将计数数组里面的剩余部分添加到新数组
# 时间复杂度：O(M+N*K+(N-M)*K)  T(N) = kT(n) + T(M) + kT(n-m) ~ T(n) + T(m) 
# 空间复杂度：O(N)

# @lc code=start
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # arr=[]
        # for i in arr2:
        #     while i in arr1:
        #         arr.append(i)
        #         arr1.remove(i)
        # return arr+sorted(arr1)
        
        arr = [0] * 1001
        res = []
        for i in arr1:
            arr[i] += 1
        for j in arr2:
            while arr[j] > 0:
                res.append(j)
                arr[j] -= 1
        for i in range(1001):
            while arr[i] > 0:
                res.append(i)
                arr[i] -= 1
        return res

# @lc code=end

