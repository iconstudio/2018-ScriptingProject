import sys
import os
import types

def decorate_p(func):
	def func_wrapper(name):
		return "<p>{0}</p>".format(func(name))
	return func_wrapper

def decorate_strong(func):
	def func_wrapper(name):
		return "<strong>{0}</strong>".format(func(name))
	return func_wrapper

def decorate_div(func):
	def func_wrapper(name):
		return "<div>{0}</div>".format(func(name))
	return func_wrapper

#def get_sentence(name):
#	return "lorem ipsum, {0} dolor sit amet".format(name)

#get_text = decorate_div(decorate_p(decorate_strong(get_sentence)))

@decorate_div
@decorate_p
@decorate_strong
def get_text(name):
  return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("John"))


def reverse(value: int or float and not str):
	result_type = type(value)
	converted = str(value)
	result: str = ""

	for char in reversed(converted):
		result += str(char)
		#print(char)
	
	return result_type(result)


print(reverse(32342486592304))
