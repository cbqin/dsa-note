#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (42.25%)
# Likes:    443
# Dislikes: 0
# Total Accepted:    83.2K
# Total Submissions: 196.8K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
# 示例:
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# 运行你的函数后，矩阵变为：
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# 解释:
#
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#
#

# @lc code=start


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if not row:
            return
        col = len(board[0])
        uf = UnionFind(row*col+1)
        dummy = row*col

        for j in range(col):
            if board[0][j] == 'O':
                uf.union(self.index(0, j, col), dummy)
            if board[row-1][j] == 'O':
                uf.union(self.index(row-1, j, col), dummy)

        for i in range(row):
            if board[i][0] == 'O':
                uf.union(self.index(i, 0, col), dummy)
            if board[i][col-1] == 'O':
                uf.union(self.index(i, col-1, col), dummy)

        directions = [[0, 1], [1, 0]]
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    for direction in directions:
                        newx = i+direction[0]
                        newy = j+direction[1]
                        if newx < row and newy < col and board[newx][newy] == 'O':
                            uf.union(self.index(newx, newy, col),
                                     self.index(i, j, col))

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    if uf.find(self.index(i, j, col)) != uf.find(dummy):
                        board[i][j] = 'X'

    def index(self, x, y, col):
        return x*col+y


class UnionFind(object):
    def __init__(self, N: int):
        self.N = N
        self.count = N
        self.parents = [0]*N
        self.rank = [1]*N

        for i in range(N):
            self.parents[i] = i

    # 路径压缩：隔代压缩
    def find(self, x: int) -> int:
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    # 路径压缩：完全压缩
    # def find(self, x: int) -> int:
    #     if x != self.parents[x]:
    #         self.parents[x] = self.find(self.parents[x])
    #     return self.parents[x]

    # O(mα(n))
    def union(self, x: int, y: int) -> None:
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return

        if self.rank[rootx] == self.rank[rooty]:
            self.parents[rootx] = rooty
            self.rank[rooty] += 1
        elif self.rank[rootx] < self.rank[rooty]:
            self.parents[rootx] = rooty
        else:
            self.parents[rooty] = rootx

        self.count -= 1

    def getCount(self) -> int:
        return self.count

# @lc code=end
