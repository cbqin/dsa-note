#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (39.90%)
# Likes:    870
# Dislikes: 0
# Total Accepted:    95.6K
# Total Submissions: 238.9K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
# 示例 1：
#
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#
#
# 示例 2：
#
#
# 输入：s = "a", t = "a"
# 输出："a"
#
#
#
#
# 提示：
#
#
# 1
# s 和 t 由英文字母组成
#
#
#
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
#

# @lc code=start


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        left = 0
        right = 0
        start = 0
        match = 0
        distance = 0
        min_len = n+1

        window_dic = {}
        t_dic = {}
        for c in t:
            if c not in t_dic:
                t_dic[c] = 0
                distance += 1
            t_dic[c] += 1

        while right < n:
            current_c = s[right]
            if current_c in t_dic:
                if current_c not in window_dic:
                    window_dic[current_c] = 0
                window_dic[current_c] += 1
                if window_dic[current_c] == t_dic[current_c]:
                    match += 1

            right += 1

            while match == distance:
                if right-left < min_len:
                    start = left
                    min_len = right-left

                current_c_left = s[left]
                if current_c_left in t_dic:
                    window_dic[current_c_left] -= 1
                    if window_dic[current_c_left] < t_dic[current_c_left]:
                        match -= 1
                left += 1

        return "" if min_len == n+1 else s[start:start+min_len]


# @lc code=end
