class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 构建有向图
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        state = [0] * numCourses
        def hasCycle(course):
            # 再次遇到了这门课，有环
            if state[course] == 1:
                return True
            # 已经确定了这节课没有环
            if state[course] == 2:
                return False
            # 遇到的课标记为1
            state[course] = 1
            for next_course in graph[course]:
                if hasCycle(next_course):
                    return True
            # 这门课后面也没找到环
            state[course] = 2
            # 始终没找到环
            return False

        for course in range(numCourses):
            if hasCycle(course):
                return False
        return True
        