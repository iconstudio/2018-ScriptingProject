import math
import os
import io

import socket
import urllib
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


pa = xml.parsers.expat.ParserCreate()
pa.StartElementHandler = start_element  # 이벤트 핸들러 연결
pa.CharacterDataHandler = char_data  # 이벤트 핸들러 연결
pa.Parse("""<?xml version="1.0"?><book ISBN="1111"><title>Loving Python</title></book>""")
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

data_alert = []
data_messages = []
data_map_safehouse = []
data_map_safearthshake = []

wx = 0  # int((1920 - 960))
window = tkinter.Tk()

window.title("Disaster Alert")
window.geometry("960x540+" + str(wx) + "+60")
window.resizable(0, 0)
window.minsize(960, 540)
window.maxsize(960, 540)
Font = font.Font(window, size=12, weight='normal', family='NanumGothic')

url = "http://tong.visitkorea.or.kr/cms/resource/74/2396274_image2_1.JPG"
with urllib.request.urlopen(url) as u:
	raw_data = u.read()
im = Image.open(io.BytesIO(raw_data))
image = ImageTk.PhotoImage(im)

label = tkinter.Label(window, image=image, height=400, width=400)
label.pack()
label.place(x=0, y=0)

Caption = tkinter.Label(window, font=Font, text="현황")
Caption.pack()
Caption.place(x=20) 

map_osm = folium.Map (location = [37.568477, 126.981611],zoom_start=13)
# 마커 지정
folium.Marker([37.568477, 126.981611], popup='Mt. Hood Meadows').add_to(map_osm)
# html 파일로 저장
map_osm.save('..\\osm.html')


window.mainloop()
