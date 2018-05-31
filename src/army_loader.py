from import_file import *


class army_stick:
	def __init__(self, master):
		self.master = master
		self.xml_pass = "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D"  # 합격 입력키
		self.xml_url = "http://apis.data.go.kr/1300000//bjGiJun/list//bjGiJun/list"
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


class army_roll:
	def __init__(self, master):
		self.master = master
		self.xml_pass = "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D"  # 서류준비 입력키
		self.xml_url = "http://apis.data.go.kr/1300000/gbSeoryu/list/gbSeoryu/list"
		self.loopflag = 1
		self.docs = None
		self.doms = None
		self.seach_key = urllib.parse.quote("공군")

	def open_xml(self):
		try:
			pet_cont = urllib.request.Request(self.xml_url + "?serviceKey=" + self.xml_pass)
		except IOError:
			print("text_error")
			return None
		except urllib.error.URLError as e:
			print(e.reason)
			print(parseString(e.read().decode('utf-8')).toprettyxml())
		except urllib.error.HTTPError as e:
			print("error code = " + e.reason)
			print(parseString(e.read().decode('utf-8')).toprettyxml())
		else:
			with urllib.request.urlopen(pet_cont) as t:
				raw_data = t.read()
				t.close()
				text_dom = parseString(raw_data)
				print(text_dom.toprettyxml())

	def open_window(self):
		self.frame = tkinter.Frame(self.master)
		self.quitButton = tkinter.Button(self.frame, text='Quit', width=25, command=self.close_windows)
		self.quitButton.pack()
		self.frame.pack()

	def close_windows(self):
		self.master.destroy()


def main():
	global wx, wy
	window = tkinter.Tk()
	window.title("army_window")
	window.geometry("960x540+" + str(wx) + "+" + str(wy))
	window.resizable(0, 0)
	window.minsize(960, 540)
	window.maxsize(960, 540)
	Font = font.Font(window, size=12, weight='normal', family='NanumGothic')

	roll = army_roll(window)
	roll.open_xml()

	Caption = tkinter.Label(window, font=Font, text="목록")
	Caption.place(x=wx, y=20)

	button_military = tkinter.Button(window, text="공석 확인", command=None)
	button_military.pack()
	button_military.config(width="18", height="8")
	button_military.place(x=480 - 200, y=80)

	button_path = tkinter.Button(window, text="사회복무 회사 검색", command=None)
	button_path.pack()
	button_path.config(width="18", height="8")
	button_path.place(x=480 + 8, y=80)

	button_milinfo = tkinter.Button(window, text="현역 정보", command=None)
	button_milinfo.pack()
	button_milinfo.config(width="18", height="8")
	button_milinfo.place(x=480 - 200, y=300)

	button_pubinfo = tkinter.Button(window, text="사회복무 정보", command=None)
	button_pubinfo.pack()
	button_pubinfo.config(width="18", height="8")
	button_pubinfo.place(x=480 + 8, y=300)

	window.mainloop()


if __name__ == '__main__':
	main()
