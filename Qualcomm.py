Q1 Write a Program to combine two different dictionaries. While combining, if you find the same keys, you can add the values of these same keys. 
Output the new dictionary

Ans:
d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}

{'key3': 200, 'key2': 200, 'key1': 250, 'key4': 300}

d3 = {}

for k,v in d1.items():
	d3[k] = v
	
for k,v in d2.items():
	if k in d3.keys():
		d3[k] += v
	else:
		d3[k] = v
		
print(d3)

Q2: Given an array A[] consisting of only 0s, 1s, and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first,
then all 1s and all 2s in last.
 
Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}
Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}
Ans:

v0,v1,v2 = 0 , 0 ,0

for i in array:
	if i==0:
		v0+=1
	elif i==1:
		v1+=1
	elif i==2:
		v2+=1
for i in range(len(array)):
	if v0>0:
		array[i]=0
		v0-=1
	elif v1>0:
		array[i]=1
		v1-=1
	elif v2>0:
		array[i]=2
		v2-=1

arr_size = len(arr)
low = 0
high = arr_size - 1
mid = 0
while mid <= high:
    if arr[mid] == 1:
        mid = mid + 1
    elif arr[mid] == 2:
        arr[mid], arr[high] = arr[high], arr[mid]
        high = high - 1
    else:
        arr[low], arr[mid] = arr[mid], arr[low]
        low = low + 1
        mid = mid+1
print(arr)

Q3: Python Program to Print the Fibonacci sequence
Ans: 
def fab_series(arr,n):  
    next = arr[-1]+arr[-2]
    while next <= n:
        arr.append(next)
        next = arr[-1]+arr[-2]
    return arr
        
# ip = 1,1,2,3,5,8

arr = [1,1]
arr =  fab_series(arr,8)
print(arr)

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

Q4: "Can you extract the date time string from my string 16:12:45:0004 Mon 27 2024" --> use reg expression
Ans:
from datetime import datetime
# Input string
input_string = "16:12:45:0004 Mon 27 2024"
# Define the format of the input string
date_format = "%H:%M:%S:%f %a %d %Y"
# Parse the input string into a datetime object
parsed_datetime = datetime.strptime(input_string, date_format)
print(parsed_datetime)

#########################

import re
from datetime import datetime
# Input string
input_string = "16:12:45:0004 Mon 27 2024"
# Define a regular expression pattern to match the date and time components
pattern = r'(\d{2}):(\d{2}):(\d{2}):(\d{4}) (\w{3}) (\d{2}) (\d{4})'
# Use regex to extract date and time components
match = re.match(pattern, input_string)
if match:
    # Extract date and time components
    hour, minute, second, microsecond, weekday, day, year = match.groups()
    print(hour, minute, second, microsecond, weekday, day, year)
else:
    print("Invalid input format")

Q5:
Program
number1 = 5
number2 = 4
# Add two numbers
sum = number1 + number2
# Display the sum of the two numbers
print('The sum of the two numbers is:' sum)		
Ans:		
num1 = input('Enter first number: ')   '15'
num2 = input('Enter second number: ')  '10'
sum = num1 + num2  
print('The sum of the numbers is', sum)		'1510'


Q6: Given N eggs and K floors, the task is to find the minimum number of trials needed, in the worst case, to find the floor below which all floors are safe.
A floor is safe if dropping an egg from it does not break the egg. Please refer n eggs and k floors for more insight
n=2
floors=10
Ans: 4

Q7: Git Commands
Ans: 
git init
git config 
email 
password
git pull 
git push 
git rebase 
git branch -b branch_name
git -d branch_name 
git checkout branch_name
git clone

Q8: Example of inner join on three table
Ans: 
SELECT
    o.order_id,
    o.order_date,
    c.customer_name,
    c.address,
    c.city,
    c.country,
    p.product_name,
    p.unit_price,
    p.category,
    o.quantity
FROM
    orders o
INNER JOIN
    customers c ON o.customer_id = c.customer_id
INNER JOIN
    products p ON o.product_id = p.product_id;


Q9: Class A: Define to get 2 variable from user, Class: Perform Math operation on those two variable in Class A... Using OOPS concept to impalement this 
Ans: 
class A:
    def __init__(self,ip1,ip2):
        self.ip1=ip1
        self.ip2=ip2
        
class B(A):
    def __init__(self,ip1,ip2):
        A.__init__(self,ip1,ip2)
        
    def operation(self):
        return self.ip1 +self.ip2

ip_user = int(input())
ip2_user = int(input())
print(ip_user,ip2_user)

b_obj = B(ip_user,ip2_user)
print(b_obj.operation())

Q10: 
Ans:
arr = np.array([1.0, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(arr.dtype)

Q11:
#code
print("Solve")
n=5000
ans=[]
for i in range(n):
    if i%7==0 and i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1:
        ans.append(i)
        if len(ans)==10:
            break
print(ans)

def test_array_length(array, expected_length):
    actual_length = len(array)
    assert actual_length == expected_length, f"Array length mismatch: expected {expected_length}, got {actual_length}"

expected_length = 10

test_array_length(ans, expected_length)

import unittest

class TestArrFunction(unittest.TestCase):
    def test_arr_len(self):
        self.assertEqual(len(ans), 10)
        
test_obj = TestArrFunction()
test_obj.test_arr_len()

Q12:
Puzzle

Q13:
Puzzle



