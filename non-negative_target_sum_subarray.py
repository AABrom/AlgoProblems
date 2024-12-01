# if non-negative array has a sum(subarray) == X
def subarray_sum(input_array, X):
    right, current_sum = 0, 0
    for left in range(len(input_array)):
        if left > 0:
            current_sum-=input_array[left-1] 

        while right < len(input_array) and current_sum<X:
            current_sum+=input_array[right]
            right+=1

        if current_sum == X:
            return True
    return False


