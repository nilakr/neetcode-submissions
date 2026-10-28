class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        returnList = []
        for num in nums:
            map[num] += 1

        frequencies = []
        for num in map:
            frequencies.append([map[num], num]) #list w/ times it appears and the num

        frequencies.sort(reverse = True)

        for i in range(k):
            returnList.append(frequencies[i][1])

        return returnList

        
       

        
            

        
       

