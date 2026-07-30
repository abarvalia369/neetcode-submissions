class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        data = {}
        ctr = 0
        ret = []

        for x in nums:
            if x in data:
                data[x] += 1
            else:
                data[x] = 1
        #^ adds key(val in num) and val(cnt of val in num)
        largest = sorted(data.items(), key=lambda kv: kv[1], reverse = True)
        #^ sorted returns list of sorted tuple pairs from dict
        for x in largest:
            if ctr<k:
                ret.append(x[0])#adds the first(key) in the pair of tuples in largest
            ctr += 1
        
        return ret
#O(nlogn) since sorted() is that
