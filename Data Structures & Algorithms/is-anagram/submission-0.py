class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        else:
            counts = {}
            countt = {}
            for i in range(len(t)):
                counts[s[i]] = 1 + counts.get(s[i], 0)
                countt[t[i]] = 1 + countt.get(t[i], 0)
            
            if counts == countt:
                return True
            else:
                return False