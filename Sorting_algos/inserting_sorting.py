from gen_input import gen_random_array

input_arr = gen_random_array(100)

# Time complexity: O(N^2)
# Space complexity: O(N)

print(f"Before sorting: {input_arr}")

def run_insert(arr, a):
    insert_pos = -1
    for i, num in enumerate(arr):
        if num >= a:
            insert_pos = i
            break
    if insert_pos == -1:
        insert_pos = len(arr)
    arr.insert(insert_pos, a)
    return arr

def insertion_sort(arr):
    current_arr = []
    for a in arr:
        current_arr = run_insert(current_arr, a)
    return current_arr

output_arr = insertion_sort(input_arr)
print(f"After sorting: {output_arr}")


