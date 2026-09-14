class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)
        for num in nums:
            mapping[num]+=1

        freq = [[] for i in range(len(nums) + 1)] 
        for key, value in mapping.items():
            freq[value].append(key)

        returnList = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                returnList.append(n)
                if len(returnList) == k:
                    return returnList
        
            

        
       

