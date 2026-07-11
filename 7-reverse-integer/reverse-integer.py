class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        
        reversed_num = int(str(x)[::-1]) * sign
        
        
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
            
        return reversed_num