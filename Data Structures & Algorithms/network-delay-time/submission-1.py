import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for ui,vi,ti in times:
            graph[ui].append((vi,ti))
        
        # 最短距离数组
        distances = [float("inf")] * (n+1)
        distances[k] = 0
        # 最小堆
        min_heap = [(0,k)]
        while min_heap:
            current_distance,node = heapq.heappop(min_heap)
            if current_distance > distances[node]:
                continue
            for neighbor, weight in graph[node]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(min_heap, (new_distance,neighbor))
        answer = max(distances[1:])
        if answer == float("inf"):
            return -1
        return answer
            
        