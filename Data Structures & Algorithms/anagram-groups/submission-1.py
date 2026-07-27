class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ret = defaultdict(list)#{char ctr:list of anagrams}

        for x in strs:
            ctr = [0]*26
            for c in x:
                ctr[ord(c) - ord('a')] += 1

            ret[tuple(ctr)].append(x)
        return list(ret.values())