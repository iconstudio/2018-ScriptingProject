import math
import os
import xml
import xmlrpc
import json

import tkinter
from tkinter import font
from tkinter import messagebox

data_alert = []
data_messages = []
data_map_safehouse = []
data_map_safearthshake = []

wx = 0#int((1920 - 960))
window = tkinter.Tk()

window.title("Disaster Alert")
window.geometry("960x540+" + str(wx) + "+60")
window.resizable(0, 0)
window.minsize(960, 540)
window.maxsize(960, 540)
Font = font.Font(window, size=12, weight='normal', family='NanumGothic')

Caption = tkinter.Label(window, font = Font, text="현황")
Caption.pack()
Caption.place(x=20)

window.mainloop()
