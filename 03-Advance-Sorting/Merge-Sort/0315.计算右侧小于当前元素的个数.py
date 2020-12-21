#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#
# https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (41.87%)
# Likes:    503
# Dislikes: 0
# Total Accepted:    38.8K
# Total Submissions: 92.6K
# Testcase Example:  '[5,2,6,1]'
#
# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
# nums[i] 的元素的数量。
#
#
#
# 示例：
#
# 输入：nums = [5,2,6,1]
# 输出：[2,1,1,0]
# 解释：
# 5 的右侧有 2 个更小的元素 (2 和 1)
# 2 的右侧仅有 1 个更小的元素 (1)
# 6 的右侧有 1 个更小的元素 (1)
# 1 的右侧有 0 个更小的元素
#
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc code=start


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [0]
        temp = [0]*n
        res = [0]*n
        index = [i for i in range(n)]

        self.mergeSort(nums, 0, n-1, temp, index, res)

        return res

    def mergeSort(self, nums: List[int], left: int, right: int, temp: List[int], index: List[int], res: List[int]) -> None:
        if left == right:
            return
        mid = left+(right-left)//2
        self.mergeSort(nums, left, mid, temp, index, res)
        self.mergeSort(nums, mid+1, right, temp, index, res)
        if nums[index[mid]] <= nums[index[mid+1]]:
            return
        self.merge(nums, left, mid, right, temp, index, res)

    def merge(self, nums: List[int], left: int, mid: int, right: int, temp: List[int], index: List[int], res: List[int]) -> None:
        temp[left:right+1] = index[left:right+1]

        i = left
        j = mid+1
        for k in range(left, right+1):
            if i > mid:
                index[k] = temp[j]
                j += 1
            elif j > right:
                index[k] = temp[i]
                i += 1
                res[index[k]] += (right-mid)
            elif nums[temp[i]] <= nums[temp[j]]:
                index[k] = temp[i]
                i += 1
                res[index[k]] += (j-mid-1)
            else:
                index[k] = temp[j]
                j += 1
# @lc code=end
