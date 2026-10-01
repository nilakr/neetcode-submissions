class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        result = []
        
        map = sorted(map.items(), key = lambda item: item[1])

        for i in range(k):
            result.append(map.pop()[0])

        return result



       

        
            

        
       

