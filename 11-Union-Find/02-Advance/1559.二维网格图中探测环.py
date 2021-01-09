#
# @lc app=leetcode.cn id=1559 lang=python3
#
# [1559] 二维网格图中探测环
#
# https://leetcode-cn.com/problems/detect-cycles-in-2d-grid/description/
#
# algorithms
# Hard (34.76%)
# Likes:    16
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 7.6K
# Testcase Example:  '[["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]'
#
# 给你一个二维字符网格数组 grid ，大小为 m x n ，你需要检查 grid 中是否存在 相同值 形成的环。
#
# 一个环是一条开始和结束于同一个格子的长度 大于等于 4
# 的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，可以移动的前提是这两个格子有 相同的值 。
#
# 同时，你也不能回到上一次移动时所在的格子。比方说，环  (1, 1) -> (1, 2) -> (1, 1) 是不合法的，因为从 (1, 2) 移动到
# (1, 1) 回到了上一次移动时的格子。
#
# 如果 grid 中有相同值形成的环，请你返回 true ，否则返回 false 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid =
# [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# 输出：true
# 解释：如下图所示，有 2 个用不同颜色标出来的环：
#
#
#
# 示例 2：
#
#
#
# 输入：grid =
# [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# 输出：true
# 解释：如下图所示，只有高亮所示的一个合法环：
#
#
#
# 示例 3：
#
#
#
# 输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# 输出：false
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m <= 500
# 1 <= n <= 500
# grid 只包含小写英文字母。
#
#
#

# @lc code=start


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(m*n)

        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i][j] == grid[i-1][j]:
                    if uf.find(i*n+j) == uf.find((i-1)*n+j):
                        return True
                    uf.union(i*n+j, (i-1)*n+j)
                if j > 0 and grid[i][j] == grid[i][j-1]:
                    if uf.find(i*n+j) == uf.find(i*n+j-1):
                        return True
                    uf.union(i*n+j, i*n+j-1)
        return False


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
