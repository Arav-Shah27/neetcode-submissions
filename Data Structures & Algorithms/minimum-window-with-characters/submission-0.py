class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        subt = {}
        subs = {}
        res, resLen = [-1, -1], float("infinity")

        for c in t:
            subt[c] = 1 + subt.get(c, 0)

        have, need = 0, len(subt)
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            subs[c] = 1 + subs.get(c, 0)
            if c in subt and subs[c] == subt[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                subs[s[l]] -= 1
                if s[l] in subt and subs[s[l]] < subt[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if resLen != float("infinity"):
            return s[l:r+1] 
        else:
            return ""