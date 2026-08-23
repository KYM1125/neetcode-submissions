class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            com = target - num
            if com in seen:
                return [seen[com]+1, i+1]
            seen[num] = i
        return []

        