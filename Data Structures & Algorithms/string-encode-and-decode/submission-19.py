class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        print("encoded_string =", encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decoded_string = []
        i = 0
        while True:
            j=i
            if j < len(s):
                while s[j] != "#":
                    j += 1
            # print("i=",i,"j=",j)
            
            word_length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + word_length
            decoded_string.append(s[word_start:word_end])
            i = word_end
            if i==len(s):
                break
        return decoded_string
        
