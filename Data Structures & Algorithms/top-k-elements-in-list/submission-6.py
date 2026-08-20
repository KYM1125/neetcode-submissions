class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        # 统计每个数字的出现频率
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # 桶的下标表示频率
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)

        results = []

        # 从最高频率向最低频率遍历
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                results.append(num)

                if len(results) == k:
                    return results

        return results