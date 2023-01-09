from googletrans import Translator


translator = Translator()

word = 'Гидра'
text = translator.translate(word, dest='en').text
print(f'перевод: {text}\n')
