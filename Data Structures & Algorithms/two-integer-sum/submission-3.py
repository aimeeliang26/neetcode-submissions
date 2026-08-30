class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums =[ 1,2,3,2,5], target = 4

        # i, j 

        # sort(nums), in ascending order 
        # # [1,2,2,3,5]
        # # i        j 
        # [3,2,3]
        # [2,3,3]

        res = []
        # 0,1,2. 1,2,2,3,5
        for i, num in enumerate(nums):
            res.append([num,i]) #res = [[1,0], [2,1], [2,2], [3,3],[5,4]]
        
        # sRes = sorted(res)
        res.sort()

        i,j = 0, len(nums) - 1
        while i < j:
            cur = res[i][0] + res[j][0]
            if cur > target:
                j -= 1
            elif cur < target:
                i += 1
            else: 
                return [min(res[i][1],res[j][1]), max(res[i][1], res[j][1])]

        return []


