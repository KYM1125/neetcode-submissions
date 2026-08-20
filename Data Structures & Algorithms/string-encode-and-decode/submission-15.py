class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        print("encoded_string=",encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decoded_strs = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # print(s[i:j])
            word_length = int(s[i:j]) # #前的部分
            word_start = j + 1 # #后的第一个字符
            word_end = word_start + word_length
            decoded_strs.append(s[word_start:word_end])
            # print("decoded_strs = ", decoded_strs)
            i = word_end
        
        return decoded_strs
