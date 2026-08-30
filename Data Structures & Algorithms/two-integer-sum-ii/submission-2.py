class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # increasing order, has duplicates 
        # return 1-indexed, ie, 0 + 1
        # index1 + index2 = target, index1 < index2
        # only 1 solution 
        #  num = [1,2,2,3,4], target = 4
        # num = [1,2,3,4] target = 3
        l,r = 0, len(numbers) - 1 

        while l < r:
            if numbers[l] + numbers[r] > target: # 5 > 3
                r -= 1 # r = 1
            elif numbers[l] + numbers[r] < target:   
                l += 1
            else:
                if numbers[l] != numbers[r]:
                    return [l+1, r+1]
  
        return []
    