class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = []
        index = 0
        for i in range(len(nums)):
            if nums[index] in visited:
                nums.pop(index)
            else:
                visited.append(nums[index])
                index += 1
        return len(nums)
