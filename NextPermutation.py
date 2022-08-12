def nextPermutation(self, nums):
    """ O(N)T O(1)S_in_place"""
    idx1 = next((i for i in range(len(nums) - 2, -1, -1) if nums[i] < nums[i + 1]), None)
    if idx1 is not None:
        idx2 = next((i for i in range(len(nums) - 1, idx1, -1) if nums[i] > nums[idx1]), None)
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
        nums[idx1 + 1:] = sorted(nums[idx1 + 1:])
    else:
        nums.sort()
