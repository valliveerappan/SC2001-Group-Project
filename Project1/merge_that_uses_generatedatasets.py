import matplotlib.pyplot as plt
import random
import csv
import time
from key_comparisons import KeyComparisons
from generate_dataset import generate_datasets, verify_datasets
from sorting_algo import merge_sort

def main():
    comparisons = []
    time_taken = []
    input_data, input_sizes = generate_datasets()

    for i in range(len(input_sizes)):
        sizes = input_sizes[i]
        dataset = input_data[i]
        comp_obj = KeyComparisons()
        start_time = time.time()
        merge_sort(dataset, comp_obj) 
        end_time = time.time()
        elapsed_time = end_time - start_time
        time_taken.append(elapsed_time) 
        comparisons.append(comp_obj.get())
        print(f"Input size: {sizes}, Key comparisons: {comp_obj.get()}, Time taken: {elapsed_time:.4f} seconds ")
    with open('merge_sort_results_10million.csv', mode='w', newline='') as file:
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


