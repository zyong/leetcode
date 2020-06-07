#
# @lc app=leetcode.cn id=818 lang=python
#
# [818] 赛车
#
# 解题思路
# 1.dijkstra最小路径算法
# A^k 表示连续使用 k 次 A指令，这样就可以用A^1*R*A^2*RA^3...A^k, ki ≥0 表示任意一种指令列表。
# 注意到最优的指令列表不可能以 R 结束，因为R只是转向的作用，不会向前行，然后到了终点后转向是无意义的，所以不会以R结束。
# 也不会以R开头，因为两点
#    1、由于target的范围是1 <= target（目标位置） <= 10000, 车的起始位置是0，所以肯定是先向前行是最优解
#    2、假设R开头是最优就存在R*A^k1*R*A^k2...R*A^kn ，由于R只是改变反向, RA^k or RA^kR开头的部分就可以通过n的奇偶性放到命令末尾，就等于说
#    RA^k or RA^kR部分命令集是在开头和结尾对结果来说是一样的。因为它只起到转向然后反向移k步的作用，类似 X - n = -n + X
#    指令列表 A^k1 R A^k2..A^kn可以到达的位置为 (2^k1 - 1) - (2^k2 - 1) + (2^k3 - 1)... ，2^k 次方代表A执行K，每次speed都*2，
#    结果Position += speed,  但是都是从1的速度开始的，所以要-1；-(2^k2 - 1) 表示的意思正好相反，是R后再A命令的情况
#    3、2*ki-1存在上界，当第一次2*ki-1 >= target ,即赛车某时刻过终点必须折返。
# 2.dp
# https://leetcode-cn.com/problems/race-car/solution/sai-che-by-leetcode/
# 假设我们需要到达位置 x，且 2^(k-1) < x < 2^k, 我们用 dp[x] 表示到达位置 x 的最短指令长度。如果 t = 2^(k-1) 
# 那么我们只需要用 A^k  即可,就是A^k刚好到达目标。否则我们需要考虑两种情况：
#   1、我们首先用 A^(k-1) 到达位置 2^(k-1) - 1，随后折返并使用 A^j，这样我们到达了位置 2^(k-1)- 2^j，
#   使用的指令为 A^(k-1)*R*A^k, 长度为 k - 1 + j，剩余的距离为 x−(2^k−1 − 2^j) < x；
#   2、我们首先用 A^k 到达位置 2^k - 1，随后仅使用折返指令，此时我们已经超过了终点并且速度方向朝向终点，
#   使用的指令为 A^k*R，长度为 k + 1，剩余的距离为 x - (2^k) - 1 < x。

# 
# 
# @lc code=start

class Solution(object):
    def racecar(self, target):
        dp = [0, 1, 4] + [float('inf')] * target
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        return dp[target]



        
# @lc code=end

