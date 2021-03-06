from import_file import *

window = None
buttons = dict()


def main():
	global window, wx, wy, global_font
	window = Tk()
	window.title("Call of Duty")
	wx = 80
	wy = 80

	window.geometry("960x540+%d+%d" % (wx, wy))
	window.bind("<Escape>", lambda self: self.widget.quit())
	window.resizable(0, 0)
	window.minsize(960, 540)
	window.maxsize(960, 540)
	window.configure(background='#ffffff')

	background_image = pimage.open("background.jpg")
	tkpi = timage.PhotoImage(background_image)
	bg = Label(image=tkpi)
	bg.pack()

	day_gabs = [
		31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
	]

	training_spot = [
		"전진", "노도", "백골", "열쇠", "청성", "칠성", "오뚜기", "백마", "화랑", "을지", "승리", "번개", "결전",
		"백두산", "율곡", "철벽", "비룡", "불무리", "이기자", "태풍", "필승", "충장", "백룡", "충경", "백호", "충용",
		"충무", "강철", "전승", "충렬", "봉화", "맹호",
		"육군 입영 훈련소", "해병대 교육 훈련단", "해군 교육 사령부", "공군 교육 사령부"
	]

	window.focus_set()
	global_font = font.Font(window, size=14, weight='normal', family='NanumGothic')

	print(window)

	def make_popup(newtitle: str):
		component = xml_parser(window)

		popup = component.window(newtitle)
		return component, popup

	def make_popup_military():
		get = make_popup("현역 정보")
		get[0].xml_connect("http://apis.data.go.kr/1300000//bjGiJun/list//bjGiJun/list",
		                   "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D",
		                   urllib.parse.quote("경남"))
		listbox = make_listbox(get[1], 0, 5)
		inputbox = make_inputbox(get[1], global_font, 2, 5)
		inputbox.focus_set()
		choosen_at = 0
		result = set()
		data_size_at = 0

		datalist = dict(bjgijunGbnm=[], bjgjsangseNm=[], gunGbnm=[], gsteukgiNm=[], jeopsuSjdtm=[], jeopsuJrdtm=[],
		                bjgijunDgnm=[])

		for i in get[0].childbody.iter("item"):
			datalist["bjgijunGbnm"].append("{0}".format(i.findtext("bjgijunGbnm")))
			datalist["bjgjsangseNm"].append("{0}".format(i.findtext("bjgjsangseNm")))
			datalist["gunGbnm"].append("{0}".format(i.findtext("gunGbnm")))
			datalist["gsteukgiNm"].append("{0}".format(i.findtext("gsteukgiNm")))
			datalist["jeopsuSjdtm"].append("{0}".format(i.findtext("jeopsuSjdtm")))
			datalist["jeopsuJrdtm"].append("{0}".format(i.findtext("jeopsuJrdtm")))
			datalist["bjgijunDgnm"].append("{0}".format(i.findtext("bjgijunDgnm")))  # 몇 개월 복무냐

		data_size_at: int = len(datalist["bjgijunGbnm"])

		def seek():
			clean()
			seekness: str = inputbox.get()
			if seekness != "":
				if str.isdecimal(seekness):  # 전화 번호 검색
					for _i in range(0, data_size_at):
						if seekness in datalist["bjgijunGbnm"][_i]:
							result.add(_i)
				else:
					for _j in range(0, data_size_at):  # 지역 검색
						if seekness in datalist["bjgjsangseNm"][_j]:
							result.add(_j)

					for _k in range(0, data_size_at):  # 지역 검색
						if seekness in datalist["gunGbnm"][_k]:
							result.add(_k)

					for _l in range(0, data_size_at):
						if seekness in datalist["gsteukgiNm"][_l]:
							result.add(_l)

				for _l, item in enumerate(result):
					once_data = datalist["gsteukgiNm"][item] + "<" + datalist["gunGbnm"][item] + ">" + "기간 : " + \
					            datalist["bjgijunDgnm"][item]
					listbox.insert(_l, once_data)

				result.clear()
				inputbox.delete(0, END)

		def view():
			global choosen_at
			choosen_at = listbox.curselection()
			print_detail = Label(get[1], text=datalist["bjgijunDgnm"][choosen_at[0]])
			print_detail.grid(row=6, column=5)
			print_detail = Label(get[1], text=datalist["bjgijunGbnm"][choosen_at[0]])
			print_detail.grid(row=7, column=5)
			print_detail = Label(get[1], text=datalist["bjgjsangseNm"][choosen_at[0]])
			print_detail.grid(row=8, column=5)
			print_detail = Label(get[1], text=datalist["gunGbnm"][choosen_at[0]])
			print_detail.grid(row=9, column=5)
			print_detail = Label(get[1], text=datalist["jeopsuSjdtm"][choosen_at[0]])
			print_detail.grid(row=10, column=5)
			print_detail = Label(get[1], text=datalist["jeopsuJrdtm"][choosen_at[0]])
			print_detail.grid(row=11, column=5)

		def clean():
			global choosen_at
			choosen_at = 0
			listbox.delete(0, END)
			result.clear()

		make_button_grid(get[1], "검색", 12, 4, "4", "2", seek)
		make_button_grid(get[1], "조회", 12, 5, "4", "2", view)
		make_button_grid(get[1], "청소", 12, 6, "4", "2", clean)
		return get[1]

	def make_popup_milinfo():
		get = make_popup("현역 서류")
		get[0].xml_connect("http://apis.data.go.kr/1300000/gbSeoryu/list/gbSeoryu/list"
		                   ,
		                   "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D",
		                   urllib.parse.quote("경남"))
		listbox_txt = make_listbox(get[1], 0, 5)
		inputbox_txt = make_inputbox(get[1], global_font, 2, 5)
		inputbox_txt.focus_set()
		listbox_txt.size()
		choosen_txt = 0
		result_txt = set()
		data_size_txt = 0
		datalist_txt = dict(gsteukgiCd=[], gsteukgiNm=[], jcseoryuNm=[], gunGbnm=[], mjgubun=[])

		for i in get[0].childbody.iter("item"):
			datalist_txt["gsteukgiCd"].append("{0}".format(i.findtext("gsteukgiCd")))
			datalist_txt["gsteukgiNm"].append("{0}".format(i.findtext("gsteukgiNm")))
			datalist_txt["gunGbnm"].append("{0}".format(i.findtext("gunGbnm")))
			datalist_txt["jcseoryuNm"].append("{0}".format(i.findtext("jcseoryuNm")))
			datalist_txt["mjgubun"].append("{0}".format(i.findtext("mjgubun")))

		data_size_txt: int = len(datalist_txt["gsteukgiCd"])

		def seek():
			clean()
			seekness: str = inputbox_txt.get()
			if seekness != "":
				if str.isdecimal(seekness):  # 전화 번호 검색
					for _i in range(0, data_size_txt):
						if seekness in datalist_txt["gsteukgiCd"][_i]:
							result_txt.add(_i)
				else:
					for _j in range(0, data_size_txt):  # 지역 검색
						if seekness in datalist_txt["gsteukgiNm"][_j]:
							result_txt.add(_j)

					for _k in range(0, data_size_txt):  # 지역 검색
						if seekness in datalist_txt["gunGbnm"][_k]:
							result_txt.add(_k)

					for _l in range(0, data_size_txt):
						if seekness in datalist_txt["jcseoryuNm"][_l]:
							result_txt.add(_l)

				for _l, item in enumerate(result_txt):
					once_data = datalist_txt["jcseoryuNm"][item]
					listbox_txt.insert(_l, once_data)

				result_txt.clear()
				inputbox_txt.delete(0, END)

		def view():
			global choosen_txt
			choosen_txt = listbox_txt.curselection()
			webbrowser.open("https://www.google.co.kr/search?q=" + datalist_txt["jcseoryuNm"][choosen_txt[0]])

		def clean():
			global choosen_txt
			choosen_txt = 0
			listbox_txt.delete(0, END)
			result_txt.clear()

		make_button_grid(get[1], "검색", 3, 4, "4", "2", seek)
		make_button_grid(get[1], "조회", 3, 5, "4", "2", view)
		make_button_grid(get[1], "청소", 3, 6, "4", "2", clean)
		return get[1]

	def make_popup_path():
		global global_font
		get = make_popup("훈련소 가는 길")
		listbox = make_listbox(get[1], 0, 5)
		for i, spot in enumerate(training_spot):
			listbox.insert(i, spot)

		def view():
			choose = listbox.curselection()[0] + 47
			webbrowser.open("https://www.mma.go.kr/contents.do?mc=mma00020" + "{0}".format(choose))

		make_button_grid(get[1], "바로가기", 1, 5, "8", "2", view)
		return get[1]

	def make_popup_pubinfo():
		global chosen, global_font
		get = make_popup("사회 복무 정보")
		get[0].xml_connect("http://apis.data.go.kr/1300000/bmggJeongBo/list",
		                   "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D",
		                   urllib.parse.quote("경남"))

		listbox = make_listbox(get[1], 0, 5)
		infobox = make_text(get[1], 1, 5, "20", "10")
		infobox.insert(INSERT, " ")
		infobox.configure(state=DISABLED)
		inputbox = make_inputbox(get[1], global_font, 2, 5)
		inputbox.focus_set()

		chosen = 0
		result = set()
		database = dict(bjdsgg=[], bokmuGgm=[], dpBokmuGgm=[], jeonhwaNo=[], sbjhjilbyeong=[], gtcdNm=[])

		for i in get[0].childbody.iter("item"):
			database["bjdsgg"].append("{0}".format(i.findtext("bjdsgg")))
			database["bokmuGgm"].append("{0}".format(i.findtext("bokmuGgm")))
			database["dpBokmuGgm"].append("{0}".format(i.findtext("dpBokmuGgm")))
			database["jeonhwaNo"].append("{0}".format(i.findtext("jeonhwaNo")))
			database["sbjhjilbyeong"].append("{0}".format(i.findtext("sbjhjilbyeong")))
			database["gtcdNm"].append("{0}".format(i.findtext("gtcdNm")))
		data_size: int = int(len(database["bjdsgg"]))

		for i in range(0, data_size):
			# if database["gtcdNm"][i] == "서울":
			print("지역 : {0}".format(database["bjdsgg"][i]))
			print("복무기관명 : {0}".format(database["bokmuGgm"][i]))
			print("대표기관명 : {0}".format(database["dpBokmuGgm"][i]))
			print("전화번호 : {0}".format(database["jeonhwaNo"][i]))
			print("기피질병 : {0}".format(database["sbjhjilbyeong"][i]))

		def seek():
			global chosen
			result.clear()
			clean()
			seekness: str = inputbox.get()
			if seekness != "":
				if str.isdecimal(seekness):  # 전화 번호 검색
					for _i in range(0, data_size):
						if seekness in database["jeonhwaNo"][_i]:
							result.add(_i)
				else:
					for _j in range(0, data_size):  # 지역 검색
						if seekness in database["bjdsgg"][_j]:
							result.add(_j)

					for _k in range(0, data_size):  # 복무 기관 검색
						if seekness in database["bokmuGgm"][_k]:
							result.add(_k)

				for _l, item in enumerate(result):
					listbox.insert(_l, database["bokmuGgm"][item])
				inputbox.delete(0, END)

		def view():
			if len(result) <= 0:
				return

			global chosen
			chosen = list(result)[listbox.curselection()[0]]

			infobox.configure(state=NORMAL)
			infobox.delete("1.0", END)
			infobox.insert(INSERT, "기관명: [")
			infobox.insert(INSERT, database["bokmuGgm"][chosen])
			infobox.insert(INSERT, "]")
			infobox.insert(INSERT, "\n")
			infobox.insert(INSERT, "주소:")
			infobox.insert(INSERT, database["bjdsgg"][chosen])
			infobox.insert(INSERT, "\n")
			infobox.insert(INSERT, "대표 기관:")
			infobox.insert(INSERT, database["dpBokmuGgm"][chosen])
			infobox.insert(INSERT, "\n")
			infobox.insert(INSERT, "전화 번호:")
			infobox.insert(INSERT, database["jeonhwaNo"][chosen])
			infobox.insert(INSERT, "\n")
			infobox.insert(INSERT, "*기피 질병:")
			infobox.insert(INSERT, database["sbjhjilbyeong"][chosen])
			infobox.insert(INSERT, "\n")
			infobox.configure(state=DISABLED)

		def clean():
			global chosen
			chosen = 0
			infobox.configure(state=NORMAL)
			infobox.delete("1.0", END)
			infobox.configure(state=DISABLED)
			listbox.delete(0, END)

		make_button_grid(get[1], "검색", 3, 4, "4", "2", seek)
		make_button_grid(get[1], "조회", 3, 5, "4", "2", view)
		make_button_grid(get[1], "청소", 3, 6, "4", "2", clean)
		return get[1]

	def make_popup_calculator():
		global global_font

		get = make_popup("근무 일자 계산")
		datebox = []
		Label(get[1], font=global_font, text="년-월-일 순서로 입력해주세요: ", background='#0078D7').grid(row=0, column=4)

		datebox.append(make_inputbox(get[1], global_font, 1, 4))  # 0
		Label(get[1], font=global_font, text="년", background='#0078D7').grid(row=1, column=5)

		datebox.append(make_inputbox(get[1], global_font, 2, 4))  # 1
		Label(get[1], font=global_font, text="월", background='#0078D7').grid(row=2, column=5)

		datebox.append(make_inputbox(get[1], global_font, 3, 4))  # 2
		Label(get[1], font=global_font, text="일 부터 ~ ", background='#0078D7').grid(row=3, column=5)
		Label(get[1], font=global_font, text=" ", background='#0078D7').grid(row=4, column=5)

		datebox.append(make_inputbox(get[1], global_font, 6, 4))  # 3
		Label(get[1], font=global_font, text="21개월 경과: ", background='#0078D7').grid(row=5, column=4)
		Label(get[1], font=global_font, text="년", background='#0078D7').grid(row=6, column=5)
		datebox[3].insert(INSERT, " ")
		datebox[3].configure(state=DISABLED)

		datebox.append(make_inputbox(get[1], global_font, 7, 4))  # 4
		Label(get[1], font=global_font, text="월", background='#0078D7').grid(row=7, column=5)
		datebox[4].insert(INSERT, " ")
		datebox[4].configure(state=DISABLED)

		datebox.append(make_inputbox(get[1], global_font, 8, 4))  # 5
		Label(get[1], font=global_font, text="일 까지", background='#0078D7').grid(row=8, column=5)
		datebox[5].insert(INSERT, " ")
		datebox[5].configure(state=DISABLED)

		def calculate():
			syear_before: str = datebox[0].get()
			smonth_before: str = datebox[1].get()
			sday_before: str = datebox[2].get()
			print(syear_before, smonth_before, sday_before)
			if syear_before == "" or smonth_before == "" or sday_before == "":
				return
			if not syear_before.isdigit() or not smonth_before.isdigit() or not sday_before.isdigit():
				return

			syear: int = int(syear_before)
			smonth: int = int(smonth_before)
			sday: int = int(sday_before)
			if syear <= 0 or smonth <= 0 or smonth > 12 or sday <= 0 or sday > day_gabs[smonth]:
				print(syear, smonth, sday)
				return

			daysum = 0
			dayi = smonth - 1
			daym = 0
			while (True):
				if daym >= 21:
					break

				daysum += day_gabs[dayi]
				dayi += 1
				if dayi > 11:
					dayi = 0
				daym += 1

			begin = datetime.datetime(syear, smonth, sday, 9, 0, 0)
			period = datetime.timedelta(days=daysum)
			end = begin + period

			datebox[3].configure(state=NORMAL)
			datebox[3].delete(0, END)
			datebox[3].insert(INSERT, str(end.year))
			datebox[3].configure(state=DISABLED)

			datebox[4].configure(state=NORMAL)
			datebox[4].delete(0, END)
			datebox[4].insert(INSERT, str(end.month))
			datebox[4].configure(state=DISABLED)

			datebox[5].configure(state=NORMAL)
			datebox[5].delete(0, END)
			datebox[5].insert(INSERT, str(end.day))
			datebox[5].configure(state=DISABLED)

		make_button_grid(get[1], "계산", 9, 5, "4", "2", calculate)

		return get[1]

	Caption = Label(window, font=global_font, text="작업", background='#ffffff')
	Caption.place(x=10, y=20)

	buttons["military"] = make_button(window, "현역 정보", 280, 80, "18", "7", make_popup_military)
	buttons["milinfo"] = make_button(window, "현역 구비서류\n리스트", 280, 300, "18", "7", make_popup_milinfo)
	buttons["path"] = make_button(window, "훈련소 가는 길", 488, 80, "18", "7", make_popup_path)
	buttons["pubinfo"] = make_button(window, "사회 복무 정보", 488, 300, "18", "7", make_popup_pubinfo)
	buttons["calculator"] = make_button(window, "근무 일자\n계산", 8, 442, "10", "3", make_popup_calculator)

	window.mainloop()
