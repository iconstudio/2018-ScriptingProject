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