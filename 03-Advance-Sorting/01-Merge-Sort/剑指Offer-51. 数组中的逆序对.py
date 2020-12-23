# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

#  

# 示例 1:

# 输入: [7,5,6,4]
# 输出: 5
#  

# 限制：

# 0 <= 数组长度 <= 50000

import copy
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        nums2 = copy.deepcopy(nums)
        temp = [0]*n

        return self.mergeSort(nums2, 0, n-1, temp)

    def mergeSort(self, nums: List[int], left: int, right: int, temp: List[int]) -> int:
        if left == right:
            return 0
        mid = left+(right-left)//2
        leftPairs = self.mergeSort(nums, left, mid, temp)
        rightPairs = self.mergeSort(nums, mid+1, right, temp)
        crossPairs = self.mergeAndCount(nums, left, mid, right, temp)

        return leftPairs+rightPairs+crossPairs

    def mergeAndCount(self, nums: List[int], left: int, mid: int, right: int, temp: List[int]) -> int:
        temp[left:right+1] = nums[left:right+1]
        i = left
        j = mid+1
        count = 0
        for k in range(left, right+1):
            if i == mid+1:
                nums[k:right+1] = temp[j:right+1]
                break
            elif j == right+1:
                nums[k:right+1] = temp[i:mid+1]
                break
            elif temp[i] <= temp[j]:
                nums[k] = temp[i]
                i += 1
            else:
                nums[k] = temp[j]
                j += 1
                count += (mid-i+1)
        return count


if __name__ == "__main__":
    s = Solution()
    nums = [5, 4, 3, 2, 1]
    count = s.reversePairs(nums)
    print(count)
