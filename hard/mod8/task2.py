import pandas as pd

data = pd.read_csv('vacancies_small.csv')


def get_popular_skills(profession):
    profession = profession.lower()
    profession_data = data[data['name'].str.lower().str.contains(profession)]
    skill_counts = profession_data['key_skills'].value_counts().head(5)
    popular_skills = list(zip(skill_counts.index, skill_counts.values))
    return popular_skills


profession = 'программист'
popular_skills = get_popular_skills(profession)
print(popular_skills)
