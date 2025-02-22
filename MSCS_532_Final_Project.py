import time
import random
import bisect
import functools
import threading
import matplotlib.pyplot as plt
from sortedcontainers import SortedList
from collections import defaultdict

# Generate a large dataset
data_size = 10000000
data = [random.randint(1, 100000000) for _ in range(data_size)]


# Implementing linear search
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            print(f"*********** Found target = {num} at index = {i}")
            return i
    return -1


# Implementing binary search using bisect to insert element in sorted order
def binary_search(arr, target):
    index = bisect.bisect_left(arr, target)
    return index if index < len(arr) and arr[index] == target else -1


# Hash search algorithm, the targe itself is the key
def hash_search(hash_table, target):
    return target in hash_table


# Quick sort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Using binary search with cache optimization
@functools.lru_cache(maxsize=100000)
def cached_search(arr_tuple, target):
    arr = list(arr_tuple)
    return binary_search(arr, target)


# Parallel search using binary search implementation
def parallel_search(arr, target, results, index):
    results[index] = binary_search(arr, target)


# Calculate end - start time for the function executed, and return the search result
def measure_execution_time(search_function, *args):
    start_time = time.time()
    result = search_function(*args)
    end_time = time.time()
    print("*********** Search result index = ", result)
    return result, (end_time - start_time)


# Prepare Data Structures
sorted_data = quicksort(data)
hash_table = set(data)
b_tree = SortedList(data)

# Select a target at random
target = random.choice(data)

# Runing Tests
# A dictionary to hold multiple search results
results = {}

# Performing search using linear search
print("\n******************************************************************")
print("*********** Linear Search ")
print("*********** Target = ", target)
results["Linear Search"] = measure_execution_time(linear_search, data, target)
print("******************************************************************")

# Performing search using binary search
# Binary Search requries the array to be in sorted order to function properly
print("\n******************************************************************")
print("*********** Binary Search ")
print("*********** Target = ", target)
results["Binary Search (Sorted)"] = measure_execution_time(
    binary_search, sorted_data, target
)
print("******************************************************************")

# Performing search using binary search
# Binary Search requries the array to be in sorted order to function properly
print("\n******************************************************************")
print("*********** Hash Search ")
print("*********** Target = ", target)
results["Hash Table Search"] = measure_execution_time(hash_search, hash_table, target)
print("******************************************************************")

# Performing search using binary search
# Binary Search requries the array to be in sorted order to function properly
print("\n******************************************************************")
print("*********** Binary search using b-tree ")
print("*********** Target = ", target)
results["B-Tree Search"] = measure_execution_time(binary_search, b_tree, target)
print("******************************************************************")

# Performing search using binary search
# Binary Search requries the array to be in sorted order to function properly
print("\n******************************************************************")
print("*********** Binary search using cache ")
print("*********** Target = ", target)
results["Cached Search"] = measure_execution_time(
    cached_search, tuple(sorted_data), target
)
print("******************************************************************")

# Parallel Execution
# Performing search using multiple threads
# Dividing data into 2 sizes
print("\n******************************************************************")
print("*********** Parallel search using multiple threads ")
print("*********** Target = ", target)
thread_results = [None, None]
thread1 = threading.Thread(
    target=parallel_search,
    args=(sorted_data[: data_size // 2], target, thread_results, 0),
)
thread2 = threading.Thread(
    target=parallel_search,
    args=(sorted_data[data_size // 2 :], target, thread_results, 1),
)

start_time = time.time()
# Start Thread execution
thread1.start()
thread2.start()
# Join the threads
thread1.join()
thread2.join()
parallel_time = time.time() - start_time
results["Parallel Binary Search"] = (thread_results, parallel_time)
print("Search results, left and right threads ", thread_results)
print("******************************************************************")


## Print Results
execution_times = []
search_methods = []

print("\n******************************************************************")
print("*********** Execution Times  ")
print("******************************************************************")
for key, value in results.items():
    print(f"{key}: Result = {value[0]}, Time Taken = {value[1]:.6f} sec")
    search_methods.append(key)
    execution_times.append(value[1])


## Plot Execution Time Graph
plt.figure(figsize=(10, 5))
plt.barh(
    search_methods,
    execution_times,
    color=["red", "blue", "green", "purple", "orange", "cyan"],
)
plt.xlabel("Execution Time (seconds)")
plt.ylabel("Search Method")
plt.title("Comparison of Search Algorithm Execution Times")
plt.gca().invert_yaxis()  # Invert axis to have the fastest at the top
plt.show()

print("\n************** End of Functionality Tests **********************")


print("\n************** Beginning Stress Tests **********************")
# Stress Testing
# Generate different dataset sizes for stress testing
data_sizes = [100000, 300000, 900000]
# Different test cases
test_cases = ["random", "min", "max", "nonexistent"]

# Loop through each data size
for data_size in data_sizes:
    print(f"\nTesting with data size: {data_size}")
    data = [random.randint(1, 10000000) for _ in range(data_size)]
    sorted_data = quicksort(data)
    hash_table = set(data)
    b_tree = SortedList(data)

    # For each data size run through each test cases
    for target_case in test_cases:
        # Choose target as random
        if target_case == "random":
            target = random.choice(data)
        # Choose target as minimum value
        elif target_case == "min":
            target = min(data)
        # Choose target as maximum value
        elif target_case == "max":
            target = max(data)
        # Choose target that does not exist
        elif target_case == "nonexistent":
            target = max(data) + 1

        print(f"\n  Testing with target: {target_case} (Target: {target})")

        results["Linear Search"] = measure_execution_time(linear_search, data, target)
        results["Binary Search (Sorted)"] = measure_execution_time(
            binary_search, sorted_data, target
        )
        results["Hash Table Search"] = measure_execution_time(
            hash_search, hash_table, target
        )
        results["B-Tree Search"] = measure_execution_time(binary_search, b_tree, target)
        results["Cached Search"] = measure_execution_time(
            cached_search, tuple(sorted_data), target
        )

        # Parallel Execution
        thread_results = [None, None]
        thread1 = threading.Thread(
            target=parallel_search,
            args=(sorted_data[: data_size // 2], target, thread_results, 0),
        )
        thread2 = threading.Thread(
            target=parallel_search,
            args=(sorted_data[data_size // 2 :], target, thread_results, 1),
        )

        start_time = time.time()
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        parallel_time = time.time() - start_time
        results["Parallel Binary Search"] = (
            thread_results,
            parallel_time,
        )
        # Print Results
        execution_times = []
        search_methods = []
        print("\n******************************************************************")
        print("*********** Execution Times  ")
        print("******************************************************************")
        for key, value in results.items():
            print(f"{key}: Result = {value[0]}, Time Taken = {value[1]:.6f} sec")
            search_methods.append(key)
            execution_times.append(value[1])

        # Plot Execution Time Graph
        plt.figure(figsize=(12, 6))
        plt.barh(
            search_methods,
            execution_times,
            color=["red", "blue", "green", "purple", "orange", "cyan"],
        )
        plt.xlabel(f"Execution Time (seconds) for {target_case} in finding {target}")
        plt.ylabel("Search Method")
        plt.title(
            f"Comparison of Search Algorithm Execution Times (Stress Testing) for data size {data_size}"
        )
        plt.gca().invert_yaxis()  # Invert axis to have the fastest at the top
        plt.show()
