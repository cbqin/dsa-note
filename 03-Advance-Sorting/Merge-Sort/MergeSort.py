from typing import List


class Solution:
    def sort(self, nums: List[int])->List[int]:
        n = len(nums)
        if n == 0:
            return nums
        temp = [0]*n
        self.mergeSort(nums, 0, n-1, temp)
        return nums

    def mergeSort(self, nums: List[int], left: int, right: int, temp: List[int])->None:
        if left == right:
            return
        mid = left+(right-left)//2
        self.mergeSort(nums, left, mid, temp)
        self.mergeSort(nums, mid+1, right, temp)
        if nums[mid] <= nums[mid+1]:
            return
        self.mergeOfTwoSortedArray(nums, left, mid, right, temp)

    def mergeOfTwoSortedArray(self, nums: List[int], left: int, mid: int, right: int, temp: List[int])->None:
        temp[left:right+1] = nums[left:right+1]

        i = left
        j = mid+1
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


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    s = Solution()
    nums = s.sort(nums)
    print(nums)
