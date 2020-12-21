#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#
# https://leetcode-cn.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (49.07%)
# Likes:    205
# Dislikes: 0
# Total Accepted:    14.7K
# Total Submissions: 29.8K
# Testcase Example:  '"ABAB"\n2'
#
# 给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k
# 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
#
# 注意:
# 字符串长度 和 k 不会超过 10^4。
#
# 示例 1:
#
# 输入:
# s = "ABAB", k = 2
#
# 输出:
# 4
#
# 解释:
# 用两个'A'替换为两个'B',反之亦然。
#
#
# 示例 2:
#
# 输入:
# s = "AABABBA", k = 1
#
# 输出:
# 4
#
# 解释:
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
#
#
#

# @lc code=start


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n < 2:
            return n
        res = 1
        left = 0
        right = 0
        max_count = 0

        window_dic = {}
        while right < n:
            current_right = s[right]
            if current_right not in window_dic:
                window_dic[current_right] = 0
            window_dic[current_right] += 1

            max_count = max(max_count, window_dic[current_right])

            right += 1

            while right-left > max_count+k:
                current_left = s[left]
                window_dic[current_left] -= 1
                left += 1

            res = max(res, right-left)
        return res

# @lc code=end
