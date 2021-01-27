#
# @lc app=leetcode.cn id=1593 lang=python3
#
# [1593] 拆分字符串使唯一子字符串的数目最大
#
# https://leetcode-cn.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/
#
# algorithms
# Medium (47.41%)
# Likes:    19
# Dislikes: 0
# Total Accepted:    3.6K
# Total Submissions: 7.5K
# Testcase Example:  '"ababccc"'
#
# 给你一个字符串 s ，请你拆分该字符串，并返回拆分后唯一子字符串的最大数目。
#
# 字符串 s 拆分后可以得到若干 非空子字符串 ，这些子字符串连接后应当能够还原为原字符串。但是拆分出来的每个子字符串都必须是 唯一的 。
#
# 注意：子字符串 是字符串中的一个连续字符序列。
#
#
#
# 示例 1：
#
# 输入：s = "ababccc"
# 输出：5
# 解释：一种最大拆分方法为 ['a', 'b', 'ab', 'c', 'cc'] 。像 ['a', 'b', 'a', 'b', 'c', 'cc']
# 这样拆分不满足题目要求，因为其中的 'a' 和 'b' 都出现了不止一次。
#
#
# 示例 2：
#
# 输入：s = "aba"
# 输出：2
# 解释：一种最大拆分方法为 ['a', 'ba'] 。
#
#
# 示例 3：
#
# 输入：s = "aa"
# 输出：1
# 解释：无法进一步拆分字符串。
#
#
#
#
# 提示：
#
#
#
# 1 <= s.length <= 16
#
#
# s 仅包含小写英文字母
#
#
#
#

# @lc code=start


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(s, index, split, seen, length):
            if index >= length:
                self.max_split = max(self.max_split, split)
                return
            for i in range(index, length):
                sub = s[index:i+1]
                if sub in seen:
                    continue
                seen.add(sub)
                dfs(s, i+1, split+1, seen, length)
                seen.remove(sub)
        self.max_split = 1
        seen = set()
        dfs(s, 0, 0, seen, len(s))
        return self.max_split
# @lc code=end
