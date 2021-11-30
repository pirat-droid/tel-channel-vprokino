from googletrans import Translator


translator = Translator()
result = translator.translate('Crypto news hungry', src='en', dest='ru')
print(result.text)
