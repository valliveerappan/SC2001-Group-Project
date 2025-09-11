from key_comparisons import KeyComparisons
from hybrid_sort import hybrid_sort
from generate_dataset import generate_datasets, verify_datasets

def main():
    input_data, input_sizes = generate_datasets()
    verify_datasets(input_data, input_sizes)

    threshold_S = 50
    print(f"Running hybrid sort with S = {threshold_S} on all datasets\n")

    for i in range(len(input_sizes)):
        size = input_sizes[i]
        dataset = input_data[i]

        comp_obj = KeyComparisons()
        hybrid_sort(dataset, threshold_S, comp_obj)
        print(f"Array Size: {size}, Key Comparisons: {comp_obj.key_comparisons}")


if __name__ == "__main__":
    main()
