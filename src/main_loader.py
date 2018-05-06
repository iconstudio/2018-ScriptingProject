import math
import os
import socket
import xml
import xmlrpc
import xml.parsers.expat
import json

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

Caption = tkinter.Label(window, font=Font, text="현황")
Caption.pack()
Caption.place(x=20)

window.mainloop()


HOST = '127.0.0.1'  # localhost
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 생성
s.bind((HOST, PORT))
s.listen(1)  # 접속이 있을 때까지 기다림
conn, addr = s.accept()  # 접속을 승인
print('Connected by', addr)
while True:
	data = conn.recv(1024)

	if not data:
		break
	conn.send(data) 	 # 받은 데이터를 그대로 클라이언트에 전송
conn.close()

