class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [1] * len(nums)

        num1 = 1
        for i in range(len(nums) + 1):
            if i != 0:
                prefix.append(num1)
                num1 *= nums[i - 1]

        num2 = 1
        for i in range(len(nums) + 1, 0, -1):
            if i != len(nums) + 1:
                suffix[i - 1]= num2
                num2 *= nums[i - 1]


        for i in range(len(nums)):
            prefix[i] = suffix[i] * prefix[i]

        return prefix
