class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = sorted(nums)
        result = 0
        count = 1
        for n in range(1, len(new), 1):
            if(new[n] == new[n-1]):
                continue
            if (new[n] - new[n-1]) == 1:
                count += 1
            else:
                if(count > result):
                    result = count
                count = 1
        if count > result and len(nums) > 0:
            result = count
        return result


# nums = [1,2,3,5,5,6,9]
# nums = [0,2,4,5,6,7]
# count = 2
# result = 3