def twoSum(arr, target):
    if len(arr) == 0:
        return None
    
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return (left, right)
        
        elif arr[left] + arr[right] < target:
            left+=1
        else:
            right-=1

    
    return None
