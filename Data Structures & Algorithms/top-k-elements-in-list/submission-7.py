class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)
        for num in nums:
            mapping[num]+=1
        
        sorted_mapping = sorted(mapping.items(), reverse = True, key=lambda item: item[1])

        returnList = []
        for i in range(k):
            returnList.append(sorted_mapping[i][0])

        return returnList



