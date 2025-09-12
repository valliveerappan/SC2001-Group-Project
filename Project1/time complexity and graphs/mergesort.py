import matplotlib.pyplot as plt
import random
import csv
import time

# KeyComparisons class remains the same
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

def merge(list1, list2, comp_obj: KeyComparisons):
    sorted_list = []
    while list1 and list2:
        if comp_obj.less_than_or_equal(list1[0], list2[0]):
            sorted_list.append(list1.pop(0))
        else:
            sorted_list.append(list2.pop(0))
    return sorted_list + list1 + list2

def merge_sort(arr, comp_obj: KeyComparisons):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], comp_obj)
    right = merge_sort(arr[mid:], comp_obj)
    return merge(left, right, comp_obj)

def main():
    sizes = list(range(10, 10000000, 100))  # Different input sizes from 100 to 1000
    comparisons = []
    time_taken = []
    for n in sizes:
        input_data = [random.randint(1, n) for _ in range(n)]  # Generate random data
        comp_obj = KeyComparisons()
        start_time = time.time()
        merge_sort(input_data.copy(), comp_obj) 
        end_time = time.time()
        elapsed_time = end_time - start_time
        time_taken.append(elapsed_time) 
        comparisons.append(comp_obj.get())
        print(f"Input size: {n}, Key comparisons: {comp_obj.get()}, Time taken: {elapsed_time:.4f} seconds ")
    with open('merge_sort_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Input Size', 'Key Comparisons', 'Time Taken'])  # header
        for size, comp, t in zip(sizes, comparisons, time_taken):
            writer.writerow([size, comp, t])    
    # Plot results
    #plt.subplot(1, 2)ignorethisline
    plt.plot(sizes, comparisons, marker='', label='Key Comparisons (Merge Sort)')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Number of Key Comparisons')
    plt.title('Merge Sort: Key Comparisons vs Input Size')
    #plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure
    plt.plot(sizes, time_taken, marker='', color='red', label='Time Taken (s)')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Merge Sort: Time Taken vs Input Size')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()


