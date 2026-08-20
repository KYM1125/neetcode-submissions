class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        results = []
        # sorted_strs = {}
        str_map = {}
        # list_map = {}

        for string in strs:
            key = tuple(sorted(string))
            str_map.setdefault(key,[]).append(string)
            # print(key)
        # print(str_map)
        for value in str_map.values():
            results.append(value)
        return results

        


        