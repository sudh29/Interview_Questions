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
The PUT method is used to update a resource or replace it entirely with a new representation. When you send a PUT request to a specific resource endpoint,
you're essentially providing the full representation of the resource, and the server updates the resource accordingly. If the resource doesn't exist,
it's created.

PUT /api/users/123 HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john.doe@example.com"
}

In this example, a PUT request is sent to update the user with ID 123 with a new name and email. If the user with ID 123 exists, it will be updated with the provided data. If not, a new user will be created with the provided data and ID 123.

PATCH Method:
The PATCH method is used to apply partial modifications to a resource. It's typically used when you want to update only certain fields of a resource 
without affecting the rest of the resource's representation.

PATCH /api/users/123 HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "name": "Jane Doe"
}

In this example, a PATCH request is sent to update the name of the user with ID 123 to "Jane Doe". Unlike PUT, the PATCH request only contains the fields
that need to be updated, and the server applies those changes without affecting other fields or properties of the resource.

Summary:
Use PUT when you want to completely replace the resource or update it with a new representation.
Use PATCH when you want to apply partial modifications to the resource, updating only specific fields.
Both PUT and PATCH methods are idempotent, meaning that multiple identical requests have the same effect as a single request. However, PATCH is more suited 
for partial updates, while PUT is used for complete replacements.'''

# Mocking:
'''Mocking involves replacing parts of your code with mock objects that simulate the behavior of real objects. Mock objects can be configured to return 
specific values, raise exceptions, or have custom behavior.'''

from unittest.mock import Mock

# Create a mock object
mock_obj = Mock()
# Configure the mock object to return a specific value
mock_obj.method.return_value = 42

# Use the mock object
result = mock_obj.method()
print(result)  # Output: 42

# Patching:
'''Patching is a specific form of mocking that replaces objects or functions in a module with mock objects during the execution of a test. It's commonly used
to replace dependencies of the code being tested with mock objects.'''

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

'''Monkey patching is a technique used in software development to dynamically modify or extend code at runtime. It involves altering or replacing parts of 
a program's code, typically functions or methods, with alternative implementations.'''

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
Patching, in the context of unit testing, refers to the process of replacing objects or functions with mock objects or alternative implementations during
testing.
While monkey patching is a more general technique that can be used for various purposes, patching in unit testing is specifically used for isolating 
code dependencies during testing.'''

# By Reference or By Value
'''
In Python, arguments are passed by object reference. This means that when you pass a variable to a function, you are actually passing a reference to the
object that the variable refers to, not a copy of the object itself.

Passing by Object Reference:
When you pass an immutable object (e.g., integers, strings, tuples) to a function, changes made to the object inside the function will not affect the original object.
When you pass a mutable object (e.g., lists, dictionaries, sets) to a function, changes made to the object inside the function will affect the original object.
'''
def modify_list(lst):
    lst.append(4)  # This will modify the original list

def modify_int(num):
    num = num + 1  # This will not modify the original integer

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

my_num = 5
modify_int(my_num)
print(my_num)   # Output: 5

'''
In the example above:
modify_list modifies the original list, demonstrating that lists are mutable and changes made inside the function affect the original list.
modify_int increments the value of num by 1, but it doesn't affect the original integer. This is because integers are immutable, and reassigning num inside
the function creates a new integer object.

In summary, while Python does not pass arguments by reference in the traditional sense, it passes them by object reference, meaning that changes to
mutable objects passed to functions can affect the original objects, while changes to immutable objects do not.'''

# Method overloading and Method overriding

'''
Method Overloading:
Method overloading refers to defining multiple methods in a class with the same name but different parameters or argument lists. The behavior of the method 
is determined by the number or type of arguments passed to it. However, Python does not support method overloading in the traditional sense like some 
other programming languages such as Java or C++.

Instead, you can achieve a form of method overloading in Python by using default parameter values or variable-length argument lists (*args and **kwargs).
This allows a single method to handle different argument types or numbers.'''

class MyClass:
    def my_method(self, a, b=None):
        if b is None:
            # handle the case when only 'a' is passed
            print(a)
        else:
            # handle the case when both 'a' and 'b' are passed
            print(a, b)

obj = MyClass()
obj.my_method(1)        # Output: 1
obj.my_method(1, 2)     # Output: 1 2

'''
Method Overriding:
Method overriding refers to defining a method in a subclass that has the same name as a method in the superclass. The method in the subclass overrides the
method in the superclass, and the behavior of the overridden method is specific to the subclass.'''

class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.make_sound()  # Output: Bark
cat.make_sound()  # Output: Meow

'''
In summary, while Python does not support method overloading in the traditional sense, you can achieve similar functionality using default parameters
or variable-length argument lists. Method overriding, on the other hand, is supported in Python and allows subclasses to provide their own implementations
of methods defined in the superclass.'''











