#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (49.82%)
# Likes:    414
# Dislikes: 0
# Total Accepted:    78.2K
# Total Submissions: 156.7K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#
#
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        pre = dummy
        current = head
        while current:
            nex = current.next
            last = None
            while nex and nex.val == current.val:
                last = nex
                nex = nex.next
            if last:
                pre.next = nex
                last.next = None
            else:
                pre = current

            current = nex

        return dummy.next

# @lc code=end
