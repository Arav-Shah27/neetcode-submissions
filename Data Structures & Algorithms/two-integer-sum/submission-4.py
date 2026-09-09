class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        var = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in var:
                return [var[diff], i]
            var[n] = i
        return