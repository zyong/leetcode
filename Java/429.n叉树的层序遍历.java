import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

import org.w3c.dom.Node;

/*
 * @lc app=leetcode.cn id=429 lang=java
 *
 * [429] N叉树的层序遍历
 */
// 解题思路
// 1.递归
//  1.逐层递归，添加每层的所有元素
//  

// @lc code=start
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        
        ArrayList<Node> nodeList = new ArrayList<>();
        nodeList.add(root);
        levelOrder(res, nodeList);
        return res;
    }

    private void levelOrder(List<List<Integer>> res, List<Node> sons) {
        if (sons.size() == 0) {
            return;
        }

        ArrayList<Node> temp = new ArrayList<>();
        ArrayList<Integer> ret = new ArrayList<>();

        for (Node node : sons) {
            if (node.children.size() > 0) {
                temp.addAll(node.children);
            }
            ret.add(node.val);
        }
        res.add(ret);
        levelOrder(res, temp);
    }

    
}
// @lc code=end

