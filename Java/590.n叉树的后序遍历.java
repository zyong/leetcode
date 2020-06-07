import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=590 lang=java
 *
 * [590] N叉树的后序遍历
 */
// 后续没什么好说的，就是左右根
// 1.递归

// @lc code=start

// Definition for a Node.
// class Node {
//     public int val;
//     public List<Node> children;

//     public Node() {}

//     public Node(int _val) {
//         val = _val;
//     }

//     public Node(int _val, List<Node> _children) {
//         val = _val;
//         children = _children;
//     }
// };

class Solution {
    public List<Integer> postorder(Node root) {
        List<Integer> res = new ArrayList<>();

        if (root == null) {
            return res;
        }

        // 先左右，再根
        // n层的情况，就不断找下层元素，直到叶子节点，然后输出叶子节点到list
        if (root.children.size() == 0) {
            res.add(root.val);
            return res;
        }

        postorder(root, res);
        return res;

        
    }

    private void postorder(Node node, List<Integer> res) {
        if (node.children.size() == 0) {
            res.add(node.val);
            return;
        }

        for (Node c : node.children) {
            postorder(c, res);
        }

        res.add(node.val);
    }
}
// @lc code=end

