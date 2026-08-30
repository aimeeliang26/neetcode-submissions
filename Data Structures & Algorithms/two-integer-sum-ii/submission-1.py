class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #non-decreasing order --- negative number? cannot use same ele twice 
        #1-indexed means? return the index + 1
        #odd, even
        # numbers[l] + numbers[r] = target, numbers[l] < numbers[r]

        # [1,2,3,4]
        # [1,2]

        # [0,2,2,8,9] target is 10
        # [1,3] or [2,3] (one of them is fine)

        # res = []
        res = []
        # l = 0, r = len(numbers) -1
        l, r = 0, len(numbers) - 1
        while l < r:
        #     if numbers[l] + numbers[r] > target \\\ 1
            if numbers[l] + numbers[r] > target:
                r -= 1
        #         r --
        #     if numbers[l] + numbers[r] < target 
            elif numbers[l] + numbers[r] < target:
                l += 1
        #         l ++
            elif numbers[l] + numbers[r] == target:
                res.append(l + 1)
                res.append(r + 1)
                # return [l +1 , r + 1]
                return res

        #     else (when they equal); res.add(l,r) return res
        return res
