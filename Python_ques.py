# Take sum of list using lambda fn.
from functools import reduce
new=[1,2,3,4,5]
res = reduce(lambda a,b : a+b,new)
print(res)

# swap two number without using two numbers
a=7
b=12
print(a,b)
a=a+b #19
b=a-b #7
a=a-b #12
print(a,b)

# Capitalize first letter
str_a = "sudhanshu"
print(str_a)
str_b=str_a.capitalize()
print(str_b)

# Difference in sort and sorted
'''The sorted() function returns a sorted list of the specific iterable object.
    The sort() method sorts the list.'''


# Delete file in linux using python
import os
os.remove("/tmp/<file_name>.txt")

# Show hidden file in linux
# ls -a

# Random integer in a range
import random
num = random.randint(0, 9)
print(num)


# Command line arguments in python
import sys
n = len(sys.argv)
print("Total arguments passed:", n)
print("\nName of Python script:", sys.argv[0])
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")    
# Run: python3 abc.py 2 3 4 5


# Top command is used to show the Linux processes.

# *arg =[] and *kwargs = {}

# Custom exception
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return(repr(self.value))
 
try:
    raise(MyError(3*2))
except MyError as error:
    print('A New Exception occurred: ', error.value)

''' Git Fetch is the command that tells the local repository 
    that there are changes available in the remote repository without 
    bringing the changes into the local repository. Git Pull on the 
    other hand brings the copy of the remote directory changes into 
    the local repository.'''

# git pull = git fetch + git merge

''' git pull and git rebase are not interchangeable, but they are closely
    connected. git pull fetches the latest changes of the current branch 
    from a remote and applies those changes to your local copy of the branch.
    Generally this is done by merging, i.e. the local changes are merged
    into the remote changes. So git pull is similar to git fetch & git merge.
    
    Rebasing is an alternative to merging. Instead of creating a new commit 
    that combines the two branches, it moves the commits of one of the branches
    on top of the other.You can pull using rebase instead of merge (git pull --rebase).
    The local changes you made will be rebased on top of the remote changes, 
    instead of being merged with the remote changes.'''

# OS version check linux command
# lsb_release -a

# CPU details linux command
# lscpu

'''JSON is a pure string written in a convention format, which does not have any characteristics of data structure
. ... Python's dictionary key can be any hash object, and JSON can only be a string. 
The Python dict string uses single quotation marks, and JSON enforces double quotation marks. 
You can nest tuple in Python dict.
JSON dictionary must have a time complexity of O(n)
Python dictionary, and now finding a key has a time complexity of O(1)
JSON is a data format (a string), Python dictionary is a data structure (in-memory object).
If you need to exchange data between different (perhaps even non-Python) processes then you could use JSON format to serialize your Python dictionary.
'''




'''A class method receives the class as an implicit first argument, just like an instance method receives the instance 
A class method is a method that is bound to the class and not the object of the class.
It can modify a class state that would apply across all the instances of the class. 
For example, it can modify a class variable that will be applicable to all the instances

A static method does not receive an implicit first argument.
A static method is also a method that is bound to the class and not the object of the class.
This method can???t access or modify the class state

Instance Method:
+ Can modify object instance state
+ Can modify class state

Class Method:
- Can't modify object instance state
+ Can modify class state

Static Method:
- Can't modify object instance state
- Can't modify class state
'''

class A(object):
    def foo(self, x):
        print(f"executing foo({self}, {x})")

    @classmethod
    def class_foo(cls, x):
        print(f"executing class_foo({cls}, {x})")

    @staticmethod
    def static_foo(x):
        print(f"executing static_foo({x})")

a = A()
a.foo(1)
a.class_foo(1)
A.class_foo(1)
'''With staticmethods, neither self (the object instance) nor cls (the class) is implicitly passed as the first argument.
They behave like plain functions except that you can call them from an instance or the class:'''
a.static_foo(1)
A.static_foo('hi')
    











