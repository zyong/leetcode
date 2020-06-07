/*
 * @lc app=leetcode.cn id=542 lang=java
 *
 * [542] 01 矩阵
 */

// @lc code=start
/* class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        // 首先将所有的 0 都入队，并且将 1 的位置设置成 -1，表示该位置是 未被访问过的 1
        Queue<int[]> queue = new LinkedList<>();
        int m = matrix.length;
        int n = matrix[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    queue.offer(new int[] {i, j});
                } else {
                    matrix[i][j] = -1;
                } 
            }
        }
        
        int[] dx = new int[] {-1, 1, 0, 0};
        int[] dy = new int[] {0, 0, -1, 1};
        while (!queue.isEmpty()) {
            int[] point = queue.poll();
            int x = point[0], y = point[1];
            for (int i = 0; i < 4; i++) {
                int newX = x + dx[i];
                int newY = y + dy[i];
                // 如果四邻域的点是 -1，表示这个点是未被访问过的 1
                // 所以这个点到 0 的距离就可以更新成 matrix[x][y] + 1。
                // 由于第一次加入queue的都是0的队列，所以找到的任意元素都是1
                // 由于队列的读取顺序，再将1加入队列，进行查找得到的元素都是2
                // 依次类推知道所有节点都找到
                if (newX >= 0 && newX < m && newY >= 0 && newY < n 
                        && matrix[newX][newY] == -1) {
                    matrix[newX][newY] = matrix[x][y] + 1;
                    queue.offer(new int[] {newX, newY});
                }
            }
        }

        return matrix;
    }
} */



// 动态规划
//  https://leetcode-cn.com/problems/01-matrix/solution/01ju-zhen-by-leetcode-solution/
class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] f = new int[m][n];

        // 设置矩阵某点为1的值为其他值
        for(int i = 0 ; i < m ; i++){
           for(int j = 0 ; j < n ; j++){
               if(matrix[i][j] == 1){
                   f[i][j] = Integer.MAX_VALUE / 2;
               }
           }
        }

        // 取上边和左边的值+1的最小值
        for(int i = 0 ; i < m ; i++){
           for(int j = 0 ; j < n ; j++){
                // 取向上一个位置的值+1和当前位置值比较，取较小值
               if(i > 0 ){
                   f[i][j] = Math.min(f[i][j],f[i-1][j] + 1);
               }
                // 取左边位置的值+1和当前位置的值比较，取最小值
               if(j > 0 ){
                   f[i][j] = Math.min(f[i][j],f[i][j-1] + 1);
               }
           }
        }

        // 取下边和右边的值的最小值+1
        for(int i = m-1 ; i >= 0 ; i--){
           for(int j = n-1 ; j >= 0 ; j--){
                // 取下面位置的值+1和当前位置值比较，取最小值
               if(i < m - 1){
                   f[i][j] = Math.min(f[i][j],f[i+1][j] + 1);
               }
               if(j < n - 1){
                   f[i][j] = Math.min(f[i][j],f[i][j+1] + 1);
               }
           }
        }
        return f;
    }
}
// @lc code=end

