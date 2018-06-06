from import_file import *
import petron_loader as pet


# 현재 장면
Scene = 0
data_messages = []

image_async = None
try:
	_army = "https://www.mma.go.kr/contents.do?mc=mma00020" + "{0}".format(46 + 1)
	with urllib.request.urlopen(_army) as u:

		raw_data = u.read()
		print(u.info())
except tkinter.TclError:
	print("happen")

try:
	if __name__ == "__main__":
		print("begins")
		pet.main()
	else:
		raise RuntimeError
except RuntimeError:
	print("Program must be run by Main.")
