class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        for n in range(len(nums) - 1, -1, -1):
            output[n] *= postfix
            postfix *= nums[n]
        return output