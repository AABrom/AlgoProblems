# if target in sorted non-negative array

def binary_search(input_array, target):
    left_idx, right_idx = 0, len(input_array)
    while left_idx<right_idx:
        mid_idx = (left_idx+right_idx) // 2
        if input_array[mid_idx] == target:
            return True
        elif input_array[mid_idx] < target:
            left_idx=mid_idx+1
        else :
            right_idx = mid_idx
    return False
