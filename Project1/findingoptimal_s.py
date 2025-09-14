#from key_comparisons import KeyComparisons
import matplotlib.pyplot as plt
import time
#keeps track of how many comparisons made when sorting arr for analysing efficiency
class KeyComparisons:
    def __init__(self):
        self.key_comparisons = 0

    def less_than(self, a, b):
        self.key_comparisons += 1
        return a < b

    def less_than_or_equal(self, a, b):
        self.key_comparisons += 1
        return a <= b

    def reset(self):
        self.key_comparisons = 0

    def get(self):
        return self.key_comparisons


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
    if len(arr) <= 1:                      #
        return arr
    #middle index that splits the array
    mid = len(arr) // 2                    #
    #recursively sort left half of array
    left = merge_sort(arr[:mid], comp_obj) #T(N/2)
    #recursively sort right half of array
    right = merge_sort(arr[mid:], comp_obj)#T(N/2)
    #merge two sorted halves into single array
    return merge(left, right, comp_obj)    #CALLS log n times, each time does n-1 comparisons

def main():
    NUMBEROFRUNS = 100000
    n = [i for i in range(1, 11)]

    insertionsorttime = []
    mergesorttime = []
    dif=[]
    
    for i in n:
        insertion_total = 0
        merge_total = 0
        for _ in range(NUMBEROFRUNS):
         input_data = [j for j in range(i, 0, -1)]  # Generate reverse sorted data

         comp_obj1 = KeyComparisons()
         start_time = time.time()
         insertion_sort(input_data.copy(), comp_obj1)
         end_time = time.time()
         elapsed_time = (end_time - start_time)*1000  # convert to milliseconds  
         insertion_total += (elapsed_time)
 
         comp_obj2 = KeyComparisons()
         start_time = time.time()
         merge_sort(input_data.copy(), comp_obj2)
         end_time = time.time()
         elapsed_time = (end_time - start_time)*1000  # convert to milliseconds
         merge_total += (elapsed_time)
 
        avg_insertion = (insertion_total / NUMBEROFRUNS) 
        avg_merge = (merge_total / NUMBEROFRUNS)

        insertionsorttime.append(avg_insertion)
        mergesorttime.append(avg_merge)
        dif.append(avg_merge - avg_insertion)
        print(f"Input size: {i}, Average Insertion Sort Time taken: {avg_insertion:.10f} ms, Average Merge Sort Time taken: {avg_merge:.10f} ms ")
    
    #for i in range(0,100):
     # value=mergesorttime[i]-insertionsorttime[i]
      #dif.append(value)

    plt.plot(n, insertionsorttime, label='ave insertion sort time', color='blue', marker='o')
    plt.plot(n, mergesorttime, label='ave insertion sort time', color='red', marker='x')

    plt.xlabel('number of elements in array')
    plt.title('comparison between insertion sort and merge sort')
    plt.ylabel('sorting time(ms)')
    plt.legend()  #shows labels
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.plot(n, dif, label="Time Difference (Merge Sort - Insertion Sort)", color="green", marker="s")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Difference in time (ms)")
    plt.title("Difference in Sorting Time between Merge Sort and Insertion Sort")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

