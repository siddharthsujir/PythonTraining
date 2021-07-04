def twosum(arr, target):
    dict1 = {}
    index = 0

    for i in arr:
        if i not in dict1.keys():
            dict1[i] = index
        index += 1
    index = 0
    for k in arr:
        diff = target - k
        if diff in dict1.keys():
            return index, dict1.get(diff)
        index += 1
    return -1, -1

arr = {2, 3, 4, 5}
target = 7
print(twosum(arr, target))
