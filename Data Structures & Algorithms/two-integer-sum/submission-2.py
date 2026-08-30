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
        
        sRes = sorted(res)

        i,j = 0, len(nums) - 1
        while i < j:
            cur = sRes[i][0] + sRes[j][0]
            if cur > target:
                j -= 1
            elif cur < target:
                i += 1
            else: 
                return [min(sRes[i][1],sRes[j][1]), max(sRes[i][1], sRes[j][1])]

        return []


