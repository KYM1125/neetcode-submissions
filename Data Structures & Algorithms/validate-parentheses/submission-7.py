class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        matching = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []
        for char in s:
            if char in matching:
                stack.append(char)
            if char in matching.values():
                if len(stack) == 0:
                    return False
                pop = matching[stack.pop()]
                if char != pop:
                    return False
        if len(stack) != 0:
            return False
        return True


        