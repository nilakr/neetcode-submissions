class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = []
        # suffix = [1] * len(nums)

        # num1 = 1
        # for i in range(len(nums) + 1):
        #     if i != 0:
        #         prefix.append(num1)
        #         num1 *= nums[i - 1]

        # num2 = 1
        # for i in range(len(nums) + 1, 0, -1):
        #     if i != len(nums) + 1:
        #         suffix[i - 1]= num2
        #         num2 *= nums[i - 1]


        # for i in range(len(nums)):
        #     prefix[i] = suffix[i] * prefix[i]

        # return prefix

        #Division Way

        val = 1
        zeroCount = 0
        output = [0] * len(nums)
        for num in nums:
            if num != 0:
                val *= num 
            if num == 0:
                zeroCount += 1  #val contains the mult. val of all of the list
        
        if zeroCount > 1:
            return output
        elif zeroCount == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    output[i] = val 
        else:
            for i in range(len(nums)):
                output[i] = val // nums[i]

        return output



        

