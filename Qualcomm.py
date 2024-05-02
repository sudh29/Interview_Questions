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


Q14: 
There are 3 baskets. one of them have apples, one has oranges only and the other has mixture of apples and oranges. The labels on their baskets always lie.
(i.e. if the label says oranges, you are sure that it doesn't have oranges only,it could be a mixture) The task is to pick one basket and pick only one
fruit from it and then correctly label all the three baskets.

A,  0,	M
 
M,  A,	0	

Ans -  Pick from mix label one

Q15:
You have 8 balls. One of them is defective and weighs less than others. You have a balance to measure balls against each other.
In 2 weighings how do you find the defective one?

Ans - 
Case 1. First put aside 2 balls. From remaining 6, put 3-3 on each side. 
If they weigh unequal, select the side which weighs less. Remove 1 ball from that. 
Put 1-1 on each side. If they weigh equal, the one in your hand is the defective ball. 
Otherwise, the side which weighs less has the defective ball. 

Case 2. If 3-3 balls weigh equal, take another two balls and put 1-1 on each side. Whichever weighs less, is the defective ball.

Q16:
You have 5 jars of pills. Each pill weighs 10 gram, except for contaminated pills contained in one jar, where each pill weighs 9 gm. 
Given a scale, how could you tell which jar had the contaminated pills in just one measurement?

Ans - 
Step 1: Take out 1 pill from jar 1, 2 pills from jar 2, 3 pills from jar 3, 4 pills from jar 4 and 5 pills from jar 5.
Step 2: Put all these 15 pills on the scale. The correct weight is 150 (15*10). But one of the jars has contaminated pills. 
So the weight will definitely be less than 150.
Step 3: If the weight is 149 then jar 1 has contaminated pills because there is only one contaminated pill. If the weight is 148 then jar 2,
if the weight is 147 then jar 3, if 146 then jar 4, if 145 then jar 5.

Q17: Write a program (recursive) to print given number in binary format.
Ans:
def decimal_to_binary(n,arr):
    if n > 1:
        decimal_to_binary(n // 2,arr)
    arr.append(str(n % 2))

# Example usage
decimal_number = 10
print(f"Binary representation of {decimal_number}: ", end='')
ans = []
decimal_to_binary(decimal_number,ans)
print(''.join(ans))

Q18: Compare two large array of alphabets and return true if each alphabet has same frequency in both the arrays, else false.
Ans:

from collections import Counter

def compare_alphabet_arrays(arr1, arr2):
    # freq1 = Counter(arr1)
    # freq2 = Counter(arr2)
    
    freq1 = {}
    for i in arr1:
        freq1[i] = freq1.get(i,0)+1
    freq2 = {}
    for i in arr2:
        freq2[i] = freq2.get(i,0)+1
    
    
    # Check if the frequencies of all alphabets are the same in both arrays
    return freq1 == freq2

# Example usage
array1 = ['a', 'b', 'c', 'a', 'a', 'b']
array2 = ['b', 'a', 'a', 'c', 'b', 'a']
print(compare_alphabet_arrays(array1, array2))  # Output: True

array3 = ['a', 'b', 'c', 'a', 'a', 'b']
array4 = ['b', 'a', 'a', 'c', 'b']
print(compare_alphabet_arrays(array3, array4))  # Output: False

