class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)
        for i in range(len(nums)):
            map[nums[i]] = i #maps each number in nums to its index

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map:
                if i != map[complement]:
                    return [i, map[complement]]
        

        