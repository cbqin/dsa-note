import random
import time
from typing import List


class Solution:
    def sort(self, nums: List[int]) -> None:
        self.quickSort1(nums)

    def swap(self, nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]

    def quickSort1(self, nums: List[int]) -> int:
        def partition(nums, left, right):
            pivot = nums[left]
            lt = left
            for i in range(left+1, right+1):
                if nums[i] < pivot:
                    lt += 1
                    self.swap(nums, lt, i)
            self.swap(nums, lt, left)

            return lt

        def quickSort(nums, left, right):
            if left >= right:  # if p==left, p+1>right
                return
            p = partition(nums, left, right)
            quickSort(nums, left, p)
            quickSort(nums, p+1, right)  # if p==left, p+1>right

        n = len(nums)
        if n == 0:
            return
        quickSort(nums, 0, n-1)

    def quickSort2(self, nums: List[int]) -> None:
        def partition(nums, left, right):
            random_index = random.randint(left, right)
            nums[left], nums[random_index] = nums[random_index], nums[left]
            pivot = nums[left]
            lt = left
            for i in range(left+1, right+1):
                if nums[i] < pivot:
                    lt += 1
                    self.swap(nums, lt, i)
            self.swap(nums, lt, left)

            return lt

        def quickSort(nums, left, right):
            if left >= right:  # if p==left, p+1>right
                return
            p = partition(nums, left, right)
            quickSort(nums, left, p-1)
            quickSort(nums, p+1, right)  # if p==left, p+1>right

        n = len(nums)
        if n == 0:
            return
        quickSort(nums, 0, n-1)

    def quickSort3(self, nums: List[int]) -> None:
        # two pointers
        # 把与 pivot 相等的元素平均分配到两侧
        def partition(nums, left, right):
            random_index = random.randint(left, right)
            nums[left], nums[random_index] = nums[random_index], nums[left]
            pivot = nums[left]
            le = left+1
            ge = right
            while True:
                while le <= ge and nums[le] < pivot:
                    le += 1
                while le <= ge and nums[ge] > pivot:
                    ge -= 1
                if le > ge:
                    break
                self.swap(nums, le, ge)
                le += 1
                ge -= 1

            self.swap(nums, left, ge)

            return ge

        def quickSort(nums, left, right):
            if left >= right:  # if p==left, p+1>right
                return
            p = partition(nums, left, right)
            quickSort(nums, left, p-1)
            quickSort(nums, p+1, right)  # if p==left, p+1>right

        n = len(nums)
        if n == 0:
            return
        quickSort(nums, 0, n-1)

    def quickSort4(self, nums: List[int]) -> None:
        # 3-way partitioning
        # 把与 pivot 相等的元素分配到中间
        def partition(nums, left, right):
            random_index = random.randint(left, right)
            nums[left], nums[random_index] = nums[random_index], nums[left]
            pivot = nums[left]
            lt = left
            gt = right+1
            i = left+1
            while i < gt:
                if nums[i] < pivot:
                    lt += 1
                    self.swap(nums, lt, i)
                    i += 1
                elif nums[i] == pivot:
                    i += 1
                else:
                    gt -= 1
                    self.swap(nums, gt, i)
            self.swap(nums, lt, left)

            return lt, gt

        def quickSort(nums, left, right):
            if left >= right:  # if p==left, p+1>right
                return
            lt, gt = partition(nums, left, right)
            quickSort(nums, left, lt-1)
            quickSort(nums, gt, right)  # if p==left, p+1>right

        n = len(nums)
        if n == 0:
            return
        quickSort(nums, 0, n-1)


if __name__ == "__main__":
    s = Solution()
    nums = [1 for i in range(1000)]

    start = time.time()
    s.quickSort2(nums)
    end = time.time()
    print(nums)
    print(end-start)
