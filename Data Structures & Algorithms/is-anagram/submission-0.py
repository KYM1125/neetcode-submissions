class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        buckets_s = {}
        buckets_t = {}

        for char in s:
            buckets_s[char] = buckets_s.get(char, 0) + 1
        for char in t:
            buckets_t[char] = buckets_t.get(char, 0) + 1

        return buckets_s == buckets_t

        