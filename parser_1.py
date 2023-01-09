# Таблица созвездий звёздного неба - https://ru.m.wikipedia.org/wiki/Список_созвездий_по_площади

# Загрузка данных в Excel - https://tonais.ru/library/zapis-dataframe-v-list-excel
# Загрузка изображений в Excel - https://docs-python.ru/packages/modul-openpyxl/dobavlenie-izobrazhenij/

import requests
import pandas
from bs4 import BeautifulSoup


# Посылаем запрос на сайт
response = requests.get('https://ru.m.wikipedia.org/wiki/Список_созвездий_по_площади')
html = response.text

# Достаём все теги строк таблицы
soup = BeautifulSoup(html, 'html.parser')
table_rows = soup.find('table').find('tbody').find_all('tr')

# Преобразуем все теги строк в список со строками
result = [row.text.split('\n') for row in table_rows]
result[0].append('')

# Создаём датасет
data = pandas.DataFrame(columns=result[0], data=result[1:])

# Создаём объект записи в Excel файл
writer = pandas.ExcelWriter('output.xlsx')

# Записываем данные в Excel и сохраняем
data.to_excel(writer)
writer.save()
