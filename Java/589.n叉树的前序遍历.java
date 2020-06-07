import java.util.ArrayList;
import java.util.List;


/*
 * @lc app=leetcode.cn id=589 lang=java
 *
 * [589] N叉树的前序遍历
 */
// 前序遍历就是根左右的顺序
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
    public List<Integer> preorder(Node root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) {
            return res;
        }

        // res.add(root.val);
        preorder(root, res);
        return res;
    }

    private void preorder(Node root, List<Integer> res) {
        if (root.children.size() == 0) {
            res.add(root.val);
            return;
        }

        res.add(root.val);
        for (Node node : root.children) {
            preorder(node, res);
        }

    }
    
}
// @lc code=end

