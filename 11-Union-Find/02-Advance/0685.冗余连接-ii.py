#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#
# https://leetcode-cn.com/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (44.64%)
# Likes:    210
# Dislikes: 0
# Total Accepted:    16.2K
# Total Submissions: 36.3K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。
#
# 输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N)
# 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
#
# 结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。
#
# 返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
#
# 示例 1:
#
# 输入: [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 解释: 给定的有向图如下:
# ⁠ 1
# ⁠/ \
# v   v
# 2-->3
#
#
# 示例 2:
#
# 输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# 输出: [4,1]
# 解释: 给定的有向图如下:
# 5 <- 1 -> 2
# ⁠    ^    |
# ⁠    |    v
# ⁠    4 <- 3
#
#
# 注意:
#
#
# 二维数组大小的在3到1000范围内。
# 二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。
#
#
#

# @lc code=start
from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        in_degrees = [0]*(n+1)
        for edge in edges:
            in_degrees[edge[1]] += 1

        for i in range(n-1, -1, -1):
            if in_degrees[edges[i][1]] == 2:
                if not self.isCircle(edges, i):
                    return edges[i]

        for i in range(n-1, -1, -1):
            if in_degrees[edges[i][1]] == 1:
                if not self.isCircle(edges, i):
                    return edges[i]

    def isCircle(self, edges, index):
        n = len(edges)
        uf = UnionFind(n+1)
        for i in range(n-1, -1, -1):
            if i == index:
                continue
            if uf.find(edges[i][0]) == uf.find(edges[i][1]):
                return True
            uf.union(edges[i][0], edges[i][1])
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
