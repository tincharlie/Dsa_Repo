def maxSubarray(nums):
    m = nums[0]
    s = 0
    for i in nums:
        if s < 0:
            s = 0
        s += i
        m = max(m,s)
    return m
