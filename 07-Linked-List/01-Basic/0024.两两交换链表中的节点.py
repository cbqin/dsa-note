#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (68.66%)
# Likes:    764
# Dislikes: 0
# Total Accepted:    205.2K
# Total Submissions: 298.4K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
#
#
# 示例 2：
#
#
# 输入：head = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：head = [1]
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 100] 内
# 0
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
    # def swapPairs(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return head

    #     dummy_node = ListNode(-1)
    #     dummy_node.next = head
    #     pre_node = dummy_node
    #     curr_node = head

    #     while curr_node and curr_node.next:
    #         next_node = curr_node.next
    #         next_next_node = next_node.next

    #         curr_node.next = next_next_node
    #         next_node.next = curr_node
    #         pre_node.next = next_node
    #         pre_node = curr_node
    #         curr_node = next_next_node

    #     return dummy_node.next

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        next_node = head.next
        node = self.swapPairs(next_node.next)
        head.next = node
        next_node.next = head

        return next_node

# @lc code=end
