def sortPairArraySumCheck(nums, x):
    n = len(nums)-1
    nums.sort()
    xi = 0 
    x = 1
    while x <= n:
        if X == nums[xi] + nums[x]:
            print("True")
            break
        elif x >= n:
            return False
        x+=1    


def sortPairArraySumCheck(nums, x):
    """nums.sort()
    x=0
    while x >= len(nums)-1:
        print(X == (nums[0] + nums[i+1]))
        for i in range(len(nums)):
            if X == (nums[0] + nums[i+1]):
                return True
            else:
                return False
            
            x+=1
    """
    n = len(nums)
    print("length of nums:", n)
    # Find the pivot element
    for i in range(0, n - 1):
        if (nums[i] > nums[i + 1]):
            break
    # l is now index of smallest element
    l = (i + 1) % n
    print("increment of i and modulus toget the remainder",l)
    # r is now index of largest element
    r = i
    print("right", i)
  
    # Keep moving either l
    # or r till they meet
    while (l != r):
  
        # If we find a pair with
        # sum x, we return True
        if (nums[l] + nums[r] == x):
            print("if l + r ",nums[l] + nums[r],"== ", x)
            return True
  
        # If current pair sum is less,
        # move to the higher sum
        if (nums[l] + nums[r] < x):
            print("if l + r ",nums[l] + nums[r],"<", x)
            l = (l + 1) % n
            print(l)
        else:
            # Move to the lower sum side
            r = (n + r - 1) % n
            print("lower sum side == ", r)
            
    return False
