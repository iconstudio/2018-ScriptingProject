import math
import os
import io
import sys
sys.path.append('included_header')
from socket import *
from urllib import *
import urllib.request
from PIL import Image, ImageTk
import folium
import xml
import xmlrpc
import xml.parsers.expat
import json
import pickle

import tkinter
from tkinter import font
from tkinter import messagebox


def start_element(name, attrs):
	print('Start element:', name, attrs)


def char_data(data):
	print('Character data:', repr(data))


# pa = xml.parsers.expat.ParserCreate()
# pa.StartElementHandler = start_element  # 이벤트 핸들러 연결
# pa.CharacterDataHandler = char_data  # 이벤트 핸들러 연결
# pa.Parse("""<?xml version="1.0"?><book ISBN="1111"><title>Loving Python</title></book>""")
"""
HOST = '127.0.0.1'  # localhost
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # -소켓 생성
s.bind((HOST, PORT))
s.listen(1)  # 접속이 있을 때까지 기다림
conn, addr = s.accept()  # 접속을 승인
print('Connected by', addr)
while True:
	data = conn.recv(1024)

	if not data:
		break
	conn.send(data)  # 받은 데이터를 그대로 클라이언트에 전송
conn.close()
"""

# 현재 장면
Scene = 0
data_messages = []

wx = int((1920 - 960) * 0.5)
wy = int((1080 - 540) * 0.5)
window = tkinter.Tk()

window.title("Disaster Alert")
window.geometry("960x540+" + str(wx) + "+" + str(wy))
window.resizable(0, 0)
window.minsize(960, 540)
window.maxsize(960, 540)
Font = font.Font(window, size=12, weight='normal', family='NanumGothic')

image_async = None
try:
	url = "http://tong.visitkorea.or.kr/cms/resource/74/2396274_image2_1.JPG"
	with urllib.request.urlopen(url) as u:
		raw_data = u.read()
	im = Image.open(io.BytesIO(raw_data))
	image_async = ImageTk.PhotoImage(im)
except tkinter.TclError:
	pass

label = tkinter.Label(window, font=Font, text="Test", height=400, width=400)
label.pack()
# label.config(image=image_async)
label.place(x=0, y=0)

Caption = tkinter.Label(window, font=Font, text="의무의 부름", anchor="w")
Caption.pack()
Caption.place(x=20, y=20)

Caption = tkinter.Label(window, font=Font, text="목록")
Caption.place(x=wx, y=20)

button_military = tkinter.Button(window, text="현역 판정검사", command=None)
button_military.pack()
button_military.config(width="18", height="8")
button_military.place(x=480 - 200, y=80)

button_path = tkinter.Button(window, text="훈련소 가는 길", command=None)
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

# map_osm = folium.Map (location = [37.568477, 126.981611],zoom_start=13)
# 마커 지정
# folium.Marker([37.568477, 126.981611], popup='Mt. Hood Meadows').add_to(map_osm)
# html 파일로 저장
# map_osm.save('..\\osm.html')


window.mainloop()
