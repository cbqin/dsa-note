#
# @lc app=leetcode.cn id=765 lang=python3
#
# [765] 情侣牵手
#
# https://leetcode-cn.com/problems/couples-holding-hands/description/
#
# algorithms
# Hard (59.40%)
# Likes:    114
# Dislikes: 0
# Total Accepted:    9.4K
# Total Submissions: 15.8K
# Testcase Example:  '[0,2,1,3]'
#
# N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。
# 一次交换可选择任意两人，让他们站起来交换座位。
#
# 人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2,
# 2N-1)。
#
# 这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。
#
# 示例 1:
#
#
# 输入: row = [0, 2, 1, 3]
# 输出: 1
# 解释: 我们只需要交换row[1]和row[2]的位置即可。
#
#
# 示例 2:
#
#
# 输入: row = [3, 2, 0, 1]
# 输出: 0
# 解释: 无需交换座位，所有的情侣都已经可以手牵手了。
#
#
# 说明:
#
#
# len(row) 是偶数且数值在 [4, 60]范围内。
# 可以保证row 是序列 0...len(row)-1 的一个全排列。
#
#
#

# @lc code=start

from typing import List


class Solution:
    # def minSwapsCouples(self, row: List[int]) -> int:
    #     ans = 0
    #     position = {}
    #     for i, num in enumerate(row):
    #         position[num] = i

    #     for i in range(0, len(row), 2):
    #         x = row[i]
    #         if row[i+1] == x ^ 1:
    #             continue
    #         ans += 1
    #         j = position[x ^ 1]
    #         row[i+1], row[j] = row[j], row[i+1]
    #         position[row[i+1]] = i+1
    #         position[row[j]] = j

    #     return ans

    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)//2
        uf = UnionFind(n)
        for i in range(n):
            uf.union(row[2*i]//2, row[2*i+1]//2)
        return n-uf.getCount()


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
