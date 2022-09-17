"""
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
"""

from typing import List


class Solution:    
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int, recurr: bool = True) -> int:
        max_left = 0                
        max_sum = 0
        
        ll = rl = 0         # left window
        lm = rm = 0         # mid window        
        
        sum_l = sum_m = sum_r = 0
        while rm < len(nums):
            sum_m += nums[rm]
            
            if rm - lm + 1 > firstLen: # mid window
                sum_m -= nums[lm]
                lm += 1
            
            if rl != 0: # left window
                sum_l += nums[rl]
                sum_l -= nums[ll]
                rl += 1
                ll += 1                             
                
            if lm == secondLen: # start the second window tracking to left of mid window
                while rl < lm:
                    sum_l += nums[rl]  
                    rl += 1                        
                            
            max_left = max(max_left, sum_l)                        
            max_sum = max(max_sum, max_left + sum_m)
            rm += 1
        
        if recurr:
            return max(max_sum, self.maxSumTwoNoOverlap(nums, secondLen, firstLen, False))
        else:
            return max_sum