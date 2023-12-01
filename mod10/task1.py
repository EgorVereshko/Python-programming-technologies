import requests
import pprint


url = "https://swapi.dev/api/starships/?search=Millennium%20Falcon"
response = requests.get(url)
data = response.json()
pilot_urls = data['results'][0]

pilots_info = []
for pilot_url in pilot_urls['pilots']:
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()
    pilot_info = {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'weight': pilot_data['mass'],
        'homeworld_url': pilot_data['homeworld'],
        'homeworld_name': requests.get(pilot_data['homeworld']).json()['name']
    }
    pilots_info.append(pilot_info)

result = ({
    'name': pilot_urls['name'],
    'max_speed': pilot_urls['max_atmosphering_speed'],
    'class': pilot_urls['starship_class'],
    'pilots': pilots_info
})

pprint.PrettyPrinter().pprint(result)
