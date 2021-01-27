#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (79.32%)
# Likes:    957
# Dislikes: 0
# Total Accepted:    188.3K
# Total Submissions: 236.9K
# Testcase Example:  '[1,2,3]'
#
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
# 提示：
#
#
# 1
# -10
# nums 中的所有元素 互不相同
#
#
#

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, begin, path, res):
            res.append(path[:])
            for i in range(begin, len(nums)):
                path.append(nums[i])
                dfs(nums, i+1, path, res)
                path.pop()
        res = []
        dfs(nums, 0, [], res)
        return res
# @lc code=end
