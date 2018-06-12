import math
import sys
import os
import io

sys.path.append('included_header')
sys.path.append(".idea")

import webbrowser
import urllib.request
import urllib.parse
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import xml
import xmlrpc
import xml.parsers.expat
import http.client, http.server

from PIL import Image, ImageTk
import tkinter
from tkinter import *
from tkinter import font

def make_button(hwnd, caption: str, nx: int, ny: int, swidth: str, sheight: str, cmd=None) -> Button:
	newbutton = Button(hwnd, background="#CCCCCC", activebackground="#7A7A7A", highlightcolor="#7A7A7A",
	                   highlightthickness="2", disabledforeground="#FFFFFF", borderwidth="0", overrelief="flat",
	                   relief="flat", text=caption)
	newbutton.pack()
	newbutton.config(width=swidth, height=sheight, justify="center", command=cmd)
	newbutton.place(x=nx, y=ny)
	return newbutton


def make_button_grid(hwnd, caption: str, r: int, c: int, swidth: str, sheight: str, cmd=None) -> Button:
	newbutton = Button(hwnd, background="#CCCCCC", activebackground="#7A7A7A", highlightcolor="#7A7A7A",
	                   highlightthickness="2", disabledforeground="#FFFFFF", borderwidth="0", overrelief="flat",
	                   relief="flat", text=caption)
	newbutton.config(width=swidth, height=sheight, justify="center", command=cmd)
	newbutton.grid(row=r, column=c, pady=4, padx=4)
	return newbutton


def make_listbox(hwnd, r: int, c: int) -> Listbox:
	scrollbar = Scrollbar(hwnd)
	scrollbar.grid(row=r, column=c + 1, padx=0, sticky=N + S)

	listbox = Listbox(hwnd, borderwidth="0", relief="flat", activestyle='none', yscrollcommand=scrollbar.set)
	listbox.grid(row=r, column=c, padx=0)
	scrollbar.config(command=listbox.yview)

	return listbox


def openAPIparse(string, parser=None):
	if parser is None:
		from xml.dom import expatbuilder
		return expatbuilder.parseString(string)
	else:
		from xml.dom import pulldom
		return pulldom.parseString()


class xml_parser:
	frame = None
	button_quit = None
	xml_url = ""
	xml_pass = ""
	search_key = ""

	def __init__(self, master: Tk):
		self.master = master
		self.loopflag = 1
		self.docs = None
		self.doms = None
		self.childbody = None
		self.childhead = None
		self.nextpage = 1
		self.datasize = 1000
		self.pagesize = 100

	def xml_connect(self, url: str, passcode: str, key="", page: int = 0):
		self.xml_url = url
		self.xml_pass = passcode
		self.search_key = key

		try:
			pet_null = urllib.request.Request(self.xml_url + "?serviceKey=" + self.xml_pass
			                                  + "&numOfRows={0}&pageSize={1}&pageNo={2}&startPage=1".format(
				self.datasize, page,
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

	def window(self, newtitle: str) -> Toplevel:
		self.frame = Toplevel(self.master)
		self.frame.title(newtitle)
		self.frame.geometry("600x540+%d+%d" % (80, 80))
		self.frame.resizable(0, 0)
		self.frame.minsize(600, 540)

		self.button_quit = make_button_grid(self.frame, "종료", 5, 5, "8", "2", self.__del__).grid(sticky=W + E,
		                                                                                         pady=10)
		return self.frame

	def __del__(self):
		self.frame.destroy()
