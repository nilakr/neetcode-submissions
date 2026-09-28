class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num]+=1

        frequencies = []
        for num in map:
            frequencies.append([map[num], num])

        frequencies.sort()

        result = []

        for i in range(k):
            result.append(frequencies.pop()[1])

        return result



       

        
            

        
       

