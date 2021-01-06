#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (52.29%)
# Likes:    644
# Dislikes: 0
# Total Accepted:    92K
# Total Submissions: 175.3K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
#
#
# 进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？
#
#
#
# 示例 1：
#
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
# 示例 2：
#
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
#
#
#
# 提示：
#
#
# 0
# -10^9
#
#
#

# @lc code=start


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        table = set(nums)
        res = 1
        for num in nums:
            cnt = 1
            if num-1 in table:
                continue
            while num+1 in table:
                cnt += 1
                num += 1
            res = max(res, cnt)
        return res


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         yf = UnionFind(nums)
#         res = 1
#         for num in nums:
#             res = max(res, yf.union(num, num+1))
#         return res


# class UnionFind(object):
#     def __init__(self, nums: List[int]):
#         self.parents = {}
#         for num in nums:
#             self.parents[num] = num
#         self.size = collections.defaultdict(lambda: 1)

#     # 路径压缩：隔代压缩
#     def find(self, x: int) -> int:
#         while x != self.parents[x]:
#             self.parents[x] = self.parents[self.parents[x]]
#             x = self.parents[x]
#         return x

#     # 路径压缩：完全压缩
#     # def find(self, x: int) -> int:
#     #     if x != self.parents[x]:
#     #         self.parents[x] = self.find(self.parents[x])
#     #     return self.parents[x]

#     # O(mα(n))
#     def union(self, x: int, y: int) -> int:
#         if y not in self.parents:
#             return 1

#         rootx = self.find(x)
#         rooty = self.find(y)

#         if rootx == rooty:
#             return self.size[rootx]

#         if self.size[rootx] <= self.size[rooty]:
#             self.parents[rootx] = rooty
#             self.size[rooty] += self.size[rootx]
#             return self.size[rooty]
#         else:
#             self.parents[rooty] = rootx
#             self.size[rootx] += self.size[rooty]
#             return self.size[rootx]


# @lc code=end
