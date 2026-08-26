class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        for current in intervals[1:]:
            if result[-1][1] >= current[0]:
                result[-1][1] = max(result[-1][1], current[1])
            else:
                result.append(current)
        return result

        