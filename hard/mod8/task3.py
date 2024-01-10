import pandas as pd

df = pd.read_csv('vacancies_small.csv')

df = df[df['salary_currency'] == 'RUR']
df['average_salary'] = (df['salary_from'] + df['salary_to']) / 2
average_salary_by_city = df.groupby('area_name')['average_salary'].mean().sort_values(ascending=False)
result = average_salary_by_city.to_dict()

print(result)
