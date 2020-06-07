/* 
 * @lc app=leetcode.cn id=679 lang=java
 *
 * [679] 24 点游戏
 * 处理逻辑是4张牌里面任意选两个进行4种操作，
 * 然后3张牌里面任意选两个进行4中操作，
 * 然后2张牌任意选两个进行4中操作
 * 可能的选择情况是，（12*4)*(6*4)*(2*4) = 9216
 * 12*4 的理解应该是4个里面任意选2个数的组合，这两个数字进行4中操作
 * 第一轮循环，假设为1 2 3 4 四个数字
 * 4张牌全排列是4的阶乘，4！= 24，由于要每次取两个数字，
 * 两个一样的数字如下会有重复的排列，需要去重，
 * 后面的部分是下一轮要考虑的，第一轮不考虑所以全排列结果除以2来进行计算所以是12；
 * 1 2 3 4, 1 2 4 3, 1 3 2 4, 1 3 4 3, 1 4 2 3, 1 4 3 2, 
 * 2 1 3 4, 2 1 4 3, 2 3 1 4, 2 3 4 1, 2 4 1 3, 2 4 3 1,
 * 3 1 2 4, 3 1 4 2, 3 2 1 4, 3 2 4 1, 3 4 1 2, 3 4 2 1,
 * 4 1 2 3, 4 1 3 2, 4 2 1 3, 4 2 3 1, 4 3 1 2, 4 3 2 1
 * 
 * 第二轮循环假设为 2 3 4 三个数字
 * 2 3 4, 2 4 3, 3 2 4, 3 4 2, 4 2 3, 4 3 2
 * 
 * 第三轮循环假设为 4 6 两个数字
 * 4 6，6 4
 * 
 */

// @lc code=start
class Solution {
    public boolean judgePoint24(int[] nums) {
        ArrayList<Double> A = new ArrayList<>();
        for (int v: nums) A.add((double) v);
        return solve(A);
    }

    private boolean solve(ArrayList<Double> nums) {
        // 没有可计算的，证明无解
        if (nums.size() == 0) return false;
        // le-6是浮点计算的进度误差，这里判断误差小于1e-6，这样就是正确结果
        if (nums.size() == 1) return Math.abs(nums.get(0) - 24) < 1e-6;


        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (i != j) {
                    // 找到当前排列下的其他两个元素
                    ArrayList<Double> nums2 = new ArrayList<>();
                    for (int k = 0; k < nums.size(); k++) {
                        if (k != i && k != j) {
                            nums2.add(nums.get(k));
                        }
                    }
                    
                    // k的四种计算情况
                    for (int k = 0; k < 4; k++) {
                        // 性能优化，当k<2时，对于+ or *不考虑顺序，
                        // 所以k<2 时，j > i与i > j的结果相同，所以有部分不用考虑
                        if (k < 2 && j > i) continue;
                        if (k == 0) nums2.add(nums.get(i) + nums.get(j));
                        if (k == 1) nums2.add(nums.get(i) * nums.get(j));
                        if (k == 2) nums2.add(nums.get(i) - nums.get(j));
                        // 避免除数为0
                        if (k == 3) {
                            if (nums.get(j) != 0) {
                                nums2.add(nums.get(i) / nums.get(j));
                            } else {
                                continue;
                            }
                        }
                        // 在这次计算后，判断剩下的元素是否符合要求
                        // 每次缩小计算范围
                        if (solve(nums2)) return true;
                        // 移除最后一个计算结果，因为最后的记过不满足要求
                        // 就是一种回溯方法，将前面添加的结果删除
                        nums2.remove(nums2.size() - 1);
                    }
                }
            }
        }
        return false;
    }
}

// @lc code=end

