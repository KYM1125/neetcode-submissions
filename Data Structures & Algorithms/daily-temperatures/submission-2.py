class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        # print("init res = ", res)
        for current_day, current_temp in enumerate(temperatures):
            # print("temperatures[stack[-1]] = ", temperatures[stack[-1]])
            while(  
                stack and
                current_temp > temperatures[stack[-1]]
            ):
                previous_day = stack.pop()
                res[previous_day] = current_day - previous_day
                # print("current_day = ", current_day)
                # print("current_temp = ", current_temp)


            stack.append(current_day)
            # print("temperatures[stack[-1]] = ", temperatures[stack[-1]])
            # print("stack = ", stack)
        return res
                


        