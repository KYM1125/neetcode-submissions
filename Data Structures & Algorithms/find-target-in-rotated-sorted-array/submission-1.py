class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
                break
            if nums[left] <= nums[mid]: #左半部分有序
                if nums[left] <= target < nums[mid]:
                    # target位于有序的左半部分
                    right = mid - 1
                else:
                    # target在左半部分找不到
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        