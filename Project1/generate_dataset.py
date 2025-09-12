import random

def generate_input_sizes():
    input_sizes = []
    for i in range(10):
        input_sizes.append((i+1) * 1000)
        input_sizes.append((i+1) * 10000)
        input_sizes.append((i+1) * 100000)
        input_sizes.append((i+1) * 1000000)
    input_sizes = sorted(set(input_sizes))
    return input_sizes

def generate_datasets(seed=42):
    random.seed(seed)  #initializes the random number generator with a specific starting value (seed).tells Python's random module:“Start generating random numbers from this exact point.”
    input_sizes = generate_input_sizes()
    input_data = []
    for s in input_sizes:
        data = [random.randint(1, s) for _ in range(s)]
        input_data.append(data)
    return input_data, input_sizes

def verify_datasets(input_data, input_sizes):
    for i in range(len(input_data)):
        print("Array Size:", len(input_data[i]))
        print("Min of this array:", min(input_data[i]))
        print("Max of this array:", max(input_data[i]))
        print()
