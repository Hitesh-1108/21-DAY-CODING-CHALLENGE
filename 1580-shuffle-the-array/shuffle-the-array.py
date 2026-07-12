class Solution(object):
    def shuffle(self, nums, n):
        k=len(nums)
        shuffle=[]
        for i in range(0,n):
            shuffle.append(nums[i])
            shuffle.append(nums[i+n])
        return shuffle    
