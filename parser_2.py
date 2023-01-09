# Картинки всех созвездий - https://naturenoon.com/star-constellations-names-meanings/

import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import process
from openpyxl import load_workbook

# Посылаем запрос на сайт
url = 'https://naturenoon.com/star-constellations-names-meanings/'
response = requests.get(url)
html = response.text

# Достаём все ссылки
soup = BeautifulSoup(html, 'html.parser')
links = [link.find('img').get('src') for link in soup.find('div', class_='entry-content').find_all('figure', class_='wp-block-image size-full')]

excel_constellations = [
    "Hydra",
    "Virgo",
    "Big Dipper",
    "Keith",
    "Oat flakes",
    "From Eri",
    "Pegasus",
    "The Dragon",
    "centaur",
    "Aquarius",
    "Dragonfly",
    "a lion",
    "Bootes",
    "Fish",
    "Sagittarius",
    "Swan",
    "Taurus",
    "Giraffe",
    "Andromeda",
    "Stern",
    "Auriga",
    "Eagle",
    "snake[6]",
    "Perseus",
    "Cassiopeia",
    "Orion",
    "Cepheus",
    "Lynx",
    "Scales",
    "Twins",
    "Cancer",
    "Sail",
    "Scorpio",
    "Keel",
    "Unicorn",
    "Sculptor",
    "Phoenix",
    "Hounds Dogs",
    "Aries",
    "Capricorn",
    "Bake",
    "Veronica's hair",
    "Big Dog",
    "Pavlin",
    "Crane",
    "Wolf",
    "Sextant",
    "Toucan",
    "Indian",
    "Octant",
    "Hare",
    "Lira",
    "A cup",
    "Pigeon",
    "Chanterelle",
    "Ursa Minor",
    "Telescope",
    "Times",
    "Painter",
    "Southern Fish",
    "Southern Hydra",
    "Pump",
    "Altar",
    "Small Lion",
    "Compass",
    "Microscope",
    "Bird of Paradise",
    "Lizard",
    "Dolphin",
    "Crow",
    "Small Dog",
    "golden fish",
    "Northern Crown",
    "Square",
    "table mountain",
    "Flying fish",
    "Fly",
    "Triangle",
    "Chameleon",
    "South Crown",
    "Incisor",
    "Network",
    "Southern Triangle",
    "Shield",
    "Compass",
    "Arrow",
    "Small Horse",
    "South Cross",
]

best_matches = []
for constellation in excel_constellations:
    all_5_matches = process.extract(constellation, links, limit=5)
    best_probability = all_5_matches[0][1]
    best_match = [i[0] for i in all_5_matches if i[1] == best_probability]
    best_matches.append(best_match)

excel_file = load_workbook('output.xlsx')
sheet = excel_file.active
for i in range(2, 89+1):
    sheet[f'K{i}'] = '; '.join(best_matches[i-2])
excel_file.save('output.xlsx')
