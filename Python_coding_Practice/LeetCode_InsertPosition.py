def findinsertposition(start, end, arr = [], target = 0):
    if(end <= start)
        return 
    mid = (start + end) / 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:

    else:
        return findinsertposition(mid+1, end, arr, target)


