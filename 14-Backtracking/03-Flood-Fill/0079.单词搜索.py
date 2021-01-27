#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (43.77%)
# Likes:    757
# Dislikes: 0
# Total Accepted:    134.5K
# Total Submissions: 305.5K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例:
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#
#
#
# 提示：
#
#
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
#
#
#

# @lc code=start

from typing import List
from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[0]*cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        length = len(word)

        def dfs(i, j, begin):
            if begin == length-1:
                return board[i][j] == word[begin]

            if board[i][j] == word[begin]:
                visited[i][j] = 1
                for d in directions:
                    newi = i+d[0]
                    newj = j+d[1]
                    if inArea(newi, newj, rows, cols) and not visited[newi][newj]:
                        if dfs(newi, newj, begin+1):
                            return True
                visited[i][j] = 0
            return False

        def inArea(i, j, rows, cols):
            if 0 <= i < rows and 0 <= j < cols:
                return True
            else:
                return False

        for i in range(0, rows):
            for j in range(0, cols):
                if dfs(i, j, 0):
                    return True
        return False


# @lc code=end
