#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (37.94%)
# Likes:    211
# Dislikes: 0
# Total Accepted:    49.9K
# Total Submissions: 131.2K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
#
# 示例1:
#
#
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#
#
#
#
# 示例2:
#
#
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#
#
#
#
# 注意：
#
#
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
#
#
#

# @lc code=start


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        left = 0
        right = 0
        distance = 0
        match = 0
        target_dic = {}
        window_dic = {}

        for c in s1:
            if c not in target_dic:
                target_dic[c] = 0
                distance += 1
            target_dic[c] += 1

        while right < n:
            current_right = s2[right]
            if current_right in target_dic:
                if current_right not in window_dic:
                    window_dic[current_right] = 0
                window_dic[current_right] += 1
                if window_dic[current_right] == target_dic[current_right]:
                    match += 1

            right += 1

            while right-left == len(s1):
                if match == distance:
                    return True
                current_left = s2[left]
                if current_left in target_dic:
                    if window_dic[current_left] == target_dic[current_left]:
                        match -= 1
                    window_dic[current_left] -= 1
                left += 1
        return False
# @lc code=end
