class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        result = []
        for num in nums:
            map[num]+=1

        map_sorted = dict(sorted(map.items(), key = lambda item: item[1]))

        for i in range(k):
            result.append(map_sorted.popitem()[0])

        # frequencies = []
        # for num in map:
        #     frequencies.append([map[num], num])

        # frequencies.sort()

        # result = []

        # for i in range(k):
        #     result.append(frequencies.pop()[1])

        return result



       

        
            

        
       

