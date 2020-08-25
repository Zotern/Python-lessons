import sys
DEFAULT_TYPE = str

def input_list(typename, etype=None):
	"""Получить список разделенных запятой."""
	result = input("Введите список %s, разделенных запятыми: " % typename)
	if etype is not None:
		try:
			result = [etype(x.strip()) for x in result]
		except ValueError:
			print("Ошибка ввода.", file=sys.stderr)
			exit(1)
	return result

print(__name__, "Module is loaded")

def import_module_in_function():
	import parser
	l = parser_module.input_list("строки")
	