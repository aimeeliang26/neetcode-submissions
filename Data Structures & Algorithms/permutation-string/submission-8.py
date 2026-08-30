class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Go through s1, s2 to formulate their array of [0] * 26 where each point is ord[c] - ord['a'], and we calculate the number of matches by checking whether s1C[i] == s2C[i]

        # loop thru r, where r is from len(s1) to len(s2) - 1
        # check if match == 26, if yes return true else :
        # l, r; l is 0, r is len(s1) in s2
        # s2C take away an element, 
        # check if s1C[index] + 1 = s2C[index]
        # match -= 1 

        # s2C add an element
        # check if s1C[index] - 1 = s2C[index]
        # match += 1

        # then to increment l += 1
        
        # s1 = abc
        # s2 = lecabee
        if len(s1) > len(s2):
            return False
    
        s1C, s2C = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1C[ord(s1[i]) - ord("a")] += 1
            s2C[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if (s1C[i] == s2C[i]):
                matches += 1

        # for i in range(26):
        #     matches += (1 if s1C[i] == s2C[i] else 0)     
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True 
            index = ord(s2[r]) - ord('a')
            s2C[index] += 1
            if s1C[index] == s2C[index]:
                matches += 1
            elif s1C[index] + 1 == s2C[index]:
                matches -= 1

            indexL = ord(s2[l]) - ord('a')
            s2C[indexL] -= 1
            if s1C[indexL] == s2C[indexL]:
                matches += 1
            elif s1C[indexL] - 1 == s2C[indexL]:
                matches -= 1
            l += 1

        return matches == 26

        # l = 0
        # for r in range(len(s1), len(s2)):
        #     # the turning point
        #     if matches == 26:
        #         return True
            
        #     index = ord(s2[r]) - ord('a')
        #     s2C[index] += 1
        #     if s1C[index] == s2C[index]:
        #         matches += 1
        #     elif s1C[index] + 1 == s2C[index]:
        #         matches -= 1
            
        #     index = ord(s2[l]) - ord('a')
        #     s2C[index] -= 1
        #     if s1C[index] == s2C[index]:
        #         matches += 1
        #     elif s1C[index] -1 == s2C[index]:
        #         matches -= 1
        #     l += 1
        
        # return matches == 26
     

        