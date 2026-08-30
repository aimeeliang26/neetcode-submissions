class Solution:

    def encode(self, strs: List[str]) -> str:

        # add a 1 at the beginning 
        # if space, add #
        # have the number, and get 
        # ["a and b"]

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        # ["1#a3#and1#b"]

    def decode(self, str) -> List[str]:
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res