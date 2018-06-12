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
		get[0].xml_connect("http://apis.data.go.kr/1300000/gbSeoryu/list/gbSeoryu/list",
		                   "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D",
		                   urllib.parse.quote("경남"))

		InputLabel = Entry(get[1], font=global_font, width=25, borderwidth=12, relief='flat')
		InputLabel.grid(row=0, column=5)

		datalist = dict(gsteukgiCd=[], gsteukgiNm=[], gunGbnm=[], jcseoryuNm=[], mjbgteukgiNm=[])
		for i in get[0].childbody.iter("item"):
			datalist["gsteukgiCd"].append("{0}".format(i.findtext("gsteukgiCd")))
			datalist["gsteukgiNm"].append("{0}".format(i.findtext("gsteukgiNm")))
			datalist["gunGbnm"].append("{0}".format(i.findtext("gunGbnm")))
			datalist["jcseoryuNm"].append("{0}".format(i.findtext("jcseoryuNm")))

		for i in range(0, len(datalist["gsteukgiCd"])):
			print("군사 특기 코드 : {0}".format(datalist["gsteukgiCd"][i]))
			print("군사 특기명 : {0}".format(datalist["gsteukgiNm"][i]))  # 기준1
			print("해당 부서 : {0}".format(datalist["gunGbnm"][i]))  # 기준2
			print("제출 서류 : {0}".format(datalist["jcseoryuNm"][i]))

		make_button_grid(get[1], "<", 1, 4, "2", "2")
		make_button_grid(get[1], "조회", 1, 5, "4", "2")
		make_button_grid(get[1], ">", 1, 6, "2", "2")
		return get[1]

	def make_popup_milinfo():
		get = make_popup("현역 서류")
		get[0].xml_connect("http://apis.data.go.kr/1300000/gbSeoryu/list/gbSeoryu/list"
		                   ,
		                   "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D",
		                   urllib.parse.quote("경남"))

		make_button_grid(get[1], "<", 1, 4, "2", "2")
		make_button_grid(get[1], "조회", 1, 5, "4", "2")
		make_button_grid(get[1], ">", 1, 6, "2", "2")
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
			clean()
			result.clear()
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
			infobox.delete("0.0", END)
			infobox.configure(state=DISABLED)
			listbox.delete(0, END)

		make_button_grid(get[1], "검색", 3, 4, "4", "2", seek)
		make_button_grid(get[1], "조회", 3, 5, "4", "2", view)
		make_button_grid(get[1], "청소", 3, 6, "4", "2", clean)
		return get[1]

	def make_popup_calculator():
		get = make_popup("근무 일자 계산")
		InputLabel = Entry(get[1], font=global_font, width=25, borderwidth=12, relief='flat')
		InputLabel.pack()
		InputLabel.place(x=14, y=96)

		return get[1]

	Caption = Label(window, font=global_font, text="작업", background='#ffffff')
	Caption.place(x=10, y=20)

	buttons["military"] = make_button(window, "현역 정보", 280, 80, "18", "7", make_popup_military)
	buttons["milinfo"] = make_button(window, "현역 구비서류", 280, 300, "18", "7", make_popup_milinfo)
	buttons["path"] = make_button(window, "훈련소 가는 길", 488, 80, "18", "7", make_popup_path)
	buttons["pubinfo"] = make_button(window, "사회 복무 정보", 488, 300, "18", "7", make_popup_pubinfo)
	buttons["calculator"] = make_button(window, "근무 일자\n계산", 8, 442, "10", "3", make_popup_calculator)

	window.mainloop()


if __name__ == '__main__':
	main()
