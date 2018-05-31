from import_file import *

window = None
buttons = dict()

wx = int((1920 - 960) * 0.5)
wy = int((1080 - 540) * 0.5)


class pet_cont:
	def __init__(self, master):
		self.master = master
		self.xml_pass = "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D"  # 복무기관 입력키
		self.xml_url = "http://apis.data.go.kr/1300000/bmggJeongBo/list"
		self.loopflag = 1
		self.docs = None
		self.doms = None
		self.search_key = urllib.parse.quote("경남")

	def open_xml(self):
		# +"&numOfRows=10&pageSize=10&pageNo=1&startPage=1" 이건 나중에 써보고 다시 편집
		try:
			pet_null = urllib.request.Request(self.xml_url + "?serviceKey=" + self.xml_pass)
		except IOError:
			print("null_error")
			return None
		except urllib.error.URLError as e:
			print(e.reason)
			print(parseString(e.read().decode('utf-8')).toprettyxml())
		except urllib.error.HTTPError as e:
			print("error code = " + e.reason)
			print(parseString(e.read().decode('utf-8')).toprettyxml())
		else:
			with urllib.request.urlopen(pet_null) as t:
				raw_data = t.read()
				t.close()
				army_dom = parseString(raw_data)
				row = army_dom.childNodes
				pry = row[0].childNodes
				head = pry[0].childNodes
				cla = pry[1].childNodes
				print("header")
				for i in head:
					print(i)
				print("body")
				for i in cla:
					print(i)

	def open_window(self):
		self.frame = tkinter.Toplevel(self.master)
		self.quitButton = tkinter.Button(self.frame, text='Quit', width=25, command=self.close_windows)
		self.quitButton.pack()

	def close_windows(self):
		self.master.destroy()


class pet_null:
	frame = None
	quitButton = None

	def __init__(self, master):
		self.master = master
		self.xml_pass = "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D"  # 복무공석 입력키
		self.xml_url = "http://apis.data.go.kr/1300000/bistGongseok/list/bistGongseok/list"
		self.loopflag = 1
		self.docs = None
		self.doms = None
		self.search_key = urllib.parse.quote("경남")

	def open_xml(self):
		# +"&numOfRows=10&pageSize=10&pageNo=1&startPage=1" 이건 나중에 써보고 다시 편집
		try:
			pet_null = urllib.request.Request(self.xml_url + "?serviceKey=" + self.xml_pass)
		except IOError:
			print("null_error")
			return None
		except urllib.error.URLError as e:
			print(e.reason)
			print(parseString(e.read().decode('utf-8')).toprettyxml())
		except urllib.error.HTTPError as e:
			print("error code = " + e.reason)
			print(parseString(e.read().decode('utf-8')).toprettyxml())
		else:
			with urllib.request.urlopen(pet_null) as t:
				raw_data = t.read()
				t.close()
				army_dom = parseString(raw_data)
				row = army_dom.childNodes
				pry = row[0].childNodes
				head = pry[0].childNodes
				cla = pry[1].childNodes
				print("header")
				for i in head:
					print(i)
				print("body")
				for i in cla:
					print(i)

	def open_window(self):
		self.frame = tkinter.Frame(self.master)
		self.quitButton = tkinter.Button(self.frame, text='Quit', width=25, command=self.close_windows)
		self.quitButton.pack()
		self.frame.pack()

	def close_windows(self):
		self.master.destroy()


def buttons_show_all():
	global buttons
	component_pack(buttons["military"])
	component_pack(buttons["milinfo"])
	component_pack(buttons["path"])
	component_pack(buttons["pubinfo"])
	component_pack(buttons["calculator"])


def buttons_hide_all():
	global buttons
	component_hide(buttons["military"])
	component_hide(buttons["milinfo"])
	component_hide(buttons["path"])
	component_hide(buttons["pubinfo"])
	component_hide(buttons["calculator"])


def main():
	global window, wx, wy, global_font
	window = tkinter.Tk()
	window.title("Petron_window")
	window.geometry("960x540+" + str(wx) + "+" + str(wy))
	window.resizable(0, 0)
	window.minsize(960, 540)
	window.maxsize(960, 540)
	global_font = font.Font(window, size=12, weight='normal', family='NanumGothic')

	roll = pet_cont(window)
	roll.open_xml()

	Caption = tkinter.Label(window, font=global_font, text="목록")
	Caption.place(x=wx, y=20)

	buttons["military"] = make_button(window, "현역 판정 검사", 280, 80, "18", "7", buttons_hide_all)
	buttons["milinfo"] = make_button(window, "현역 정보", 280, 300, "18", "7")
	buttons["path"] = make_button(window, "훈련소 가는 길", 488, 80, "18", "7")
	buttons["pubinfo"] = make_button(window, "사회 복무 정보", 488, 300, "18", "7", roll.open_window)
	buttons["calculator"] = make_button(window, "근무 일자\n계산", 8, 442, "10", "3")

	window.mainloop()


if __name__ == '__main__':
	main()
