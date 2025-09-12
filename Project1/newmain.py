from key_comparisons import KeyComparisons
from hybrid_sort import hybrid_sort
from generate_dataset import generate_datasets, verify_datasets
from plots import plot_results
from plottime import plot_time
import time
import csv

def main():
    input_data, input_sizes = generate_datasets()
    verify_datasets(input_data, input_sizes)

    threshold_S = 50
    print(f"Running hybrid sort with S = {threshold_S} on all datasets\n")
    comparisons = []
    time_taken = []
    for i in range(len(input_sizes)):
        size = input_sizes[i]
        dataset = input_data[i]
        comp_obj = KeyComparisons()
        start_time = time.time()
        hybrid_sort(dataset, threshold_S, comp_obj)
        end_time = time.time()
        elapsed_time = end_time - start_time
        time_taken.append(elapsed_time)
        print(f"Array Size: {size}, Key Comparisons: {comp_obj.key_comparisons}, Time taken: {elapsed_time:.4f} seconds")
        # Store the number of comparisons for analysis
        comparisons.append(comp_obj.key_comparisons)
    
    with open('hybrid_sort_results.csv', mode='w', newline='') as file:  ##saving file heere
        writer = csv.writer(file)
        writer.writerow(['Input Size', 'Key Comparisons', 'Time Taken'])  # header
        for size, comp, t in zip(input_sizes, comparisons, time_taken):
            writer.writerow([size, comp, t]) 

    print("\nPlotting results...")
    plot_results(input_sizes, comparisons, threshold_S)
    plot_time(input_sizes, time_taken)
    print("All datasets sorted and results plotted.")

if __name__ == "__main__":
    main()
