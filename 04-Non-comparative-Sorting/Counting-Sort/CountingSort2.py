import copy
from typing import List


class CountingSort:
    def countingSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums
        max_value = 0
        for num in nums:
            assert num >= 0
            if num >= max_value:
                max_value = num

        count = [0]*(max_value+1)
        for num in nums:
            count[num] += 1

        for i in range(1, max_value+1):
            count[i] += count[i-1]

        nums_copy = copy.deepcopy(nums)

        for i in range(n-1, -1, -1):
            position = count[nums_copy[i]]-1
            nums[position] = nums_copy[i]
            count[nums_copy[i]] -= 1

        return nums


if __name__ == "__main__":
    nums = [2, 5, 3, 0, 2, 3, 0, 3]
    cs = CountingSort()
    nums = cs.countingSort(nums)
    print(nums)
