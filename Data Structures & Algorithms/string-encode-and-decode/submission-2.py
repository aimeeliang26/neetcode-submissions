class Solution:

    def encode(self, strs: List[str]) -> str:

        # add a 1 at the beginning 
        # if space, add #
        # have the number, and get 
        # ["a and b"]
        
        res = ""
        for ele in strs:
            # a 
            # and 
            # b 
            res += (str(len(ele)) + "#" + ele)
            #[1#a3#and1#b]
        return res

    def decode(self, s : str) -> List[str]:
        toDecode, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            toDecode.append(s[j+1 :j + length + 1])
            i = j + 1 + length
        return toDecode
