#
# @lc app=leetcode.cn id=959 lang=python3
#
# [959] 由斜杠划分区域
#
# https://leetcode-cn.com/problems/regions-cut-by-slashes/description/
#
# algorithms
# Medium (67.60%)
# Likes:    117
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 6.3K
# Testcase Example:  '[" /","/ "]'
#
# 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。
#
# （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
#
# 返回区域的数目。
#
#
#
#
#
#
# 示例 1：
#
# 输入：
# [
# " /",
# "/ "
# ]
# 输出：2
# 解释：2x2 网格如下：
#
#
# 示例 2：
#
# 输入：
# [
# " /",
# "  "
# ]
# 输出：1
# 解释：2x2 网格如下：
#
#
# 示例 3：
#
# 输入：
# [
# "\\/",
# "/\\"
# ]
# 输出：4
# 解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
# 2x2 网格如下：
#
#
# 示例 4：
#
# 输入：
# [
# "/\\",
# "\\/"
# ]
# 输出：5
# 解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
# 2x2 网格如下：
#
#
# 示例 5：
#
# 输入：
# [
# "//",
# "/ "
# ]
# 输出：3
# 解释：2x2 网格如下：
#
#
#
#
#
# 提示：
#
#
# 1 <= grid.length == grid[0].length <= 30
# grid[i][j] 是 '/'、'\'、或 ' '。
#
#
#

# @lc code=start

from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(4*n*n)

        for i in range(n):
            for j in range(n):
                root = 4*(i*n+j)
                if grid[i][j] != '\\':
                    uf.union(root+0, root+3)
                    uf.union(root+1, root+2)
                if grid[i][j] != '/':
                    uf.union(root+0, root+1)
                    uf.union(root+2, root+3)
                if i < n-1:
                    uf.union(root+2, 4*((i+1)*n+j))
                if j < n-1:
                    uf.union(root+1, 4*(i*n+j+1)+3)

        return uf.getCount()


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
