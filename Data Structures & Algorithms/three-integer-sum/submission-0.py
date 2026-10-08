class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #ascending order
        returnList = []

        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            target = -nums[i] #the other 2 numbers should add up to the negative of this 
            l, r = i + 1, len(nums) - 1
            while (l < r):
                if ((nums[l] + nums[r]) < target):
                    l+=1
                elif ((nums[l] + nums[r]) > target):
                    r-=1
                elif ((nums[l] + nums[r]) == target):
                    returnList.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -=1
            
        
        return returnList
