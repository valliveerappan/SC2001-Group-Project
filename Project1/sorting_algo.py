from key_comparisons import KeyComparisons

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def insertion_sort(arr, comp_obj: KeyComparisons):
    arr = arr[:]
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if comp_obj.less_than(arr[j], arr[j - 1]):
                swap(arr, j, j - 1)
            else:
                break
    return arr

def merge(list1, list2, comp_obj: KeyComparisons):
    sorted_list = []
    l1, l2 = list1[:], list2[:]
    while l1 and l2:
        if comp_obj.less_than_or_equal(l1[0], l2[0]):
            sorted_list.append(l1.pop(0))
        else:
            sorted_list.append(l2.pop(0))
    return sorted_list + l1 + l2

def merge_sort(arr, comp_obj: KeyComparisons):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], comp_obj)
    right = merge_sort(arr[mid:], comp_obj)
    return merge(left, right, comp_obj)

def hybrid_sort(arr, S, comp_obj: KeyComparisons):
    if len(arr) <= S:
        return insertion_sort(arr, comp_obj)
    mid = len(arr) // 2
    left = hybrid_sort(arr[:mid], S, comp_obj)
    right = hybrid_sort(arr[mid:], S, comp_obj)
    return merge(left, right, comp_obj)
