import openpyxl
from googletrans import Translator


excel_file = openpyxl.load_workbook('output.xlsx')
sheet = excel_file['Sheet1']
translator = Translator()
for i in range(2, 89+1):
    text_rus = sheet[f"D{i}"].value
    text_eng = translator.translate(text_rus, dest='en').text
    sheet[f'E{i}'] = text_eng
excel_file.save('output.xlsx')
