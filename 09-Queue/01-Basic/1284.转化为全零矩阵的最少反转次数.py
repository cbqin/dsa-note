#
# @lc app=leetcode.cn id=1284 lang=python3
#
# [1284] 转化为全零矩阵的最少反转次数
#
# https://leetcode-cn.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/description/
#
# algorithms
# Hard (65.06%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    2.1K
# Total Submissions: 3.2K
# Testcase Example:  '[[0,0],[0,1]]\r'
#
# 给你一个 m x n 的二进制矩阵 mat。
#
# 每一步，你可以选择一个单元格并将它反转（反转表示 0 变 1 ，1 变 0
# ）。如果存在和它相邻的单元格，那么这些相邻的单元格也会被反转。（注：相邻的两个单元格共享同一条边。）
#
# 请你返回将矩阵 mat 转化为全零矩阵的最少反转次数，如果无法转化为全零矩阵，请返回 -1 。
#
# 二进制矩阵的每一个格子要么是 0 要么是 1 。
#
# 全零矩阵是所有格子都为 0 的矩阵。
#
#
#
# 示例 1：
#
#
#
# 输入：mat = [[0,0],[0,1]]
# 输出：3
# 解释：一个可能的解是反转 (1, 0)，然后 (0, 1) ，最后是 (1, 1) 。
#
#
# 示例 2：
#
# 输入：mat = [[0]]
# 输出：0
# 解释：给出的矩阵是全零矩阵，所以你不需要改变它。
#
#
# 示例 3：
#
# 输入：mat = [[1,1,1],[1,0,1],[0,0,0]]
# 输出：6
#
#
# 示例 4：
#
# 输入：mat = [[1,0,0],[1,0,0]]
# 输出：-1
# 解释：该矩阵无法转变成全零矩阵
#
#
#
#
# 提示：
#
#
# m == mat.length
# n == mat[0].length
# 1 <= m <= 3
# 1 <= n <= 3
# mat[i][j] 是 0 或 1 。
#
#
#

# @lc code=start


class Solution:
    def encode(self, mat, m, n):
        x = 0
        for i in range(m):
            for j in range(n):
                x = x*2+mat[i][j]
        return x

    def decode(self, x, m, n):
        mat = [[0]*n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mat[i][j] = x & 1
                x >>= 1
        return mat

    def convert(self, mat, m, n, i, j):
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1), (0, 0)]:
            i0, j0 = i+di, j+dj
            if 0 <= i0 < m and 0 <= j0 < n:
                mat[i0][j0] ^= 1

    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        start = self.encode(mat, m, n)
        step = 0
        if start == 0:
            return step

        visited = {start}
        deque = collections.deque()
        deque.append(start)

        while len(deque):
            step += 1
            size = len(deque)
            for _ in range(size):
                state = self.decode(deque.popleft(), m, n)
                for i in range(m):
                    for j in range(n):
                        self.convert(state, m, n, i, j)
                        curr = self.encode(state, m, n)
                        if curr == 0:
                            return step
                        if curr not in visited:
                            visited.add(curr)
                            deque.append(curr)
                        self.convert(state, m, n, i, j)
        return -1
# @lc code=end
