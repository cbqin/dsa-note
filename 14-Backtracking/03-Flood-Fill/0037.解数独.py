#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# https://leetcode-cn.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (66.86%)
# Likes:    737
# Dislikes: 0
# Total Accepted:    67.8K
# Total Submissions: 101.5K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 编写一个程序，通过填充空格来解决数独问题。
#
# 一个数独的解法需遵循如下规则：
#
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#
#
# 空白格用 '.' 表示。
#
#
#
# 一个数独。
#
#
#
# 答案被标成红色。
#
# 提示：
#
#
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
#
#
#

# @lc code=start


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [[0]*9 for _ in range(9)]
        col = [[0]*9 for _ in range(9)]
        box = [[[0]*9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    index = int(board[i][j])-1
                    row[i][index] = 1
                    col[j][index] = 1
                    box[i//3][j//3][index] = 1

        def dfs(board, i, j):
            if i == 9:
                return True

            if board[i][j] == '.':
                for index in range(9):
                    if row[i][index] or col[j][index] or box[i//3][j//3][index]:
                        continue
                    row[i][index] = 1
                    col[j][index] = 1
                    box[i//3][j//3][index] = 1
                    board[i][j] = str(index+1)

                    if dfs(board, i+(j+1)//9, (j+1) % 9):
                        return True

                    row[i][index] = 0
                    col[j][index] = 0
                    box[i//3][j//3][index] = 0
                    board[i][j] = '.'
            else:
                return dfs(board, i+(j+1)//9, (j+1) % 9)
            return False

        dfs(board, 0, 0)

# @lc code=end
