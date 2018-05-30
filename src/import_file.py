import math
import os
import io
import sys
sys.path.append('included_header')
from socket import *
import urllib.request
import urllib.parse
from PIL import Image, ImageTk
import folium
import json
import pickle
from xml.dom.minidom import parse, parseString
from xml.etree import cElementTree
import xml
import xmlrpc
import xml.parsers.expat


import tkinter
from tkinter import font
from tkinter import messagebox

wx = int((1920 - 960) * 0.5)
wy = int((1080 - 540) * 0.5)

class xml_open:
    def __init__(self):
        print("상속됨")

    def open_xml(self):
        pass