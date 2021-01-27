#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (62.32%)
# Likes:    563
# Dislikes: 0
# Total Accepted:    132.4K
# Total Submissions: 211.7K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
#
# 提示：
#
#
# 1
# -10
#
#
#

# @lc code=start


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, index, used, path, length, res):
            if index == length:
                res.append(path[:])
                return

            for i in range(length):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(nums, index+1, used, path, length, res)
                path.pop()
                used[i] = False

        res = []
        nums.sort()
        length = len(nums)
        used = [False]*length
        path = []
        index = 0
        dfs(nums, index, used, path, length, res)
        return res
# @lc code=end
