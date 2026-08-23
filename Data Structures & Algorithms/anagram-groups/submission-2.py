class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        str_map = {}
        res = []
        for string in strs:
            key = tuple(sorted(string))
            # print("key=", key)
            str_map.setdefault(key,[]).append(string)
            # print("str_map = ", str_map)
        for val in str_map.values():
            res.append(val)
        return res

        


        