/*
 * @lc app=leetcode.cn id=221 lang=cpp
 *
 * [221] 最大正方形
 */

// @lc code=start
#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char> >& matrix) {
        if(matrix.empty())
            return 0;
        int m=matrix.size(),n=matrix[0].size(),size=0;
        vector<int> pre(n,0),cur(n,0);
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(!i||!j||matrix[i][j]=='0')
                    cur[j]=matrix[i][j]-'0';
                else
                    cur[j]=min(pre[j-1],min(pre[j],cur[j-1]))+1;
                size=max(cur[j],size);
            }
            fill(pre.begin(),pre.end(),0);
            swap(pre,cur);
        }
        return size*size;
    }
};

int main() {
    Solution obj;
    char arr[4][6] = {
        "10100",
        "10111",
        "11111",
        "10010"
    };
    // vector初始化如果在定义时使用的初始化参数，就会设置相应的空间大小
    // 后面新加的元素会增加到先前定义的后面，先前定义如果没有赋值，会给初始值
    vector<vector<char> > vc;
    for(int i=0; i<4; i++) {
        vector<char> a(arr[i], arr[i] + 6);
        vc.push_back(a);
    }

    int ret = obj.maximalSquare(vc);
    cout << ret << endl;
}
// @lc code=end

