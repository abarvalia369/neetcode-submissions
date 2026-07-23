class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
            
        for char in t:
            if char in dict:
                dict[char] += -1
            else:
                dict[char] = 1

        for x in dict:
            if dict[x] != 0:
                return False
        return True