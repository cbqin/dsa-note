#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (71.11%)
# Likes:    1409
# Dislikes: 0
# Total Accepted:    395.8K
# Total Submissions: 556.1K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     pre_node = None
    #     curr_node = head
    #     while curr_node:
    #         next_node = curr_node.next
    #         curr_node.next = pre_node
    #         pre_node = curr_node
    #         curr_node = next_node
    #     return pre_node

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        next_node = head.next
        new_node = self.reverseList(next_node)
        next_node.next = head
        head.next = None

        return new_node
# @lc code=end
