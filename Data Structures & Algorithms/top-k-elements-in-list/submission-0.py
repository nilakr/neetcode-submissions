class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)
        for num in nums:
            mapping[num]+=1
        
        elems = list(mapping.values())
        returnList = [0] * k
        for i in range(k):
            returnList[i] = next((key for key, value in mapping.items() if value == max(elems)), None)
            elems.remove(max(elems))

        return returnList



