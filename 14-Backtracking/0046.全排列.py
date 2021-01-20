#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (77.27%)
# Likes:    1085
# Dislikes: 0
# Total Accepted:    243.6K
# Total Submissions: 314.6K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#

# @lc code=start

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, index, used, path, length, res):
            if index == length:
                res.append(path[:])
                return

            for i in range(length):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(nums, index+1, used, path, length, res)
                path.pop()
                used[i] = False

        res = []
        length = len(nums)
        used = [False]*length
        path = []
        index = 0
        dfs(nums, index, used, path, length, res)
        return res
# @lc code=end
