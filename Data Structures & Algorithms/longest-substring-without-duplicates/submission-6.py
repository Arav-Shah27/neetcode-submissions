class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        sub = set()
        l = 0
        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            output = max(output, len(sub))
        return output    
