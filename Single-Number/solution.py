class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            val = nums.pop(i)
            if val not in nums:
                return val
            else:
                nums.insert(i, val)
