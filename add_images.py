from time import sleep
from openpyxl import load_workbook
import requests
from openpyxl.drawing.image import Image

for i in range(2, 89+1):
    excel_file = load_workbook('output.xlsx')
    sheet = excel_file.active
    url = sheet[f'K{i}'].value
    print(f'{round(i / 89 * 100)}%')

    # получаем объект изображения
    img = requests.get(url).content
    open('image.png', 'wb').write(img)
    excel_image = Image(open('image.png', 'rb'))

    # меняем размеры изображения
    excel_image.width *= 0.2
    excel_image.height *= 0.2

    # добавляем объект изображение в ячейку
    sheet.add_image(excel_image, f'L{i}')

    # сохраняем
    excel_file.save('output.xlsx')
    sleep(1)
