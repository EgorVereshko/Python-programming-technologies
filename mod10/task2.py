import requests
from bs4 import BeautifulSoup

url = "http://www.columbia.edu/~fdc/sample.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

subheadings = soup.find_all('h3')
subheading_list = [subheading.text for subheading in subheadings]

print(subheading_list)
