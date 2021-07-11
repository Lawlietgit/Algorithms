from gen_input import gen_random_array

input_arr = gen_random_array(100)

# Time complexity: O(N^2)
# Space complexity: O(1)

print(f"Before sorting: {input_arr}")

def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        a, b = arr[i], arr[i+1]
        if a > b:
            arr[i], arr[i+1] = arr[i+1], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        bubble(arr[:n-i])

bubble_sort(input_arr) # in-place
print(f"After sorting: {input_arr}")


