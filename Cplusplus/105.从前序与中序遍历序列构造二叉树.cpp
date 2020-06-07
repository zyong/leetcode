/*
 * @lc app=leetcode.cn id=105 lang=cpp
 *
 * [105] 从前序与中序遍历序列构造二叉树
 */

// @lc code=start
/* *
 * Definition for a binary tree node.
 */


#include <vector>
#include <unordered_map>

using namespace std;

/*  struct TreeNode {
     int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
}; */

class Solution {
public:
    vector<int> preorder;
    vector<int> inorder;
    unordered_map<int, int> inMap;
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        this->preorder = preorder;
        this->inorder = inorder;

        for (int i=0; i<preorder.size(); i++) {
            inMap[inorder[i]] = i;
        }
        return buildTree(0, preorder.size()-1, 0, inorder.size()-1);
    }

    TreeNode* buildTree(int preStart, int preEnd, int inStart, int inEnd) {
        if (preStart > preEnd || inStart > inEnd) return nullptr;

        int inorder_root = inMap[preorder[preStart]];

        TreeNode* root = new TreeNode(preorder[preStart]);
        int left_subtree_size = inorder_root - inStart;
        root->left = buildTree(preStart+1, preStart + left_subtree_size, inStart, inorder_root - 1);
        root->right = buildTree(preStart + left_subtree_size + 1, preEnd, inorder_root+1, inEnd);

        return root;
    }
};
// @lc code=end

