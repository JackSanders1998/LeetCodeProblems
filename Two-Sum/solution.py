class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y:
                    if nums[x] + nums[y] == target:
                        return [x, y]
