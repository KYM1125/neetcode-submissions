import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        punc = string.punctuation
        for i in punc:
            s = s.replace(i, '')
        s = s.lower()
        s = s.replace(" ", "")
        # print("s = ", s)
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            # if s[left] in punc:
            #     left += 1
            # if s[right] in punc:
            #     right -= 1
            if s[left] != s[right]:
                # print("s[",left,"] = ", s[left])
                # print("s[",right,"] = ", s[right])
                return False
            left += 1
            right -= 1
        return True
        