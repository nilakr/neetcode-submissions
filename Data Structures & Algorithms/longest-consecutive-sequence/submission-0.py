class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        maxLength = 0
        map = defaultdict(int)
        for i in range(len(nums)):
            map[nums[i]] = i
        for i in range(len(nums)):
            if (nums[i] - 1) not in map:
                length += 1
                current = nums[i] + 1
                while current in map:
                    length += 1
                    current += 1
            maxLength = max(length, maxLength)
            length = 0
                    
        return maxLength