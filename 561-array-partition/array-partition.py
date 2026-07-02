class Solution(object):
    def arrayPairSum(self, nums):
        n = len(nums)
        nums.sort()
        
        total_sum = 0
        
        
        for i in range(0, n, 2):
            total_sum += nums[i]
            
        return total_sum
        



             


        