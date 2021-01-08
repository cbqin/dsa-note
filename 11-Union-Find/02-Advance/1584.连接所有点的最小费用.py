#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#
# https://leetcode-cn.com/problems/min-cost-to-connect-all-points/description/
#
# algorithms
# Medium (51.31%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 7.8K
# Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
#
# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
#
# 连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示
# val 的绝对值。
#
# 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
#
#
#
# 示例 1：
#
#
#
#
# 输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# 输出：20
# 解释：
#
# 我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
# 注意到任意两个点之间只有唯一一条路径互相到达。
#
#
# 示例 2：
#
#
# 输入：points = [[3,12],[-2,5],[-4,1]]
# 输出：18
#
#
# 示例 3：
#
#
# 输入：points = [[0,0],[1,1],[1,0],[-1,1]]
# 输出：4
#
#
# 示例 4：
#
#
# 输入：points = [[-1000000,-1000000],[1000000,1000000]]
# 输出：4000000
#
#
# 示例 5：
#
#
# 输入：points = [[0,0]]
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= points.length <= 1000
# -10^6 <= xi, yi <= 10^6
# 所有点 (xi, yi) 两两不同。
#
#
#

# @lc code=start

from typing import List
from heapq import heapify, heappop


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        queue = []
        for i in range(n):
            for j in range(i+1, n):
                x = points[i]
                y = points[j]
                queue.append((abs(x[0]-y[0])+abs(x[1]-y[1]), i, j))
        heapify(queue)

        uf = UnionFind(n)
        res = 0
        while uf.getCount() > 1:
            pop = heappop(queue)
            cost = pop[0]
            x = pop[1]
            y = pop[2]
            if uf.find(x) == uf.find(y):
                continue
            uf.union(x, y)
            res += cost
        return res


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
