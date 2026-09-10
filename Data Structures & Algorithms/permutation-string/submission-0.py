class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub1 = {}
        sub2 = {}
        for c in s1:
            sub1[c] = 1 + sub1.get(c, 0)
        l = 0
        for r in range(len(s2)):
            sub2[s2[r]] = 1 + sub2.get(s2[r], 0)
            if((r - l + 1) > len(s1)):
                sub2[s2[l]] -= 1
                if sub2[s2[l]] == 0:
                    del sub2[s2[l]]
                l += 1
            if (sub1 == sub2):
                return True
        return False
            


            