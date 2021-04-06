class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        remainder = abs(goal - sum(nums))
        count = (remainder // limit)
        if (remainder % limit) != 0:
            count += 1
        return count
