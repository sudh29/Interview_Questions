# count_characters

def count_characters(text):
    char_frequency = {}
    for char in text:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    return char_frequency

from collections import Counter
def count_characters_1(text):
    char_frequency = Counter(text)
    return char_frequency
  
text = "hello world"
result = count_characters(text)
print(result)

result = count_characters_1(text)
print(result)

# Merge Sort 

def merge(left_arr,right_arr):
    merge_arr = []
    l, r = 0, 0
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            merge_arr.append(left_arr[l])
            l+=1
        else:
            merge_arr.append(right_arr[r])
            r+=1
    merge_arr.extend(left_arr[l:])
    merge_arr.extend(right_arr[r:])
    return merge_arr
    
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)
    
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)

# PUT and PATCH are HTTP methods used in RESTful APIs to update resources. Here's a brief explanation of each:

'''
PUT Method:
The PUT method is used to update a resource or replace it entirely with a new representation. When you send a PUT request to a specific resource endpoint, you're essentially providing the full representation of the resource, and the server updates the resource accordingly. If the resource doesn't exist, it's created.

PUT /api/users/123 HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john.doe@example.com"
}

In this example, a PUT request is sent to update the user with ID 123 with a new name and email. If the user with ID 123 exists, it will be updated with the provided data. If not, a new user will be created with the provided data and ID 123.

PATCH Method:
The PATCH method is used to apply partial modifications to a resource. It's typically used when you want to update only certain fields of a resource without affecting the rest of the resource's representation.

PATCH /api/users/123 HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "name": "Jane Doe"
}

In this example, a PATCH request is sent to update the name of the user with ID 123 to "Jane Doe". Unlike PUT, the PATCH request only contains the fields that need to be updated, and the server applies those changes without affecting other fields or properties of the resource.

Summary:
Use PUT when you want to completely replace the resource or update it with a new representation.
Use PATCH when you want to apply partial modifications to the resource, updating only specific fields.
Both PUT and PATCH methods are idempotent, meaning that multiple identical requests have the same effect as a single request. However, PATCH is more suited for partial updates, while PUT is used for complete replacements.'''






