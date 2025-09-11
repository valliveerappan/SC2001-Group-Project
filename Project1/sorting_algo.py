from key_comparisons import KeyComparisons

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def insertion_sort(arr, comp_obj: KeyComparisons):
    #start from second element (index 1) and traverse though each element in array
    for i in range(1, len(arr)):
        #compare current element with all previous elements, moving backwards
        for j in range(i, 0, -1):
            #if the current element is smaller than prev, swap
            if comp_obj.less_than(arr[j], arr[j - 1]):
                swap(arr, j, j - 1)
            #otherwise it is in correct pos so stop checking
            else:
                break
    #return sorted array
    return arr

def merge(list1, list2, comp_obj: KeyComparisons):
    sorted_list = []
    while list1 and list2:
        #compare first elements of both lists
        if comp_obj.less_than_or_equal(list1[0], list2[0]):
            #if first element of list1 is smaller, append to sorted list
            sorted_list.append(list1.pop(0))
        else:
            #otherwise append first element of list2
            sorted_list.append(list2.pop(0))
    #once one list is empty, append remaining elements from other list
    return sorted_list + list1 + list2

def merge_sort(arr, comp_obj: KeyComparisons):
    #arrays with just 0 or 1 elements are already sorted, so just return
    if len(arr) <= 1:
        return arr
    #middle index that splits the array
    mid = len(arr) // 2
    #recursively sort left half of array
    left = merge_sort(arr[:mid], comp_obj)
    #recursively sort right half of array
    right = merge_sort(arr[mid:], comp_obj)
    #merge two sorted halves into single array
    return merge(left, right, comp_obj)
