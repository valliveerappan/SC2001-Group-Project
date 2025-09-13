import random
import matplotlib.pyplot as plt

class KeyComparisons:
    def __init__(self):
        self.key_comparisons = 0

    def less_than(self, a, b):
        self.key_comparisons += 1
        return a < b

    def less_than_or_equal(self, a, b):
        self.key_comparisons += 1
        return a <= b

    def get(self):
        return self.key_comparisons

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def insertion_sort(arr, comp_obj: KeyComparisons):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if comp_obj.less_than(arr[j], arr[j - 1]):
                swap(arr, j, j - 1)
            else:
                break
    return arr

def merge(list1, list2, comp_obj: KeyComparisons):
    sorted_list = []
    while list1 and list2:
        if comp_obj.less_than_or_equal(list1[0], list2[0]):
            sorted_list.append(list1.pop(0))
        else:
            sorted_list.append(list2.pop(0))
    return sorted_list + list1 + list2

def hybrid_sort(arr, S, comp_obj: KeyComparisons):
    if len(arr) <= S:
        return insertion_sort(arr, comp_obj)
    mid = len(arr) // 2
    left = hybrid_sort(arr[:mid], S, comp_obj)
    right = hybrid_sort(arr[mid:], S, comp_obj)
    return merge(left, right, comp_obj)

def generate_dataset(n, seed=42):
    random.seed(seed)
    return [random.randint(1, n) for _ in range(n)]

def find_optimal_S():
    input_size = 100000
    data = generate_dataset(input_size)
    S_values = list(range(10, 110, 10))
    comparison_counts = []

    for S in S_values:
        dataset_copy = data.copy()
        comp_obj = KeyComparisons()
        hybrid_sort(dataset_copy, S, comp_obj)
        comparison_counts.append(comp_obj.get())

    # Plot the results
    plt.plot(S_values, comparison_counts, marker='o')
    plt.title("Key Comparisons vs Threshold S")
    plt.xlabel("Threshold S")
    plt.ylabel("Key Comparisons")
    plt.grid(True)
    plt.show()

find_optimal_S()
