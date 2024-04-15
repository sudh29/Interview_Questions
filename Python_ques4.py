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

# Mocking:
'''Mocking involves replacing parts of your code with mock objects that simulate the behavior of real objects. Mock objects can be configured to return specific values, raise exceptions, or have custom behavior.'''

from unittest.mock import Mock

# Create a mock object
mock_obj = Mock()
# Configure the mock object to return a specific value
mock_obj.method.return_value = 42

# Use the mock object
result = mock_obj.method()
print(result)  # Output: 42

# Patching:
'''Patching is a specific form of mocking that replaces objects or functions in a module with mock objects during the execution of a test. It's commonly used to replace dependencies of the code being tested with mock objects.'''

from unittest import TestCase, mock
from mymodule import function_to_test

class MyTestCase(TestCase):

    @mock.patch('mymodule.dependency')
    def test_function_to_test(self, mock_dependency):
        # Configure the mock dependency
        mock_dependency.return_value = 42

        # Call the function being tested
        result = function_to_test()

        # Assert that the function behaves as expected
        self.assertEqual(result, 42)

'''Monkey patching is a technique used in software development to dynamically modify or extend code at runtime. It involves altering or replacing parts of a program's code, typically functions or methods, with alternative implementations.'''

# Original module code
def original_function():
    return "Original implementation"

# Monkey patching: Replace original_function with a new implementation
def new_function():
    return "Monkey-patched implementation"

# Applying the patch
import module
module.original_function = new_function

# Now calling original_function will execute the monkey-patched implementation
result = module.original_function()
print(result)  # Output: "Monkey-patched implementation"

# Monkey patching and Patching

''' Monkey patching is a general programming technique for dynamically modifying or extending code at runtime.
Patching, in the context of unit testing, refers to the process of replacing objects or functions with mock objects or alternative implementations during testing.
While monkey patching is a more general technique that can be used for various purposes, patching in unit testing is specifically used for isolating code dependencies during testing.'''





