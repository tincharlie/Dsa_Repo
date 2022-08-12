def findMinChocDiff(arr, m):
    """
    params: 
    1. arr= lst of choclate
    2. n = len(arr)
    3. m = No. of students
    """
    n = len(arr)
    if n==0 or m==0:
        return 0
    
    arr.sort()
    
    # If no.of chocolate is less then no. of students then return -1
    if n < m:
        return -1
    # Largest number of chocolates
    min_diff = arr[n-1] - arr[0]
    
    # Find the subarray of size m such that
    # difference between last (maximum in case
    # of sorted) and first (minimum in case of
    # sorted) elements of subarray is minimum.
    for i in range(n - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])
        
    return min_diff
