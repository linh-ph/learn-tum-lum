def merge_sort(arr, length_hyphens = 0):
    
    if len(arr) <= 1:
        print( print_hyphens(len(arr) + length_hyphens) + "Returning array:", arr)
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    print(print_hyphens(mid + length_hyphens) + "Dividing array", arr, "into", left_half, "and", right_half)
    
    left_half = merge_sort(left_half, (mid + length_hyphens))
    print(print_hyphens(mid + length_hyphens) +'left_half_after_merge', left_half)
    right_half = merge_sort(right_half, (mid + length_hyphens))
    print(print_hyphens(mid + length_hyphens) +'right_half_after_merge', right_half)
    
    return merge(left_half, right_half)
    
    
def merge(left, right):
    merged_arr = []
    left_idx, right_idx = 0, 0
    print("subarrays", left, "and", right, "left_idx", left_idx, "right_idx", right_idx)
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged_arr.append(left[left_idx])
            left_idx += 1

        else:
            merged_arr.append(right[right_idx])
            right_idx += 1

    print('sort_done', merged_arr)
    print('merged_arr_at_left+1', left[left_idx:])
    merged_arr += left[left_idx:]

    print('merged_arr_at_right+1', right[right_idx:])
    merged_arr += right[right_idx:]

    print("Merging subarrays", left, "and", right, "into", merged_arr)
    return merged_arr

def print_hyphens(length):
    return ("-" * length)
    
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr, len(arr))
print("Sorted array:", sorted_arr)