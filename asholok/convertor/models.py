import os
import sys
PATH_TO_RULES = '/'.join(str(os.path.abspath(__file__)).split('/')[:-1])+'/lib'
sys.path.insert(0,PATH_TO_RULES)
from conv import NumToWord
import localization


class Engine(object):
	info = 'Please input number like 23448592.23'
	langs_available = [lang for lang in localization.languages]
	currencies_available = localization.available_currenceis

	def __init__(self, language=None, currency=None, number=None):
		if language:
			convertor = NumToWord(language, currency)
			self.result = convertor.convert(number)
		else:
			self.result = language
		self.number = number

# Create your models here.

x = NumToWord('ua', 'uah')

print x._lang_family