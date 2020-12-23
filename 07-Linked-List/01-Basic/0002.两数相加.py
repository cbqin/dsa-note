#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (39.09%)
# Likes:    5414
# Dislikes: 0
# Total Accepted:    658.7K
# Total Submissions: 1.7M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        curr1 = l1
        curr2 = l2
        pre1 = None
        carry = 0
        while curr1 or curr2:
            if not curr1:
                curr1 = ListNode(0)
                pre1.next = curr1
                val = curr2.val + carry
            elif not curr2:
                val = curr1.val + carry
            else:
                val = curr1.val + curr2.val + carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0

            curr1.val = val
            pre1 = curr1

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next

        if carry:
            curr1 = ListNode(0)
            pre1.next = curr1
            curr1.val = carry

        return head

# @lc code=end
