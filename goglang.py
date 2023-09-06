from googletrans import Translator
import googletrans

translator = Translator()
result = translator.translate('go',src='en',dest='fr')
print(result)
# print(googletrans.LANGUAGES)