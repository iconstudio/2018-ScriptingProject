from import_file import *

window = None
buttons = dict()



class petron_component:
	frame = None
	button_quit = None
	xml_url = ""
	xml_pass = ""
	search_key = ""

	def __init__(self, master):
		self.master = master
		self.loopflag = 1
		self.docs = None
		self.doms = None
		self.childbody = None
		self.childhead = None
		self.nextpage = 1

	def xml_connect(self, url, passcode, key=""):
		self.xml_url = url
		self.xml_pass = passcode
		self.search_key = key

		# +"&numOfRows=10&pageSize=10&pageNo=1&startPage=1" 이건 나중에 써보고 다시 편집
		try:
			pet_null = urllib.request.Request(self.xml_url + "?serviceKey=" + self.xml_pass
											  +"&numOfRows={0}&pageSize={1}&pageNo={2}&startPage=1".format(1000, 1000, self.nextpage)) # 이건 나중에 키 입력을 통해 변경할 수 있도록
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
				test_tree = ElementTree.ElementTree(file= t)
				self.childbody = test_tree.getroot()

	def window(self, newtitle:str):
		global px, py
		self.frame = tkinter.Toplevel(self.master)
		self.frame.title(newtitle)
		self.frame.geometry("480x540+" + str(px) + "+" + str(py))
		self.frame.resizable(0, 0)
		self.frame.minsize(480, 540)
		self.frame.maxsize(480, 540)

		self.button_quit = make_button(self.frame, "종료", 208, 490, "6", "1", self.__del__)
		# self.button_quit = tkinter.Button(self.frame, text='Quit', width=25, command=self.__del__)
		# self.button_quit.pack()
		return self.frame

	def __del__(self):
		self.frame.destroy()


class pet_null:
	frame = None
	button_quit = None

	def __init__(self, master):
		self.master = master
		self.xml_pass = "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D"  # 복무공석 입력키
		self.xml_url = "http://apis.data.go.kr/1300000/bistGongseok/list/bistGongseok/list"
		self.loopflag = 1
		self.docs = None
		self.doms = None
		self.search_key = urllib.parse.quote("경남")
		self.childbody = None
		self.nextpage = 1




	def open_xml(self):
		# +"&numOfRows=10&pageSize=10&pageNo=1&startPage=1" 이건 나중에 써보고 다시 편집
		try:
			pet_null = urllib.request.Request(self.xml_url + "?serviceKey=" + self.xml_pass
											  + "&numOfRows={0}&pageSize={1}&pageNo={2}&startPage=1".format(1000, 1000,self.nextpage))
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
				test_tree = ElementTree.ElementTree(file=t)
				self.childbody = test_tree.getroot()
			# with urllib.request.urlopen(pet_null) as t:
			#	raw_data = t.read()
			#	t.close()
			#	army_dom = parseString(raw_data)
			#	row = army_dom.childNodes
			#	pry = row[0].childNodes
			#	head = pry[0].childNodes
			#	cla = pry[1].childNodes#
			#	print("header")
			#	for i in head:
			#		print(i)
			#	print("body")
			#	for i in cla:
			#		print(i)

	def window(self, newtitle:str):
		global px, py
		self.frame = tkinter.Toplevel(self.master)
		self.frame.title(newtitle)
		self.frame.geometry("480x540+" + str(px) + "+" + str(py))
		self.frame.resizable(0, 0)
		self.frame.minsize(480, 540)
		self.frame.maxsize(480, 540)

		self.button_quit = make_button(self.frame, "종료", 208, 490, "6", "1", self.__del__)
		# self.button_quit = tkinter.Button(self.frame, text='Quit', width=25, command=self.__del__)
		# self.button_quit.pack()
		return self.frame

	def __del__(self):
		self.frame.destroy()


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
	window.title("Call of Duty")
	window.geometry("960x540+" + str(wx) + "+" + str(wy))
	window.resizable(0, 0)
	window.minsize(960, 540)
	window.maxsize(960, 540)
	global_font = font.Font(window, size=14, weight='normal', family='NanumGothic')

	def make_popup_component(newtitle: str):
		component = petron_component(window)

		popup = component.window(newtitle)
		return component, popup

	def make_popup_null(newtitle: str):
		comnull = pet_null(window)
		comnull.open_xml()

		popup = comnull.window(newtitle)
		return comnull, popup

	def make_popup_military():
		get = make_popup("현역 판정 검사 현황")
		# get[0].xml_connect()

		make_button(get[1], "<", 118, 400, "2", "2")
		make_button(get[1], "조회", 218, 400, "4", "2")
		make_button(get[1], ">", 338, 400, "2", "2")
		return get[1]

	def make_popup_milinfo():
		get = make_popup("현역 정보")
		return get[1]

	def make_popup_path():
		global global_font
		get = make_popup("훈련소 가는 길")
		# get[0].xml_connect()

		InputLabel = tkinter.Entry(get[1], font=global_font, width=25, borderwidth=12, relief='flat')
		InputLabel.pack()
		InputLabel.place(x=14, y=96)

		make_button(get[1], "검색", 106, 400, "4", "2")
		make_button(get[1], "조회", 218, 400, "4", "2")
		make_button(get[1], "청소", 338, 400, "4", "2")
		return get[1]

	def make_popup_pubinfo():
		get = make_popup_component("사회 복무 정보")
		get[0].xml_connect("http://apis.data.go.kr/1300000/bmggJeongBo/list",
						   "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D", urllib.parse.quote("경남"))

		check = make_popup_null("공석 조회")


		InputLabel = tkinter.Entry(get[1], font=global_font, width=25, borderwidth=12, relief='flat')
		InputLabel.pack()
		InputLabel.place(x=14, y=96)
		datalist = dict(bjdsgg = [], bokmuGgm = [], dpBokmuGgm = [], jeonhwaNo = [], sbjhjilbyeong = [], gtcdNm = [])
		checklist = dict(bjdsggjusoNm = [], ghjbcNm= [], bmgigwanNm = [], shbmsojipDt = [])


		#datalist_bjdsgg = [] # 지역
		#datalist_bokmuGgm = [] #  복무기관명
		#datalist_dpBokmuGgm = [] # 대표기관명
		#datalist_jeonhwaNo = [] # 전화번호
		#datalist_sbjhjilbyeong = [] # 선발제한질병


		for i in get[0].childbody.iter("item"):
			datalist["bjdsgg"].append("{0}".format(i.findtext("bjdsgg")))
			datalist["bokmuGgm"].append("{0}".format(i.findtext("bokmuGgm")))
			datalist["dpBokmuGgm"].append("{0}".format(i.findtext("dpBokmuGgm")))
			datalist["jeonhwaNo"].append("{0}".format(i.findtext("jeonhwaNo")))
			datalist["sbjhjilbyeong"].append("{0}".format(i.findtext("sbjhjilbyeong")))
			datalist["gtcdNm"].append("{0}".format(i.findtext("gtcdNm")))




		for i in range(0, len(datalist["bjdsgg"])):
			if datalist["gtcdNm"][i] == "서울":
				print("지역 : {0}".format(datalist["bjdsgg"][i]))
				print("복무기관명 : {0}".format(datalist["bokmuGgm"][i]))
				print("대표기관명 : {0}".format(datalist["dpBokmuGgm"][i]))
				print("전화번호 : {0}".format(datalist["jeonhwaNo"][i]))
				print("기피질병 : {0}".format(datalist["sbjhjilbyeong"][i]))#







		make_button(get[1], "검색", 106, 400, "4", "2")
		make_button(get[1], "조회", 218, 400, "4", "2")
		make_button(get[1], "청소", 338, 400, "4", "2")
		return get[1]

	def make_popup_calculator():
		get = make_popup_null("근무 일자 계산")
		InputLabel = tkinter.Entry(get[1], font=global_font, width=25, borderwidth=12, relief='flat')
		InputLabel.pack()
		InputLabel.place(x=14, y=96)

		return get[1]

	Caption = tkinter.Label(window, font=global_font, text="작업")
	Caption.place(x=wx, y=20)

	buttons["military"] = make_button(window, "현역 판정 검사\n현황", 280, 80, "18", "7", make_popup_military)
	buttons["milinfo"] = make_button(window, "현역 정보", 280, 300, "18", "7", make_popup_milinfo)
	buttons["path"] = make_button(window, "훈련소 가는 길", 488, 80, "18", "7", make_popup_path)
	buttons["pubinfo"] = make_button(window, "사회 복무 정보", 488, 300, "18", "7", make_popup_pubinfo)
	buttons["calculator"] = make_button(window, "근무 일자\n계산", 8, 442, "10", "3", make_popup_calculator)

	window.mainloop()


if __name__ == '__main__':
	main()
