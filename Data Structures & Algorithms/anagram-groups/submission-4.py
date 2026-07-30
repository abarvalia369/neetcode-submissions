from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}

        for x in strs:
            ary = [0] * 26 
            for l in x:
                ary[ord(l) - ord('a')] += 1

            if tuple(ary) not in data:#need to tuple ary because lists cant be hashed
                data[tuple(ary)] = [x]#hashable = never changes and can be compared
            else:
                data[tuple(ary)].append(x)#tuple can cause its immutable = cant be changed after creation 
     
        return list(data.values())#values() gives j dict values, list puts them in a list