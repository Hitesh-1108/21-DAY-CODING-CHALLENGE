class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        is_increasing = False
        is_decreasing = False
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                is_increasing = True
            if nums[i] > nums[i + 1]:
                is_decreasing = True
        
        return not (is_increasing and is_decreasing)