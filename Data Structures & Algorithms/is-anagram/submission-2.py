class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        dict = {}

        for x in s:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        
        for x in t:
            if x in dict:
                dict[x] += -1
            else:
                dict[x] = 1
        ret = True
        for x in dict:
            if dict[x] != 0:
                ret = False
        
        return ret