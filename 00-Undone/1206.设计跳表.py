#
# @lc app=leetcode.cn id=1206 lang=python3
#
# [1206] 设计跳表
#
# https://leetcode-cn.com/problems/design-skiplist/description/
#
# algorithms
# Hard (60.73%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 5.7K
# Testcase Example:  '["Skiplist","add","add","add","search","add","search","erase","erase","search"]\r\n[[],[1],[2],[3],[0],[4],[1],[0],[1],[1]]\r'
#
# 不使用任何库函数，设计一个跳表。
#
# 跳表是在 O(log(n))
# 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想与链表相似。
#
# 例如，一个跳表包含 [30, 40, 50, 60, 70, 90]，然后增加 80、45 到跳表中，以下图的方式操作：
#
#
# Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons
#
# 跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。跳表的每一个操作的平均时间复杂度是
# O(log(n))，空间复杂度是 O(n)。
#
# 在本题中，你的设计应该要包含这些函数：
#
#
# bool search(int target) : 返回target是否存在于跳表中。
# void add(int num): 插入一个元素到跳表。
# bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num
# ，删除其中任意一个即可。
#
#
# 了解更多 : https://en.wikipedia.org/wiki/Skip_list
#
# 注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。
#
# 样例:
#
# Skiplist skiplist = new Skiplist();
#
# skiplist.add(1);
# skiplist.add(2);
# skiplist.add(3);
# skiplist.search(0);   // 返回 false
# skiplist.add(4);
# skiplist.search(1);   // 返回 true
# skiplist.erase(0);    // 返回 false，0 不在跳表中
# skiplist.erase(1);    // 返回 true
# skiplist.search(1);   // 返回 false，1 已被擦除
#
#
# 约束条件:
#
#
# 0 <= num, target <= 20000
# 最多调用 50000 次 search, add, 以及 erase操作。
#
#
#

# @lc code=start


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.forwards = []


class Skiplist:

    MAX_LEVEL = 4

    def __init__(self):
        self.level_count = 1
        self.head = ListNode()
        self.head.forwards = [None]*self.MAX_LEVEL

    def _random_level(self, p=0.5):
        level = 1
        while random.random() < p and level < self.MAX_LEVEL:
            level += 1
        return level

    def search(self, target: int) -> bool:
        p = self.head
        for i in range(self.level_count-1, -1, -1):
            if p.forwards[i] and p.forwards[i].key < target:
                p = p.forwards[i]
            if p.forwards[i] and p.forwards[i].key == target:
                return True
        return False

    def add(self, num: int) -> None:
        level = self._random_level()
        if self.level_count < level:
            self.level_count = level
        new_node = ListNode(key=num)
        new_node.forwards = [None]*level
        prevs = [self.head]*level

        p = self.head
        for i in range(level-1, -1, -1):
            while p.forwards[i] and p.forwards[i].key < num:
                p = p.forwards[i]
            # if p.forwards[i] and p.forwards[i].key == num:
            #     return
            prevs[i] = p

        for i in range(level):
            new_node.forwards[i] = prevs[i].forwards[i]
            prevs[i].forwards[i] = new_node

    def erase(self, num: int) -> bool:
        prevs = [None]*self.level_count
        p = self.head
        for i in range(self.level_count-1, -1, -1):
            while p.forwards[i] and p.forwards[i].key < num:
                p = p.forwards[i]
            prevs[i] = p

        if p.forwards[0] and p.forwards[0].key == num:
            for i in range(self.level_count-1, -1, -1):
                if prevs[i].forwards[i] and prevs[i].forwards[i].key == num:
                    prevs[i].forwards[i] = prevs[i].forwards[i].forwards[i]
            while self.level_count > 1 and (not self.head.forwards[self.level_count-1]):
                self.level_count -= 1
            return True
        else:
            return False


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end
