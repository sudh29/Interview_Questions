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

