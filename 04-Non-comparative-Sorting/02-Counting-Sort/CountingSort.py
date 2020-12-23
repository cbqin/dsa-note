from typing import List


class CountingSort:
    def countingSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return nums
        max_value = 0
        for num in nums:
            assert num >= 0
            if num >= max_value:
                max_value = num
        count = [0]*(max_value+1)

        for num in nums:
            count[num] += 1

        index = 0
        for i, c in enumerate(count):
            for j in range(c):
                nums[index+j] = i
            index += c
        return nums


if __name__ == "__main__":
    nums = [2, 5, 3, 0, 2, 3, 0, 3]
    cs = CountingSort()
    nums = cs.countingSort(nums)
    print(nums)
