# Prefix Sum and Prefix Sum with Dictionary

## 1. Prefix Sum

### Overview

Prefix sum is a technique used for efficiently calculating the sum of elements in a subarray or subsequence. It involves creating an auxiliary array, where each element at index `i` represents the sum of elements from the beginning of the array up to index `i` (inclusive).

![image](https://github.com/sudh29/Interview_Questions/assets/73557822/816eeb07-ea32-462c-912c-bbfdc839c2ae)

## 2. Prefix Sum with Dictionary

### Overview

When using a dictionary for prefix sum, each prefix sum encountered during the traversal of an array is associated with its frequency (count). This is particularly useful when looking for a specific target sum and counting the number of subarrays with that sum.

### Steps

1. **Initialize a Dictionary:** Start with an empty dictionary to store prefix sums and their frequencies.

2. **Traverse the Array:** While traversing the array from left to right, maintain a running sum (prefix sum).

3. **Update the Dictionary:** At each step, update the dictionary by incrementing the count for the current prefix sum.

4. **Check for Target Sum:** When looking for a specific target sum, check if the complement of the current prefix sum exists in the dictionary. If it does, increment the count by the frequency of the complement.

### Example

```python
def count_subarrays_with_sum(arr, target_sum):
 prefix_sum = 0
 prefix_sum_count = {0: 1}  # Initialize with a prefix sum of 0 and count 1
 count = 0

 for num in arr:
     prefix_sum += num
     complement = prefix_sum - target_sum

     # Check if complement exists in the dictionary
     if complement in prefix_sum_count:
         count += prefix_sum_count[complement]

     # Update the dictionary with the current prefix sum
     prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

 return count

# Example usage:
arr = [1, 2, 3, 4, 5]
target_sum = 8
result = count_subarrays_with_sum(arr, target_sum)
print("Count of subarrays with sum equal to", target_sum, ":", result)


