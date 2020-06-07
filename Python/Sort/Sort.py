# -*- coding:utf-8 -*-


import math
import test

class Solution(object):
    # 冒泡排序原理
    # 1.从第一个数开始，不断与后面的数字比较，如果后面比前面的大，就交换两个数字
    # 2.不断的进行交换，直到最后一个数字
    # 时间复杂度：O(N^2)
    # 空间复杂度：O(N) 在原数组上交换
    @staticmethod
    def bubbleSort(nums):
        """
        :type nums: List
        :rtype: List
        """
        
        if not nums:
            return nums
        
        n = len(nums)
        for i in range(n-1):
            for j in range(0, n-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        return nums

    # 选择排序原理
    # 1、第一次从所有元素里面选择最小（大）的元素放到头部
    # 2. 依次每轮从剩下的元素里面找最小（大）的元素放到已经有序的末尾
    # 时间复杂度：O(N^2)
    # 空间复杂度：O(N)
    @staticmethod
    def selectSort(nums):
        """
        :type nums: List
        :rtype: List
        """
        if not nums:
            return nums
        
        n = len(nums)
        
        for i in range(n):
            index = i
            for j in range(i, n):
                if nums[j] < nums[index]:
                    index = j
            nums[i],nums[index] = nums[index], nums[i]
        
        return nums
    
    
    # 插入排序原理
    # 1。插入排序都采用in-place在数组上实现。具体算法描述如下：
    #   1.从第一个元素开始，该元素可以认为已经被排序；
    #   2、取出下一个元素，在已经排序的元素序列中从后向前扫描；
    #   3.如果该元素（已排序）大于新元素，将该元素移到下一位置；
    #   4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
    #   5.将新元素插入到该位置后；
    #   重复步骤2~5。
    # 时间复杂度：O(n^2)
    # 空间复杂度：O(n)
    @staticmethod
    def insertSort(nums):
        """
        :type nums: List
        :rtype: List
        """
        n = len(nums)
        if not n:
            return nums
        
        for i in range(n):
            index = i - 1
            current = nums[i]
            while index >= 0 and nums[index] > current:
                nums[index+1] = nums[index]
                index -= 1
            nums[index+1] = current
        return nums
    
    
    # 归并原理
    # 1.采用分治法划分序列，然后逐个排序
    # 2.排序后再合并结果
    @staticmethod
    def mergeSort(nums):
        def merge(left, right):
            ans = []
            m,n = len(left),len(right)
            i = 0
            j = 0
            while i < m and j < n:
                if left[i] > right[j]:
                    ans.append(right[j])
                    j += 1
                else:
                    ans.append(left[i])
                    i += 1
                    
            while i < m: 
                ans.append(left[i])
                i += 1
            while j < n: 
                ans.append(right[j])
                j += 1
            return ans
        
        def _mergeSort(left, right):
            if left == right:
                return [nums[left]]
            
            mid = (left+right)>>1
            return merge(_mergeSort(left, mid), _mergeSort(mid+1, right))
            
        
        return _mergeSort(0, len(nums) - 1)
    
    # 
    # 快速排序原理
    # 1.快速排序就是从数据中找到一个基准pivot，把数据以基准分成两部分
    # 一部分比基准大，一部分比基准小
    # 2.找基准的过程就是先假设基准为left位置的值，以index=left+1为起点
    # 不断比较右值与基准，如果比基准小就和index交换，然后index+1
    # 3.以基准值的位置为中间点，然后分隔数组为两个部分，分别进行排序
    # 依次循环这个操作，直到左边索引等于右边索引
    # 
    # https://www.cnblogs.com/onepixel/p/7674659.html
    # 时间复杂度：O(logN) 
    # 最坏情况为倒序排列为O(n^2), 会退化为冒泡排序
    # 空间复杂度：O(N)
    @staticmethod
    def qsort(nums):
        """
        :type nums: List
        :rtype: List
        """
        
        if not nums:
            return nums
        
        # 产生基准位置
        def partition(left, right):
            pivot = left
            index = pivot+1
            for i in range(index, right+1):
                if nums[pivot] > nums[i]:
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1
            nums[pivot], nums[index-1] = nums[index-1], nums[pivot]
            return index-1
        
        def _qsort(left, right):
            # terminator
            if left >= right:
                return
            
            mid = partition(left, right)
            _qsort(left, mid)
            _qsort(mid+1, right)
            
        _qsort(0, len(nums)-1)
        
        return nums
    
    # 计数排序原理
    # 找出待排序的数组中最大元素；
    # 使用最大元素+1构建一个新数组，加一是保证最大元素可以放入下标从0开始的数组里面
    # 统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
    # 
    # 反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。
    # 时间复杂度:O(n)
    # 空间复杂度:O(n)
    @staticmethod
    def countingSort(nums):
        """
        :type nums: List
        :rtype: List
        """
        
        # 先找最大值
        maxVal = float('-inf')
        for i in nums:
            maxVal = max(maxVal, i)
            
        # 再生成数组
        arr = [0] * (maxVal + 1)
        for i in nums:
            arr[i] += 1
        
        ans = []
        for j in range(len(arr)):
            while arr[j] > 0:
                ans.append(j)
                arr[j] -= 1
        return ans

    # 堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
    # 堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
    # 时间复杂度O(nlogn)
    # 空间复杂度O(n)
    @staticmethod
    def heapSort(nums):        
        def heapify(h, i):
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            
            if left < length['len'] and h[left] > h[largest]:
                largest = left
            
            if right < length['len'] and h[right] > h[largest]:
                largest = right
                
            if largest != i:
                h[largest], h[i] = h[i], h[largest]
                heapify(h, largest)
    
        def _heapSort(nums):
            n = len(nums)
            for i in range(length['len']//2, -1, -1):
                heapify(nums, i)
                
            ans = []
            for i in range(n-1, -1, -1):
                nums[0], nums[i] = nums[i], nums[0]
                length['len'] = i
                heapify(nums, 0)
                ans.insert(0, nums[i])
            return ans
         
        n = len(nums)
        if n == 0:
            return 0

        n = len(nums)
        length = {'len':n}
        return _heapSort(nums)


    # Bucket Sort 桶排序
    # 桶排序类似于计数排序，由于使用映射函数，不会出现分配过大的数组导致爆掉的情况
    # 
    # 原理
    # 1、得到输入元素的最大值和最小值
    # 2. 建立一个特定大小的桶，bucket的size越大每个bucket里面的元素越少，排序越快
    # 3. 映射函数映射每个值到具体的bucket，分bucket是依据元素大小依次放入的。可以理解为倍数的不同依次放入
    # 这个也和最大最小值有关，比如1000条数组，分10个桶，每个桶里面都约是100份，输出的时候就可以按bucket依次输出就可以
    # 4.对每个bucket进行排序，依次将bucket里面结果输出
    # 时间复杂度：O(n + logn/k) 当 n 远大于k的时候 时间复杂度为O(n)
    # 空间复杂度：O(n)
    @staticmethod
    def buecktSort(nums, bucketSize=5):
        if len(nums) == 0:
            return nums
        
        # 取得最大值和最小值
        minVal = nums[0]
        maxVal = nums[0]
        for i in nums:
            if i < minVal:
                minVal = i
            elif i > maxVal:
                maxVal = i
        
        # 建立bucket
        DEFAULT_BUCKET_SIZE = 5
        bucketSize = bucketSize or DEFAULT_BUCKET_SIZE
        # 这句限制了传入的元素可以存着的桶的范围，也就是设置一个这么多bucket的桶，
        # 传入元素经过映射后一定在里面
        bucketCount = int(math.floor((maxVal - minVal) // bucketSize) + 1)
        buckets = [[] * 1 for _ in range(bucketCount)]
        
        for num in nums:
            buckets[int(math.floor((num - minVal) / bucketSize))].append(num)
        
        ans = []
        for i in range(bucketCount):
            # 排序数组
            buckets[i].sort()
            for num in buckets[i]:
                ans.append(num)
            
        return ans 
    
    # 基数排序
    # 原理
    # 从最低位依次向上对每个位划分位置，相当于对低位进行排序
    # 在基本有序的情况下，在对高位进行排序，如果位数少的肯定已经再低位上了
    # 位数多的会进入后面的bucket，就对每一位进行排序，最后得到有序的序列
    # 
    # 排序过程
    # 1.获取数组中的最大值的位数，计数数组为10个bucket的长度
    # 2。将数字从最低位开始计算bucket位置，依次排入计数数组的bucket
    # 3. 每完成一轮写入计数数组后将数组里面的数字依次取出覆盖原数组
    # 4.重复排序，都将每个数字的前一位取出重新放入计数数组里面排序
    # 知道所有数字都拍完
    # 时间复杂度:O(2n*k) k为最大位数，n为元素个数
    # 空间复杂度:O(n)
    @staticmethod
    def radixSort(nums):
        #找最大值
        length = float('-inf')
        for num in nums:
            n = len(str(num))
            if n > length:
                length = n

        arr = [[] * 1 for _ in range(10)]
        dev = 1
        mod = 10
        for _ in range(length):
            for num in nums:
                bucket = int((num % mod) / dev)
                arr[bucket].append(num)
            print(arr)
            dev *= 10
            mod *= 10
            pos = 0
            for j in range(10):
                while len(arr[j]) > 0:
                    nums[pos] = arr[j].pop(0)
                    pos += 1
        
        return nums

            
            
        
        
    

if __name__ == "__main__":
    test.test(Solution.bubbleSort)
    print("{}\n".format("--" * 50))
    test.test(Solution.selectSort)
    print("{}\n".format("--" * 50))
    test.test(Solution.qsort)
    print("{}\n".format("--" * 50))
    test.test(Solution.insertSort)
    print("{}\n".format("--" * 50))
    test.test(Solution.mergeSort)
    print("{}\n".format("--" * 50))
    test.test(Solution.heapSort)
    print("{}\n".format("--" * 50))
    test.test(Solution.buecktSort)
    print("{}\n".format("--" * 50))
    test.test(Solution.radixSort)




        
        
