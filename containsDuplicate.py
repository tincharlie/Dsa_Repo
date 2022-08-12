def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dictNums = {}
    for i in nums:
        if i not in dictNums:
            dictNums[i] = 1
        else:
            return True

    return False
nums = [1,2,3,4,1]
containsDuplicate(nums)

def containsDuplicate1(nums):
    NumSet = set(nums)
    if len(nums) == len(NumSet):
        return False
    return True
nums = [1,2,3,4,1]
containsDuplicate1(nums)

def containsDuplicate2(nums):
    
    numslen = len(nums)
    if numslen < 2:
        return False
    nums.sort()
    for i in range(numslen - 1):
        if nums[i] == nums[i+1]:
            return True
        return False
nums = [1,2,3,4,1]
containsDuplicate2(nums)
