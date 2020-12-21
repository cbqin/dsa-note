#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#
# https://leetcode-cn.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (65.93%)
# Likes:    194
# Dislikes: 0
# Total Accepted:    34.7K
# Total Submissions: 52.5K
# Testcase Example:  '"tree"'
#
# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
#
# 示例 1:
#
#
# 输入:
# "tree"
#
# 输出:
# "eert"
#
# 解释:
# 'e'出现两次，'r'和't'都只出现一次。
# 因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
#
#
# 示例 2:
#
#
# 输入:
# "cccaaa"
#
# 输出:
# "cccaaa"
#
# 解释:
# 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
# 注意"cacaca"是不正确的，因为相同的字母必须放在一起。
#
#
# 示例 3:
#
#
# 输入:
# "Aabb"
#
# 输出:
# "bbAa"
#
# 解释:
# 此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
# 注意'A'和'a'被认为是两种不同的字符。
#
#
#

# @lc code=start


class Solution:
    def swap(self, nums: List[str], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]

    def frequencySort(self, s: str) -> str:
        arr = list(s)
        self.freq = [0]*128
        for c in arr:
            self.freq[ord(c)] += 1
        self.quickSort(arr, 0, len(arr)-1)
        return "".join(arr)

    def quickSort(self, nums, left, right):
        if left >= right:  # if p==left, p+1>right
            return
        random_index = random.randint(left, right)
        nums[left], nums[random_index] = nums[random_index], nums[left]
        pivot = nums[left]
        lt = left
        gt = right+1

        i = left+1
        while i < gt:
            if self.freq[ord(nums[i])] > self.freq[ord(pivot)]:
                lt += 1
                self.swap(nums, lt, i)
                i += 1
            elif nums[i] == pivot:
                i += 1
            else:
                gt -= 1
                self.swap(nums, gt, i)
        self.swap(nums, lt, left)

        self.quickSort(nums, left, lt-1)
        self.quickSort(nums, gt, right)  # if p==left, p+1>right


# @lc code=end
