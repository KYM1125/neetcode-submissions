class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        # print("buckets = ", buckets)
        freq_map = {}
        results = []
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
            # print("freq_map = ", freq_map)
        for num in freq_map:
            buckets[freq_map[num]].append(num)
        # print("buckets = ", buckets)
        # print("len(buckets) = ", len(buckets))
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                # print("num = ", num)
                results.append(num)
                if len(results) == k:
                    return results
        return results
