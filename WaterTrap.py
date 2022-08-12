def Trap(height):
    if not height:
        return 0
    
    l, r = 0, len(height) - 1
    leftmax, rightmax = height[l], height[r]
    result = 0
    while l<r:
        if leftmax < rightmax:
            l += 1
            leftmax = max(leftmax, height[l])
            result += rightmax - height[l]
        else:
            r -= 1
            rightmax = max(rightmax, height[r])
            result += rightmax - height[r]
    return result
