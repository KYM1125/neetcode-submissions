import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [num for num in nums if num > pivot]
        mid = [num for num in nums if num == pivot]
        right = [num for num in nums if num < pivot]
        if k <= len(left):
            return self.findKthLargest(left, k)
        elif k <= len(left) + len(mid):
            return pivot
        else:
            return self.findKthLargest(right, k-len(left)-len(mid))
        