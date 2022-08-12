def reverseList(A): ## Only One parameter passing
    start = 0
    end = len(A) - 1
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1 ## It will take the no. from the start
        end -= 1 ## It will take the no. from the last
