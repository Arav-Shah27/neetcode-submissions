class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 1
        sub = set()
        l, r = 0, 0
        if(len(s) == 0):
            return 0
        while r < len(s):
            if(s[r] in sub):
                sub.remove(s[l])
                l += 1
            else:
                sub.add(s[r])
                r += 1
            output = max(output, len(sub))
        return output
            
