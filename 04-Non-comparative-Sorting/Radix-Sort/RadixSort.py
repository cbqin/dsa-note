import copy
from typing import List


class RadixSort:
    def radixSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums

        max_value = 0
        for num in nums:
            assert num >= 0
            if num >= max_value:
                max_value = num

        max_len = self.getMaxLen(max_value)

        divisor = 1
        for _ in range(max_len):
            self.countingSort(nums, divisor)
            divisor *= 10

        return nums

    def getMaxLen(self, num: int) -> int:
        max_len = 0
        while num > 0:
            num //= 10
            max_len += 1
        return max_len

    def countingSort(self, nums: List[int], divisor: int) -> List[int]:
        count = [0]*10
        nums_copy = copy.deepcopy(nums)

        for num in nums:
            remainder = (num//divisor) % 10
            count[remainder] += 1

        for i in range(1, 10):
            count[i] += count[i-1]

        for i in range(len(nums_copy)-1, -1, -1):
            remainder = (nums_copy[i]//divisor) % 10
            position = count[remainder]-1
            nums[position] = nums_copy[i]
            count[remainder] -= 1


if __name__ == "__main__":
    nums = [111, 2222, 999, 888, 777]
    rs = RadixSort()
    nums = rs.radixSort(nums)
    print(nums)
