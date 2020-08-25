import sys
import parser2

def print_list(parser_module):
	l = parser_module.input_list("строки")
	print(l)

def import_module_in_function():
	import parser2
	l = parser2.input_list("строки")
	print(l)
	
#print_list(parser2)
#print(sys.path)
#print(sys.modules)
#import_module_in_function()
#print(sys.modules)
#import_module_in_function()

for p in sys.path:
	print(p)