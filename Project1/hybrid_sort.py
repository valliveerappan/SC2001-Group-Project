import key_comparisons
from sorting_algo import insertion_sort
from sorting_algo import merge

def hybrid_sort(arr, S, comp_obj: key_comparisons.KeyComparisons):
    if len(arr) <= S:
        return insertion_sort(arr, comp_obj)
    mid = len(arr) // 2
    left = hybrid_sort(arr[:mid], S, comp_obj)
    right = hybrid_sort(arr[mid:], S, comp_obj)
    return merge(left, right, comp_obj)