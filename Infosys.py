# Round 1
#Q1-
my_tiple = [(1,'a'), (4,'d'), (3, 'c'), (2,'b')]
print(my_tiple)
my_tiple.sort(key=lambda x:x[0])
print(my_tiple)

#Q2-
a = "[{{}}]" #-- valid
 
b = "{[}]" #--- invalid

def check_valid_par(ip):
    dic_val = {"(": ")", "{": "}", "[": "]"}
    stack = []
    
    for char in ip:
        if char in dic_val:
            stack.append(char)
        elif not stack or dic_val[stack.pop()] != char:
            return "Invalid"
    
    return "Valid" if not stack else "Invalid"
     
print(check_valid_par(a))
print(check_valid_par(b))

#Q3-
import pandas as pd
# Create the DataFrame
data = {
    'Type': ['x', 'x', 'x', 'x', 'Y', 'Y', 'Y', 'Y', 'z', 'z', 'z'],
    'ID': [123, 123, 123, 123, 567, 567, 567, 567, 890, 890, 890],
    'Salary': [2000, 5000, 7000, 10000, 10000, 12000, 15000, 17000, 8000, 9000, 11000]
}
df = pd.DataFrame(data)
print(df)
# Group by 'Type' and find the second-highest salary for each group
second_highest_salaries = df.groupby('Type')['Salary'].nlargest(2).groupby(level=0).nth(-1)
print("Second-highest salaries for each group:")
print(second_highest_salaries)



'''
df.groupby('Type')['Salary']: It groups the DataFrame df by the 'Type' column and selects the 'Salary' column, creating groups based on unique values in the 'Type' column.

.nlargest(2): For each group created in the previous step, it selects the two largest values in the 'Salary' column. This function effectively identifies the top two salaries within each group.

.groupby(level=0): After selecting the top two salaries within each group, it groups the resulting data by the level 0 index, which corresponds to the first level of the multi-index created by the groupby operation.

.nth(-1): Finally, it retrieves the element at the last position (-1 index) within each group. Since the data is already sorted in descending order (largest to smallest salaries), the element at index -1 corresponds to the second-largest salary within each group.

In summary, the query df.groupby('Type')['Salary'].nlargest(2).groupby(level=0).nth(-1) effectively identifies the second-highest salary within each group defined by the 'Type' column in the DataFrame.
'''

#Round2








