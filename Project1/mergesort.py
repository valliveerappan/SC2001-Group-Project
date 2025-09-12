import matplotlib.pyplot as plt
import random
import csv

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
    sizes = list(range(10, 10001, 100))  # Different input sizes from 100 to 1000
    comparisons = []

    for n in sizes:
        input_data = [random.randint(1, n) for _ in range(n)]  # Generate random data
        comp_obj = KeyComparisons()
        merge_sort(input_data.copy(), comp_obj)  
        comparisons.append(comp_obj.get())
        print(f"Input size: {n}, Key comparisons: {comp_obj.get()}")
    with open('merge_sort_results.csv', mode='w', newline='') as file: #this is to create and import results to a csv in case you dont want to run the program again
        writer = csv.writer(file)
        writer.writerow(['Input Size', 'Key Comparisons'])  # header
        for size, comp in zip(sizes, comparisons):
            writer.writerow([size, comp])    
    # Plot results
    plt.plot(sizes, comparisons, marker='', label='Key Comparisons (Merge Sort)')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Number of Key Comparisons')
    plt.title('Merge Sort: Key Comparisons vs Input Size')
    #plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()


