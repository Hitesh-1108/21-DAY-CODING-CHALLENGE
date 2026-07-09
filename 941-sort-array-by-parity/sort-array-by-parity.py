class Solution(object):
    def sortArrayByParity(self, nums):
        n=len(nums)
        temp=[]
        null=[]
        for i in range(0,n):
            if nums[i]%2==0:
                temp.append(nums[i])
            else:
                null.append(nums[i])    
        z=len(temp)
        for i in range(0,z):
            nums[i]=temp[i]
        for i in range(z,n):
            nums[i]=null[i-z]
        return nums    

        