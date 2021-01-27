#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (73.38%)
# Likes:    730
# Dislikes: 0
# Total Accepted:    99.8K
# Total Submissions: 135.6K
# Testcase Example:  '4'
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
#
#
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#
#
# 示例 1：
#
#
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：[["Q"]]
#
#
#
#
# 提示：
#
#
# 1
# 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
#
#
#
#
#

# @lc code=start


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        main = set()
        sub = set()
        cols = set()
        res = []

        def dfs(row, path):
            if row == n:
                res.append(convert(path))
                return

            for col in range(n):
                if row-col not in main and row+col not in sub and col not in cols:
                    main.add(row-col)
                    sub.add(row+col)
                    cols.add(col)
                    path.append(col)
                    dfs(row+1, path)
                    main.remove(row-col)
                    sub.remove(row+col)
                    cols.remove(col)
                    path.pop()

        def convert(path):
            r = []
            for num in path:
                line = ["."]*n
                line[num] = "Q"
                r.append("".join(line))
            return r

        dfs(0, [])
        return res

# @lc code=end
