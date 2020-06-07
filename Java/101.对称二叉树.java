import java.util.HashSet;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode.cn id=101 lang=java
 *
 * [101] 对称二叉树
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 * 
 * 递归
 * 每次判断左边的孩子和右边的孩子是不是都对称
 * 1、注意对称是左边孩子的左边与右边孩子的右边相同，
 * 左孩子的右边和右孩子的左边相同，这样才能对称。
 * 2、root节点如果为null也是对称的
 * 3、在递归开头解决掉null的情况，这样后面就可以不用判断了
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return recurCompare(root.left, root.right);
    }

    private boolean recurCompare(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        }
        if (left == null || right == null ) {
            return false;
        }

        return left.val == right.val
            && recurCompare(left.left, right.right) 
            && recurCompare(left.right, right.left);
    }
}
// @lc code=end

