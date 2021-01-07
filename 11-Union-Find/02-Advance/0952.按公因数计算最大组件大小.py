#
# @lc app=leetcode.cn id=952 lang=python3
#
# [952] 按公因数计算最大组件大小
#
# https://leetcode-cn.com/problems/largest-component-size-by-common-factor/description/
#
# algorithms
# Hard (33.38%)
# Likes:    38
# Dislikes: 0
# Total Accepted:    2K
# Total Submissions: 6K
# Testcase Example:  '[4,6,15,35]'
#
# 给定一个由不同正整数的组成的非空数组 A，考虑下面的图：
#
#
# 有 A.length 个节点，按从 A[0] 到 A[A.length - 1] 标记；
# 只有当 A[i] 和 A[j] 共用一个大于 1 的公因数时，A[i] 和 A[j] 之间才有一条边。
#
#
# 返回图中最大连通组件的大小。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：[4,6,15,35]
# 输出：4
#
#
#
# 示例 2：
#
#
# 输入：[20,50,9,63]
# 输出：2
#
#
#
# 示例 3：
#
#
# 输入：[2,3,6,7,4,12,21,39]
# 输出：8
#
#
#
#
#
# 提示：
#
#
# 1
# 1
#
#
#

# @lc code=start
from math import sqrt
from typing import List


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        max_val = max(A)
        uf = UnionFind(max_val+1)

        for num in A:
            upper = sqrt(num)+1
            for i in range(2, int(upper)):
                if num % i == 0:
                    uf.union(num, i)
                    uf.union(num, num//i)

        cnt = [0]*(max_val+1)
        res = 0
        for num in A:
            root = uf.find(num)
            cnt[root] += 1
            res = max(res, cnt[root])

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
