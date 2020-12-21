#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (47.87%)
# Likes:    433
# Dislikes: 0
# Total Accepted:    47.9K
# Total Submissions: 99.6K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
# 说明：
#
#
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
#
#
# 示例 1:
#
#
# 输入:
# s: "cbaebabacd" p: "abc"
#
# 输出:
# [0, 6]
#
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#
#
# 示例 2:
#
#
# 输入:
# s: "abab" p: "ab"
#
# 输出:
# [0, 1, 2]
#
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#
#
#

# @lc code=start


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        left = 0
        right = 0
        distance = 0
        res = []
        p_dic = {}
        w_dic = {}
        match = 0

        for c in p:
            if c not in p_dic:
                p_dic[c] = 0
                distance += 1
            p_dic[c] += 1

        while right < n:
            current_right = s[right]
            if current_right in p_dic:
                if current_right not in w_dic:
                    w_dic[current_right] = 0
                w_dic[current_right] += 1
                if w_dic[current_right] == p_dic[current_right]:
                    match += 1

            right += 1

            while right-left == len(p):
                if match == distance:
                    res.append(left)
                current_left = s[left]
                if current_left in p_dic:
                    if w_dic[current_left] == p_dic[current_left]:
                        match -= 1
                    w_dic[current_left] -= 1
                left += 1
        return res

# @lc code=end
