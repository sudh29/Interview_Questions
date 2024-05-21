import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'Salary': [50000, 60000, 45000]}

df = pd.DataFrame(data)
print(df)

# Example 1: Filtering Columns
subset_df = df[['Name', 'Age']]
print("Filtered DataFrame:")
print(subset_df)

# Example 2: Adding Rows
new_row = {'Name': 'David', 'Age': 28, 'Salary': 52000}
df = df.append(new_row, ignore_index=True)
print("\nDataFrame with added row:")
print(df)

# Example 3: Reshaping and Merging
melted_df = pd.melt(df, id_vars=['Name'], value_vars=['Age', 'Salary'])
print("\nMelted DataFrame:")
print(melted_df)

# Example 4: Grouping and Aggregation
grouped_df = df.groupby(['Age']).agg({'Salary': 'mean'}).reset_index()
print("\nGrouped and Aggregated DataFrame:")
print(grouped_df)


# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'Salary': [50000, 60000, 45000]}

df = pd.DataFrame(data)
print(df)
# Pivoting the DataFrame
pivoted_df = df.pivot(index='Name', columns='Age', values='Salary')

print("Pivoted DataFrame:")
print(pivoted_df)

# Unpivoting the DataFrame
unpivoted_df = pivoted_df.reset_index().melt(id_vars=['Name'], value_vars=[25, 30, 22], 
                                            var_name='Age', value_name='Salary')

print("\nUnpivoted DataFrame:")
print(unpivoted_df)
