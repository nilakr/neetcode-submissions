class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)
        for num in nums:
            mapping[num]+=1
        
        elems = list(mapping.values())
        returnList = []
        for i in range(k):
            if [key for key, value in mapping.items() if value == max(elems)] not in returnList:
                returnList.extend([key for key, value in mapping.items() if value == max(elems)])
                elems.remove(max(elems))

        return returnList



