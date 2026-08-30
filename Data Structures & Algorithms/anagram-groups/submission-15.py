class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # i am given a list of strings, i need to group strings that are anagrams together. 
        # anagrams are strings that have the same letters, order does not matter. 

        # a,1
        # c,1
        # t,1

        # p,1
        # o,1
        # t,1
        # s,1

        # t,1
        # o,1
        # p,1
        # s,1

        output = defaultdict(list)

        for string in strs: #act
            storeArray = [0] * 26 #storeArray = [0,0,0]
            for letter in string: # a
                storeArray[ord(letter) - ord("a")] += 1 #[1,0,0]
            
            output[tuple(storeArray)].append(string)

        return list(output.values())


        
