d = {i: i*2 for i in range(1000000)}
k = 9999
# print(d)
# print(k)
res=d.get(k,None)
if res:
  print("Available")
else:
  print("Not Avaiable")

# fibonacci series
# 0,1,1,2,3,5,8,13

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

def fibonacci(n):
    if n <= 1:
        return [0] if n == 0 else [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

d = {"a": {"b": {"c": "hey", "d": {"e": "Bye"}}}}

d = {"a": {"b": {"c": "hey", "d": {"e": "Bye"}}}}
# print("val",d.keys())
inp = "a.b"
# op = {"c": "hey", "d": {"e": "Bye"}}
inp1 = "a.b.c"
# op = "hey"
inp2 = "a.c"
# op = "Not available"


def find_val(dic_val, target):
  n = len(target)
  for i in range(n):

    val = dic_val.get(target[i], None)
    if i == n - 1:
        if val:
            print(val)
        else:
          print("Not Available")
        return
    if val:
      find_val(val, target[i + 1:])
    else:
        return


(find_val(d, inp.split('.')))
(find_val(d, inp1.split('.')))
(find_val(d, inp2.split('.')))

def print_nested_dict_values(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print_nested_dict_values(value)
        else:
            print(value)


import pandas as pd

df = pd.DataFrame([[1,2,3], ["A", "B", "C"]], columns=["Col1", "Col2", "Col3"])

# #  Find "B" in column
print(df)

res = df[df["Col2"]=='B']
print(res)

