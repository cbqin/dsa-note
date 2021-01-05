#
# @lc app=leetcode.cn id=1282 lang=python3
#
# [1282] 用户分组
#
# https://leetcode-cn.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
#
# algorithms
# Medium (80.90%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    9.5K
# Total Submissions: 11.8K
# Testcase Example:  '[3,3,3,3,3,1,3]'
#
# 有 n 位用户参加活动，他们的 ID 从 0 到 n - 1，每位用户都 恰好 属于某一用户组。给你一个长度为 n 的数组
# groupSizes，其中包含每位用户所处的用户组的大小，请你返回用户分组情况（存在的用户组以及每个组中用户的 ID）。
#
# 你可以任何顺序返回解决方案，ID 的顺序也不受限制。此外，题目给出的数据保证至少存在一种解决方案。
#
#
#
# 示例 1：
#
# 输入：groupSizes = [3,3,3,3,3,1,3]
# 输出：[[5],[0,1,2],[3,4,6]]
# 解释：
# 其他可能的解决方案有 [[2,1,6],[5],[0,4,3]] 和 [[5],[0,6,2],[4,3,1]]。
#
#
# 示例 2：
#
# 输入：groupSizes = [2,1,3,3,3,2]
# 输出：[[1],[0,5],[2,3,4]]
#
#
#
#
# 提示：
#
#
# groupSizes.length == n
# 1 <= n <= 500
# 1 <= groupSizes[i] <= n
#
#
#

# @lc code=start
from typing import List
from heapq import heapify, heappop
from collections import defaultdict


class Solution:
    # def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    #     h = [(size, i) for i, size in enumerate(groupSizes)]
    #     heapify(h)
    #     cur = []
    #     res = []
    #     while h:
    #         size, i = heappop(h)
    #         cur.append(i)
    #         if len(cur) == size:
    #             res.append(cur)
    #             cur = []
    #     return res

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size_to_user = defaultdict(list)
        for user, gsize in enumerate(groupSizes):
            size_to_user[gsize].append(user)

        ans = []
        for gsize, user in size_to_user.items():
            for it in range(0, len(user), gsize):
                ans.append(user[it:it+gsize])
        return ans

# @lc code=end
