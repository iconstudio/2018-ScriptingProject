from import_file import *

window = None
buttons = dict()


def main():
    global window, wx, wy, global_font
    window = Tk()
    window.title("Call of Duty")
    wx = 80
    wy = 80

    window.geometry("960x540+%d+%d" % (wx, wy))
    window.bind("<Escape>", lambda self: self.widget.quit())
    window.resizable(0, 0)
    window.minsize(960, 540)
    window.maxsize(960, 540)
    window.configure(background='#ffffff')

    background_image = pimage.open("background.jpg")
    tkpi = timage.PhotoImage(background_image)
    bg = Label(image=tkpi)
    bg.pack()

    training_spot = [
        "전진", "노도", "백골", "열쇠", "청성", "칠성", "오뚜기", "백마", "화랑", "을지", "승리", "번개", "결전",
        "백두산", "율곡", "철벽", "비룡", "불무리", "이기자", "태풍", "필승", "충장", "백룡", "충경", "백호", "충용",
        "충무", "강철", "전승", "충렬", "봉화", "맹호",
        "육군 입영 훈련소", "해병대 교육 훈련단", "해군 교육 사령부", "공군 교육 사령부"
    ]

    window.focus_set()
    global_font = font.Font(window, size=14, weight='normal', family='NanumGothic')

    print(window)

    def make_popup(newtitle: str):
        component = xml_parser(window)

        popup = component.window(newtitle)
        return component, popup

    def make_popup_military():
        get = make_popup("현역 정보")
        get[0].xml_connect("http://apis.data.go.kr/1300000//bjGiJun/list//bjGiJun/list",
                           "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D",
                           urllib.parse.quote("경남"))
        listbox = make_listbox(get[1], 0, 5)
        infobox = make_text(get[1], 1, 5, "20", "10").configure(state='disabled')
        inputbox = make_inputbox(get[1], global_font, 2, 5)
        inputbox.focus_set()
        choosen_at = 0
        result = set()
        data_size_at = 0

        datalist = dict(bjgijunGbnm=[], bjgjsangseNm=[], gunGbnm=[], gsteukgiNm=[], jeopsuSjdtm=[])

        for i in get[0].childbody.iter("item"):
            datalist["bjgijunGbnm"].append("{0}".format(i.findtext("bjgijunGbnm")))
            datalist["bjgjsangseNm"].append("{0}".format(i.findtext("bjgjsangseNm")))
            datalist["gunGbnm"].append("{0}".format(i.findtext("gunGbnm")))
            datalist["gsteukgiNm"].append("{0}".format(i.findtext("gsteukgiNm")))
            datalist["jeopsuSjdtm"].append("{0}".format(i.findtext("jeopsuSjdtm")))

        data_size_at : int = len(datalist["bjgijunGbnm"])

        def seek():
            clean()
            seekness: str = inputbox.get()
            if seekness != "":
                if str.isdecimal(seekness):  # 전화 번호 검색
                    for _i in range(0, data_size_at):
                        if seekness in datalist["bjgijunGbnm"][_i]:
                            result.add(_i)
                else:
                    for _j in range(0, data_size_at):  # 지역 검색
                        if seekness in datalist["bjgjsangseNm"][_j]:
                            result.add(_j)

                    for _k in range(0, data_size_at):  # 지역 검색
                        if seekness in datalist["gunGbnm"][_k]:
                            result.add(_k)

                    for _l in range(0, data_size_at):
                        if seekness in datalist["gsteukgiNm"][_l]:
                            result.add(_l)


                for _l, item in enumerate(result):
                    once_data = datalist["gsteukgiNm"][item] + "<" + datalist["gunGbnm"][item] + ">"
                    listbox.insert(_l, once_data)

                result.clear()
                inputbox.delete(0, END)

        def view():
            global choosen_at
            choosen_at = listbox.curselection()

        def clean():
            global choosen_at
            choosen_at = 0
            listbox.delete(0, END)
            result.clear()

        make_button_grid(get[1], "검색", 6, 4, "4", "2", seek)
        make_button_grid(get[1], "조회", 6, 5, "4", "2", view)
        make_button_grid(get[1], "청소", 6, 6, "4", "2", clean)
        return get[1]

    def make_popup_milinfo():
        get = make_popup("현역 서류")
        get[0].xml_connect("http://apis.data.go.kr/1300000/gbSeoryu/list/gbSeoryu/list"
                           ,
                           "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D",
                           urllib.parse.quote("경남"))
        listbox_txt = make_listbox(get[1], 0, 5)
        inputbox_txt = make_inputbox(get[1], global_font, 2, 5)
        inputbox_txt.focus_set()
        listbox_txt.size()
        choosen_txt = 0
        result_txt = set()
        data_size_txt = 0
        datalist_txt = dict(gsteukgiCd = [], gsteukgiNm = [], jcseoryuNm = [], gunGbnm = [], mjgubun = [])

        for i in get[0].childbody.iter("item"):
            datalist_txt["gsteukgiCd"].append("{0}".format(i.findtext("gsteukgiCd")))
            datalist_txt["gsteukgiNm"].append("{0}".format(i.findtext("gsteukgiNm")))
            datalist_txt["gunGbnm"].append("{0}".format(i.findtext("gunGbnm")))
            datalist_txt["jcseoryuNm"].append("{0}".format(i.findtext("jcseoryuNm")))
            datalist_txt["mjgubun"].append("{0}".format(i.findtext("mjgubun")))


        data_size_txt : int = len(datalist_txt["gsteukgiCd"])
        def seek():
            clean()
            seekness: str = inputbox_txt.get()
            if seekness != "":
                if str.isdecimal(seekness):  # 전화 번호 검색
                    for _i in range(0, data_size_txt):
                        if seekness in datalist_txt["gsteukgiCd"][_i]:
                            result_txt.add(_i)
                else:
                    for _j in range(0, data_size_txt):  # 지역 검색
                        if seekness in datalist_txt["gsteukgiNm"][_j]:
                            result_txt.add(_j)

                    for _k in range(0, data_size_txt):  # 지역 검색
                        if seekness in datalist_txt["gunGbnm"][_k]:
                            result_txt.add(_k)

                    for _l in range(0, data_size_txt):
                        if seekness in datalist_txt["jcseoryuNm"][_l]:
                            result_txt.add(_l)


                for _l, item in enumerate(result_txt):
                    once_data = datalist_txt["jcseoryuNm"][item]
                    listbox_txt.insert(_l, once_data)

                result_txt.clear()
                inputbox_txt.delete(0, END)
        def view():
            global choosen_txt
            choosen_txt = listbox_txt.curselection()
            webbrowser.open("https://www.google.co.kr/search?q=" +datalist_txt["jcseoryuNm"][choosen_txt[0]] )

        def clean():
            global choosen_txt
            choosen_txt = 0
            listbox_txt.delete(0, END)
            result_txt.clear()


        make_button_grid(get[1], "검색", 3, 4, "4", "2", seek)
        make_button_grid(get[1], "조회", 3, 5, "4", "2", view)
        make_button_grid(get[1], "청소", 3, 6, "4", "2", clean)
        return get[1]

    def make_popup_path():
        global global_font
        get = make_popup("훈련소 가는 길")
        listbox = make_listbox(get[1], 0, 5)
        for i, spot in enumerate(training_spot):
            listbox.insert(i, spot)

        def view():
            choose = listbox.curselection()[0] + 47
            webbrowser.open("https://www.mma.go.kr/contents.do?mc=mma00020" + "{0}".format(choose))

        make_button_grid(get[1], "바로가기", 1, 5, "8", "2", view)
        return get[1]

    def make_popup_pubinfo():
        global choosen, global_font
        get = make_popup("사회 복무 정보")
        get[0].xml_connect("http://apis.data.go.kr/1300000/bmggJeongBo/list",
                           "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D",
                           urllib.parse.quote("경남"))

        listbox = make_listbox(get[1], 0, 5)
        infobox = make_text(get[1], 1, 5, "20", "10").configure(state='disabled')
        inputbox = make_inputbox(get[1], global_font, 2, 5)
        inputbox.focus_set()

        chosen = 0
        result = set()
        database = dict(bjdsgg=[], bokmuGgm=[], dpBokmuGgm=[], jeonhwaNo=[], sbjhjilbyeong=[], gtcdNm=[], bjgjsangseNm = [])

        for i in get[0].childbody.iter("item"):
            database["bjdsgg"].append("{0}".format(i.findtext("bjdsgg")))
            database["bokmuGgm"].append("{0}".format(i.findtext("bokmuGgm")))
            database["dpBokmuGgm"].append("{0}".format(i.findtext("dpBokmuGgm")))
            database["jeonhwaNo"].append("{0}".format(i.findtext("jeonhwaNo")))
            database["sbjhjilbyeong"].append("{0}".format(i.findtext("sbjhjilbyeong")))
            database["gtcdNm"].append("{0}".format(i.findtext("gtcdNm")))
            database["bjgjsangseNm"].append("{0}".format(i.findtext("bjgjsangseNm")))
        data_size: int = int(len(database["bjdsgg"]))

        for i in range(0, data_size):
            # if database["gtcdNm"][i] == "서울":
            print("지역 : {0}".format(database["bjdsgg"][i]))
            print("복무기관명 : {0}".format(database["bokmuGgm"][i]))
            print("대표기관명 : {0}".format(database["dpBokmuGgm"][i]))
            print("전화번호 : {0}".format(database["jeonhwaNo"][i]))
            print("기피질병 : {0}".format(database["sbjhjilbyeong"][i]))

        def seek():
            clean()
            seekness: str = inputbox.get()
            #if seekness != "":
            if str.isdecimal(seekness):  # 전화 번호 검색
                for _i in range(0, data_size):
                    if seekness in database["jeonhwaNo"][_i]:
                        result.add(_i)
            else:
                for _j in range(0, data_size):  # 지역 검색
                    if seekness in database["bjdsgg"][_j]:
                        result.add(_j)

                for _k in range(0, data_size):  # 복무 기관 검색
                    if seekness in database["bokmuGgm"][_k]:
                        result.add(_k)

            for _l, item in enumerate(result):
                listbox.insert(_l, database["bokmuGgm"][item])

            result.clear()
            inputbox.delete(0, END)

        def view():
            global chosen
            chosen = listbox.curselection()

            infobox.configure(state=NORMAL)
            infobox.delete("1.0", END)
            infobox.insert(INSERT, "기관명: [")
            infobox.insert(INSERT, database["bokmuGgm"][chosen])
            infobox.insert(INSERT, "]")
            infobox.insert(INSERT, "\n")
            infobox.insert(INSERT, "주소:")
            infobox.insert(INSERT, database["bjdsgg"][chosen])
            infobox.insert(INSERT, "\n")
            infobox.insert(INSERT, "대표 기관:")
            infobox.insert(INSERT, database["dpBokmuGgm"][chosen])
            infobox.insert(INSERT, "\n")
            infobox.insert(INSERT, "전화 번호:")
            infobox.insert(INSERT, database["jeonhwaNo"][chosen])
            infobox.insert(INSERT, "\n")
            infobox.insert(INSERT, "*기피 질병:")
            infobox.insert(INSERT, database["sbjhjilbyeong"][chosen])
            infobox.insert(INSERT, "\n")
            infobox.configure(state=DISABLED)

        def clean():
            global chosen
            chosen = 0
            listbox.delete(0, END)
            result.clear()

        make_button_grid(get[1], "검색", 3, 4, "4", "2", seek)
        make_button_grid(get[1], "조회", 3, 5, "4", "2", view)
        make_button_grid(get[1], "청소", 3, 6, "4", "2", clean)
        return get[1]

    def make_popup_calculator():
        get = make_popup("근무 일자 계산")
        InputLabel = Entry(get[1], font=global_font, width=25, borderwidth=12, relief='flat')
        InputLabel.pack()
        InputLabel.place(x=14, y=96)

        return get[1]

    Caption = Label(window, font=global_font, text="작업", background='#ffffff')
    Caption.place(x=10, y=20)

    buttons["military"] = make_button(window, "현역 정보", 280, 80, "18", "7", make_popup_military)
    buttons["milinfo"] = make_button(window, "현역 구비서류\n리스트", 280,300, "18", "7", make_popup_milinfo)
    buttons["path"] = make_button(window, "훈련소 가는 길", 488, 80, "18", "7", make_popup_path)
    buttons["pubinfo"] = make_button(window, "사회 복무 정보", 488, 300, "18", "7", make_popup_pubinfo)
    buttons["calculator"] = make_button(window, "근무 일자\n계산", 8, 442, "10", "3", make_popup_calculator)

    window.mainloop()


if __name__ == '__main__':
    main()
