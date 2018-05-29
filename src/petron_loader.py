from import_file import *



xml_cont_pass = "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D" #복무기관 입력키
xml_cont_endpoint = "http://apis.data.go.kr/1300000/bmggJeongBo"
cont_url = "http://apis.data.go.kr/1300000/bmggJeongBo/list"
pet_loopflag_cont = 1
contdocs = None
cont_dom = None
cont_tet = urllib.parse.quote("경남")

xml_null_pass = "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D" #복무공석 입력키
xml_null_endpoint = "http://apis.data.go.kr/1300000/bistGongseok/list"
null_url = "http://apis.data.go.kr/1300000/bistGongseok/list/bistGongseok/list"
pet_loopflag_null = 1
nulldocs = None
null_dom = None
null_tet = urllib.parse.quote("경남")

def open_null_xml():
	global nulldocs
	global null_dom
	global null_tet
	# +"&numOfRows=10&pageSize=10&pageNo=1&startPage=1" 이건 나중에 써보고 다시 편집
	try:
		pet_null = urllib.request.Request(null_url + "?serviceKey=" + xml_null_pass + "&numOfRows=10&pageSize=10&pageNo=1&startPage=1")

		with urllib.request.urlopen(pet_null) as t:
			raw_data = t.read()
			t.close()
			null_dom = parseString(raw_data)
			print(null_dom.toprettyxml())

	except IOError:
	  print("null_error")
	  return None
	except urllib.error.URLError as e:
		print(e.reason)
		print(parseString(e.read().decode('utf-8')).toprettyxml())
	except urllib.error.HTTPError as e:
		print("error code = " + e.reason)
		print(parseString(e.read().decode('utf-8')).toprettyxml())

def print_null_xml():
	global null_dom
	global nulldocs
	nulldocs = null_dom.childNodes


def open_cont_xml():
	global contdocs
	global cont_dom

	try:
		pet_cont = urllib.request.Request(cont_url + "?serviceKey=" + xml_cont_pass)
		with urllib.request.urlopen(pet_cont) as t:
			raw_data = t.read()
			t.close()
			cont_dom = parseString(raw_data)
			print(cont_dom.toprettyxml())
	except IOError:
	  print("cont_error")
	  return None
	except urllib.error.URLError as e:
		print(e.reason)
		print(parseString(e.read().decode('utf-8')).toprettyxml())
	except urllib.error.HTTPError as e:
		print("error code = " + e.reason)
		print(parseString(e.read().decode('utf-8')).toprettyxml())



wx = int((1920 - 960) * 0.5)
wy = int((1080 - 540) * 0.5)
petronwindow = tkinter.Tk()
petronwindow.title("Petron_window")
petronwindow.geometry("960x540+" + str(wx) + "+" + str(wy))
petronwindow.resizable(0, 0)
petronwindow.minsize(960, 540)
petronwindow.maxsize(960, 540)
Font = font.Font(petronwindow, size=12, weight='normal', family='NanumGothic')


open_null_xml()
print_null_xml()
open_cont_xml()

Caption = tkinter.Label(petronwindow, font=Font, text="목록")
Caption.place(x=wx, y=20)

button_military = tkinter.Button(petronwindow, text="공석 확인", command=None)
button_military.pack()
button_military.config(width="18", height="8")
button_military.place(x=480 - 200, y=80)

button_path = tkinter.Button(petronwindow, text="사회복무 회사 검색", command=None)
button_path.pack()
button_path.config(width="18", height="8")
button_path.place(x=480 + 8, y=80)

button_milinfo = tkinter.Button(petronwindow, text="현역 정보", command=None)
button_milinfo.pack()
button_milinfo.config(width="18", height="8")
button_milinfo.place(x=480 - 200, y=300)

button_pubinfo = tkinter.Button(petronwindow, text="사회복무 정보", command=None)
button_pubinfo.pack()
button_pubinfo.config(width="18", height="8")
button_pubinfo.place(x=480 + 8, y=300)


petronwindow.mainloop()




