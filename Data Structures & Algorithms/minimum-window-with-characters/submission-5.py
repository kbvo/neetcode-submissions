class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        tCount = defaultdict(int)
        for c in t:
            tCount[c] += 1
        

        l = 0
        have, need = 0, len(tCount)
        res, resLen = "", float("inf")
        window = defaultdict(int)
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if window[c] == tCount[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        return res



            
