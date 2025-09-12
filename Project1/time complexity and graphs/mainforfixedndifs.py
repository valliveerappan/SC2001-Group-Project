from key_comparisons import KeyComparisons
from hybrid_sort import hybrid_sort
#from generate_dataset import generate_datasets, verify_datasets
import random
import matplotlib.pyplot as plt

def plot_results(sizes, comparisons, n):
    print(f"[DEBUG] Sizes: ")
    print(f"[DEBUG] Comparisons: ")
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, comparisons, marker='o', label=f'Empirical (n={n})')
    #plt.plot(sizes, [n * (n.bit_length()) for n in sizes], linestyle='--', color='gray', label='Theoretical O(n log n)')
    plt.xlabel("Values of S")
    plt.ylabel("Number of Key Comparisons")
    plt.title(f"Key Comparisons vs Values of S (Hybrid Sort, n={n})")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():

    n=80000
    input_data = [random.randint(1, n) for _ in range(n)]
    
    threshold_S = []
    comparisons = []

    for i in range(1,50,1):#
        S = i
        threshold_S.append(S)
        comp_obj = KeyComparisons()
        hybrid_sort(input_data.copy(), S, comp_obj)
        print(f"S: {S}, Key Comparisons: {comp_obj.key_comparisons}")
        # Store the number of comparisons for analysis
        comparisons.append(comp_obj.key_comparisons)
    plot_results(threshold_S, comparisons, n)



if __name__ == "__main__":
    main()
