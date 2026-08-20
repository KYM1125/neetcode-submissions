class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        buckets = [[] for _ in range(len(nums) + 1)]
        freq_map = {}
        results = []

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        for num, freq in freq_map.items():
            buckets[freq].append(num)

        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                results.append(num)
                if len(results) == k:
                    return results
        return results
        