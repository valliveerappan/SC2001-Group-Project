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
    i = j = 0
    len1, len2 = len(list1), len(list2)

    while i < len1 and j < len2:
        if comp_obj.less_than_or_equal(list1[i], list2[j]):
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1

    # Append the remaining elements from both lists
    sorted_list.extend(list1[i:])
    sorted_list.extend(list2[j:])
    return sorted_list

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
