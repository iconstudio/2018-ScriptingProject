import math
import sys
import os
import io

sys.path.append('included_header')
sys.path.append(".idea")

from socket import *
import urllib.request
import urllib.parse
import folium
import json
import pickle
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import xml
import xmlrpc
import xml.parsers.expat
import http.client, http.server

import tkinter
from tkinter import font
from tkinter import messagebox

wx = int((1920 - 960) * 0.5)
wy = int((1080 - 540) * 0.5)
px = int((1920 - 480) * 0.5)
py = int((1080 - 540) * 0.5)


class xml_open:
	def __init__(self):
		print("상속됨")

	def open_xml(self):
		pass


def make_button(hwnd, caption : str, nx : int, ny:int, swidth: str, sheight: str, cmd=None) -> tkinter.Widget:
	newbutton = tkinter.Button(hwnd, background="#CCCCCC", activebackground="#7A7A7A", highlightcolor="#7A7A7A", highlightthickness="2", disabledforeground="#FFFFFF", borderwidth="0", overrelief="flat", relief="flat", text=caption)
	newbutton.pack()
	newbutton.config(width=swidth, height=sheight, justify="center", command=cmd)
	newbutton.place(x=nx, y=ny)
	return newbutton


def component_pack(what: tkinter.Widget):
	what.pack()


def component_hide(what: tkinter.Widget):
	what.pack_forget()


def component_command_set(what: tkinter.Widget, cmd):
	what.config(command=cmd)


def component_name_change(what: tkinter.Widget, how: str):
	what.config(text=how)


def openAPIparse(string, parser = None):
	if parser is None:
		from xml.dom import expatbuilder
		return expatbuilder.parseString(string)
	else:
		from xml.dom import pulldom
		return pulldom.parseString()


class getxml:
	frame = None
	button_quit = None
	xml_url = ""
	xml_pass = ""
	search_key = ""

	def __init__(self, master : 'tkinter.Tk'):
		self.master = master
		self.loopflag = 1
		self.docs = None
		self.doms = None
		self.childbody = None
		self.childhead = None
		self.nextpage = 1
		self.datasize = 1000
		self.pagesize = 100

	def xml_connect(self, url : str, passcode : str, key=""):
		self.xml_url = url
		self.xml_pass = passcode
		self.search_key = key

		# +"&numOfRows=10&pageSize=10&pageNo=1&startPage=1" 이건 나중에 써보고 다시 편집
		try:
			pet_null = urllib.request.Request(self.xml_url + "?serviceKey=" + self.xml_pass
											  + "&numOfRows={0}&pageSize={1}&pageNo={2}&startPage=1".format(self.datasize, self.datasize,
																											self.nextpage))  # 이건 나중에 키 입력을 통해 변경할 수 있도록
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

	def window(self, newtitle: str):
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