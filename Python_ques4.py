# count_characters
def count_characters(text):
    char_frequency = {}
    for char in text:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    return char_frequency

from collections import Counter
def count_characters(text):
    char_frequency = Counter(text)
    return char_frequency
  
text = "hello world"
result = count_characters(text)
print(result)

# Merge Sort 

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
          
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged
  
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
