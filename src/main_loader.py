import math
import os
import xml
import xmlrpc
import json

import tkinter

data_alert = []
data_messages = []
data_map_safehouse = []
data_map_safearthshake = []

window = tkinter.Tk()
window.title("Disaster Alert")
window.geometry("960x540+270+135")

window.resizable(0, 0)
window.minsize(960, 540)
window.maxsize(960, 540)
window.mainloop()
