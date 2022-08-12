def  BSMinMax(arr):
    low = 0
    high = len(arr) - 1
    arr_max = arr[low]
    arr_min = arr[low]
    
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max, arr_min)
    
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)
    else:
        
        mid = int((low + high)/2)

        arr_max1, arr_min1 = BSMinMax(arr)
        arr_max2, arr_min2 = BSMinMax(arr)
    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))
    
def getMinMax(arr, n):
        minmax = pair()
        """
        if there is only one element then return it as min & max
        """
        
        if n == 1:
            minmax.max = arr[0]
            minmax.min = arr[0]            
            return minmax
        
        """
        If there is more than one elements, then initialize min & max
        """
        
        if arr[0] > arr[1]:
            minmax.max = arr[0]
            minmax.min = arr[1]
        else:
            minmax.max = arr[1]
            minmax.min = arr[0]
            
        for i in range(2, n):
            if arr[i] > minmax.max:
                minmax.max = arr[i]
            elif arr[i] < minmax.min:
                minmax.min = arr[i]
                
        return "Min Value: "+str(minmax.min)+ " Max Value: " + str(minmax.max)
