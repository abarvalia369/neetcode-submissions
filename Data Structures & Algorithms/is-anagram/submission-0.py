class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for item in list(s):
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

        countt = {}
        for item in list(t):
            if item in countt:
                countt[item] += 1
            else:
                countt[item] = 1
        
        if counts == countt:
            return True
        else:
            return False