class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        found = False
        for i in range(len(nums)):
            if nums[i] == target:
                found = True
                return i
        if not found:
            inserted = False
            for i in range(len(nums)):
                if target < nums[i]:
                    inserted = True
                    return i
            if not inserted:
                return len(nums)
            


