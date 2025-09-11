import key_comparisons
from sorting_algo import insertion_sort
from sorting_algo import merge

def hybrid_sort(arr, S, comp_obj: key_comparisons.KeyComparisons):
    #if array size <= S, use insertion sort
    if len(arr) <= S:
        return insertion_sort(arr, comp_obj)

    #otherwise split array and sort halves recursively using hybrid sort
    else:
        mid = len(arr) // 2
        left = hybrid_sort(arr[:mid], S, comp_obj)
        right = hybrid_sort(arr[mid:], S, comp_obj)
        #merge sorted halves into one array
        return merge(left, right, comp_obj)