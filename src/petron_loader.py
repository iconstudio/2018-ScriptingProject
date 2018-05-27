from import_file import *

xml_cont_pass = "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D" #복무기관 입력키
xml_cont_endpoint = "http://apis.data.go.kr/1300000/bmggJeongBo"
cont_url = "http://apis.data.go.kr/1300000/bmggJeongBo"
xml_null_pass = "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D" #복무공석 입력키
xml_null_endpoint = "http://apis.data.go.kr/1300000/bistGongseok/list"
null_url = "http://apis.data.go.kr/1300000/bistGongseok/list"

pet_loopflag_cont = 1
pet_xmlFD_cont = -1		#XML문서 파일 디스크립터
pet_BooksDoc_cont = None

pet_loopflag_cont = 1
pet_xmlFD_cont = -1		#XML문서 파일 디스크립터
pet_BooksDoc_cont = None

entext = urllib.parse.quote("파이썬")

wx = int((1920 - 960) * 0.5)
wy = int((1080 - 540) * 0.5)
petronwindow = tkinter.Tk()
petronwindow.title("Petron_window")
petronwindow.geometry("960x540+" + str(wx) + "+" + str(wy))
petronwindow.resizable(0, 0)
petronwindow.minsize(960, 540)
petronwindow.maxsize(960, 540)
Font = font.Font(petronwindow, size=12, weight='normal', family='NanumGothic')

try:
	pet = "http://apis.data.go.kr/1300000/bmggJeongBo/list?serviceKey="+xml_cont_pass +"&numOfRows=10&pageSize=10&pageNo=1&startPage=1"

	with urllib.request.urlopen(pet) as u:
		raw_data = u.read()
		print(u.info())

	#im = Image.open(io.BytesIO(raw_data))
	#image_async = ImageTk.PhotoImage(im)
except tkinter.TclError:
	print("happen")
#


Caption = tkinter.Label(petronwindow, font=Font, text="목록")
Caption.place(x=wx, y=20)

button_military = tkinter.Button(petronwindow, text="현역 판정검사", command=None)
button_military.pack()
button_military.config(width="18", height="8")
button_military.place(x=480 - 200, y=80)

button_path = tkinter.Button(petronwindow, text="훈련소 가는 길", command=None)
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




