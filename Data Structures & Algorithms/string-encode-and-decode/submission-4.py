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

        #learning: know clear what each variable mean, what you are traversing in, eg s[i], for i in s, or while i < len (s); str is +=; you can convert str or int by simply int() or str()
        #time complexity: O(m+n) for each encode and decode function calls, where m is the number of elements in all strings, n is the number of strings, 
        # encode: go trhough every element in a string, and add # and an integer to each string, time complexity is O(m + 2n) where m is total strings character
        # space complexity: append every character as well as the # and integer 
        # decode: go through every character in all strings, m, prefix the length per string, so n is the number of strings
        # time complexity : O(m+n)
        # space: O(m+n) you need a pointer for each string, and theres n string, you also need to store m characters in all the strings, hence m + n

