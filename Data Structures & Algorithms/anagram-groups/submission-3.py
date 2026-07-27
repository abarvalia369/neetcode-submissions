class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ret = {}#{char ctr:list of anagrams}

        for x in strs:
            ctr = [0]*26
            for c in x:
                ctr[ord(c) - ord('a')] += 1

            key = tuple(ctr)#dict keys must be hasable and lists arent
            if key not in ret:
                ret[key] = []#empty list
            ret[key].append(x)#add to the empty list
            
        return list(ret.values())