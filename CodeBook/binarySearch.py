values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # value should be sorted
target = 8

def binarySearch(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid # Return the index
            # return values[mid] - returns the value
        elif values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binarySearch(values, target))