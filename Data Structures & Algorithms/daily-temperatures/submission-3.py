class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for current_day, current_temp in enumerate(temperatures):
            while(
                stack and
                current_temp > temperatures[stack[-1]]
            ):
                previous_day =  stack.pop()
                res[previous_day] = current_day - previous_day
            stack.append(current_day)
        return res
                


        