# Recursive way
def bin_search(num, target, low=0, high=None):
    if high is None:
        high = len(num) - 1
        
    if high >= low:
        mid = (high + low)//2
        if num[mid] < target:
            return bin_search(num, target, mid+1, high)
        elif num[mid] > target:
            return bin_search(num, target, low, mid-1)
        else:
            return mid
    else:
        return -1


# Iterative
def binary_search(num, target):
    low = 0
    high = len(num) - 1
    mid = 0
    while high >= low:
        mid = (low + high)//2
        if num[mid] < target:
            low = mid + 1
        elif num[mid] > target:
            high = mid - 1
        else:
            return mid
    return None


n = [1, 2, 3, 4, 5]
for i in range(len(n)):
    print(f"-----------------\nlista = {n}, numero = {i+1}")
    print("Recursive: ", bin_search(n, i+1))
    print("Iterative: ", binary_search(n, i+1))
