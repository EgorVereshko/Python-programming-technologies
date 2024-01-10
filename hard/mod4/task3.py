from bs4 import BeautifulSoup
import json

# Замените "html_content" на HTML-код страницы, с которой хотите работать
html_content = """
<div class="vacancy-title">Очень крутой разработчик</div>
<div class="vacancy-title">30000 ₽</div>
<span class="vacancy-description-list-item">от 3 до 6 лет</span>
<div class="vacancy-company-name">Очень крутая компания</div>
<div data-qa="vacancy-description">Бла-бла-бла бла-бла бла-бла-бла БЛА-БЛА бла Бла-бла-бла</div>
<div class="vacancy-section">
    <p>Python</p>
    <p>HTML</p>
    <p>Django</p>
    <p>Docker</p>
</div>
<span class="vacancy-creation-time-redesigned">18 авг. 2023</span>
"""

# Создаем объект BeautifulSoup для парсинга данных
soup = BeautifulSoup(html_content, 'html.parser')

# Ищем и извлекаем нужные данные
vacancy = soup.find('div', {'class': 'vacancy-title'}).text
salary = soup.find_all('div', {'class': 'vacancy-title'})[1].text.split(' ₽')[0]
experience = soup.find('span', {'class': 'vacancy-description-list-item'}).text
company = soup.find('div', {'class': 'vacancy-company-name'}).text
description = soup.find('div', {'data-qa': 'vacancy-description'}).text
skills = ', '.join([skill.text for skill in soup.find('div', {'class': 'vacancy-section'}).find_all('p')])
created_at = soup.find('span', {'class': 'vacancy-creation-time-redesigned'}).text

# Обрабатываем полученные данные
experience = ''.join(filter(str.isdigit, experience))  # оставляем только цифры

# Формируем словарь
result = {
    "vacancy": vacancy,
    "salary": salary,
    "experience": experience,
    "company": company,
    "description": description,
    "skills": skills,
    "created_at": created_at
}

# Преобразуем словарь в JSON и выводим
print(json.dumps(result, ensure_ascii=False))