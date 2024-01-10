import pandas as pd

df = pd.read_csv('vacancies_small.csv')
filtered_df = df[(df['area_name'].str.contains('Екатеринбург', case=False)) & (df['salary_from'] > 0)]
sorted_df = filtered_df.sort_values(by='salary_from', ascending=False)
print(sorted_df['name'].tolist())
