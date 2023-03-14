'''
Given an array nums of integers, find the contiguous subarray with the largest sum.
'''

def max_subarray_sum(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
    return max(dp)
  
 '''
 In the above code, we first initialize a list dp of size n where `n
 '''
