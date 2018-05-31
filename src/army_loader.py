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
		# 서류준비 입력키
		self.xml_pass = "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D"
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


if __name__ == '__main__':
	main()
