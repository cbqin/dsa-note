#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (46.66%)
# Likes:    502
# Dislikes: 0
# Total Accepted:    120.5K
# Total Submissions: 258.1K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
#
# 示例:
#
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        curr_node = dummy_node.next
        pre_node = dummy_node
        while curr_node:
            next_node = curr_node.next
            if curr_node.val == val:
                pre_node.next = next_node
                curr_node.next = None
                del curr_node
            else:
                pre_node = curr_node
            curr_node = next_node
        return dummy_node.next


# @lc code=end
