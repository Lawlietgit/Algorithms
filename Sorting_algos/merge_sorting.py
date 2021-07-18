from gen_input import gen_random_array

class MergeSort(object):
    def __init__(self, n):
        self.input_arr = gen_random_array(n)

    def merge(self, left, right):
        """
        Merge 2 sorted arrays, return the resulted array
        """
        m, n = len(left), len(right)
        res = [0]*(m+n)
        i, j = 0, 0
        while i < m or j < n:
            current_left = left[i] if i < m else float('inf')
            current_right = right[j] if j < n else float('inf') 
            if current_left <= current_right:
                res[i+j] = current_left
                i += 1
            else:
                res[i+j] = current_right
                j += 1
        return res

merge_sort = MergeSort(10)
print(merge_sort.merge([1,3,7,8],[0,2,4,9]))
