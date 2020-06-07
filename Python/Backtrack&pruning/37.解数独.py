# -*- coding:utf-8 -*-
#
# @lc app=leetcode.cn id=37 lang=python
#
# [37] 解数独
#
# 解题思路
# 1.回溯+剪枝
#   1.遍历元素获取已经放入的1-9范围
#   2.递归节点，查找所有可能，如果没有可能就剪枝

# @lc code=start

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 判断条件，行 列 宫格,初始所有可用的值
        rows = [set(range(1,10)) for _ in range(9)]
        cols = [set(range(1,10)) for _ in range(9)]
        boxes = [set(range(1,10)) for _ in range(9)]
        
        empty = []
        # 检查所有元素，
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    rows[i].remove(val)
                    cols[j].remove(val)
                    boxes[i // 3 * 3 + j // 3].remove(val)
                else:
                    #记录哪些是可以填入值的
                    empty.append((i,j))
        
        def backtrack(iter=0):
            if iter == len(empty): return True
            
            i, j = empty[iter]
            for val in rows[i] & cols[j] & boxes[i // 3 * 3 + j // 3]:
                rows[i].remove(val)
                cols[j].remove(val)
                boxes[i// 3 * 3 + j // 3].remove(val)
                board[i][j] = str(val)
                if backtrack(iter + 1):
                    return True
                
                rows[i].add(val)
                cols[j].add(val)
                boxes[i// 3 * 3 + j // 3].add(val)
            return False
        
        backtrack()
                

                
        

# from collections import defaultdict
# class Solution:
#     def solveSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: void Do not return anything, modify board in-place instead.
#         """
#         def could_place(d, row, col):
#             """
#             Check if one could place a number d in (row, col) cell
#             """
#             return not (d in rows[row] or d in columns[col] or \
#                     d in boxes[box_index(row, col)])
        
#         def place_number(d, row, col):
#             """
#             Place a number d in (row, col) cell
#             """
#             rows[row][d] += 1
#             columns[col][d] += 1
#             boxes[box_index(row, col)][d] += 1
#             board[row][col] = str(d)
            
#         def remove_number(d, row, col):
#             """
#             Remove a number which didn't lead 
#             to a solution
#             """
#             del rows[row][d]
#             del columns[col][d]
#             del boxes[box_index(row, col)][d]
#             board[row][col] = '.'    
            
#         def place_next_numbers(row, col):
#             """
#             Call backtrack function in recursion
#             to continue to place numbers
#             till the moment we have a solution
#             """
#             # if we're in the last cell
#             # that means we have the solution
#             if col == N - 1 and row == N - 1:
#                 sudoku_solved[0] = True
#             #if not yet    
#             else:
#                 # if we're in the end of the row
#                 # go to the next row
#                 if col == N - 1:
#                     backtrack(row + 1, 0)
#                 # go to the next column
#                 else:
#                     backtrack(row, col + 1)
                
                
#         def backtrack(row = 0, col = 0):
#             """
#             Backtracking
#             """
#             # if the cell is empty
#             if board[row][col] == '.':
#                 # iterate over all numbers from 1 to 9
#                 for d in range(1, 10):
#                     if could_place(d, row, col):
#                         place_number(d, row, col)
#                         place_next_numbers(row, col)
#                         # print(board)
#                         # if sudoku is solved, there is no need to backtrack
#                         # since the single unique solution is promised
#                         if not sudoku_solved[0]:
#                             remove_number(d, row, col)
#             else:
#                 place_next_numbers(row, col)
                    
#         # box size
#         n = 3
#         # row size
#         N = n * n
#         # lambda function to compute box index
#         box_index = lambda row, col: (row // n ) * n + col // n
        
#         # init rows, columns and boxes
#         rows = [defaultdict(int) for i in range(N)]
#         columns = [defaultdict(int) for i in range(N)]
#         boxes = [defaultdict(int) for i in range(N)]
#         for i in range(N):
#             for j in range(N):
#                 if board[i][j] != '.': 
#                     d = int(board[i][j])
#                     place_number(d, i, j)
        
#         sudoku_solved = {}
#         sudoku_solved[0] = False
#         backtrack()


# class Solution(object):
#     def solveSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: None Do not return anything, modify board in-place instead.
#         """
        
#         def index(i, j):
#             return  (i//3) * 3 + j // 3

#         def could_place(x, row, col):
#             return not (x in rows[row] or x in cols[col] or \
#                  x in boxs[index(col, row)])
        
#         def place(x, i, j):
#             rows[i].append(x)
#             cols[j].append(x)
#             boxs[index(i,j)].append(x)
#             board[i][j] = x
            
#         def remove(x, i, j):
#             board[i][j] = '.'
#             rows[i].remove(x)
#             cols[j].remove(x)
#             boxs[index(i,j)].remove(x)
            
#         def place_next(row, col):
#             if row == m - 1 and col == m - 1:
#                 sudu[0] = True
#             else:
#                 if col + 1 == m:
#                     backtrace(row + 1, 0)
#                 else:
#                     backtrace(row, col + 1)
           
#         def backtrace(row = 0, col = 0):
#             if board[row][col] == '.':
#                 for x in range(1,10):
#                     if could_place(x, row, col):
#                         place(x, row, col)
#                         place_next(row, col)
#                         print(board)

#                         if not sudu[0]:
#                              remove(x, row, col)
#             else:                    
#                 place_next(row, col)
        
        
#         m = 9
#         cols = [[0] * 9 for _ in range(9)]
#         rows = [[0] * 9 for _ in range(9)]
#         boxs = [[0] * 9 for _ in range(9)]
#         sudu = {0:False}
        
#         for i in range(m):
#             for j in range(m):
#                 if board[i][j] != '.':
#                     d = int(board[i][j])
#                     place(d, i, j)
        
#         backtrace()
#         return board
    
# @lc code=end

