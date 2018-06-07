from import_file import *
import army_loader as army

window = None
buttons = dict()


class petron_component(getxml):

    def __init__(self, master: tkinter.Tk):
        getxml.__init__(self, master)


class pet_null(getxml):

    def __init__(self, master):
        getxml.__init__(self, master)


def buttons_show_all():
    global buttons
    component_pack(buttons["military"])
    component_pack(buttons["milinfo"])
    component_pack(buttons["path"])
    component_pack(buttons["pubinfo"])
    component_pack(buttons["calculator"])


def buttons_hide_all():
    global buttons
    component_hide(buttons["military"])
    component_hide(buttons["milinfo"])
    component_hide(buttons["path"])
    component_hide(buttons["pubinfo"])
    component_hide(buttons["calculator"])


def main():
    global window, wx, wy, global_font
    window = tkinter.Tk()
    window.title("Call of Duty")
    window.geometry("960x540+" + str(wx) + "+" + str(wy))
    window.resizable(0, 0)
    window.minsize(960, 540)
    window.maxsize(960, 540)
    global_font = font.Font(window, size=14, weight='normal', family='NanumGothic')

    print(window)

    def make_component(newtitle: str):
        component = petron_component(window)

        popup = component.window(newtitle)
        return component, popup

    def make_null(newtitle: str):
        comnull = pet_null(window)

        popup = comnull.window(newtitle)
        return comnull, popup

    def make_text(newtitle: str):
        stick = army.army_stick(window)

        popup = stick.window(newtitle)
        return stick, popup

    def make_roll(newtitle: str):
        roll = army.army_roll(window)

        popup = roll.window(newtitle)
        return roll, popup

    def make_popup_military():
        get = make_text("현역 판정 검사 현황")
        get[0].xml_connect("http://apis.data.go.kr/1300000/gbSeoryu/list/gbSeoryu/list",
                           "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D",
                           urllib.parse.quote("경남"))
        datalist = dict(gsteukgiCd=[], gsteukgiNm=[], gunGbnm=[], jcseoryuNm=[], mjbgteukgiNm=[])
        for i in get[0].childbody.iter("item"):
            datalist["gsteukgiCd"].append("{0}".format(i.findtext("gsteukgiCd")))
            datalist["gsteukgiNm"].append("{0}".format(i.findtext("gsteukgiNm")))
            datalist["gunGbnm"].append("{0}".format(i.findtext("gunGbnm")))
            datalist["jcseoryuNm"].append("{0}".format(i.findtext("jcseoryuNm")))

        for i in range(0, len(datalist["gsteukgiCd"])):
            print("군사 특기 코드 : {0}".format(datalist["gsteukgiCd"][i]))
            print("군사 특기명 : {0}".format(datalist["gsteukgiNm"][i])) # 기준1
            print("해당 부서 : {0}".format(datalist["gunGbnm"][i])) #기준2
            print("제출 서류 : {0}".format(datalist["jcseoryuNm"][i]))

        make_button(get[1], "<", 118, 400, "2", "2")
        make_button(get[1], "조회", 218, 400, "4", "2")
        make_button(get[1], ">", 338, 400, "2", "2")
        return get[1]

    def make_popup_milinfo():
        get = make_roll("현역 정보")
        get[0].xml_connect("http://apis.data.go.kr/1300000/gbSeoryu/list/gbSeoryu/list"
                           ,
                           "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D",
                           urllib.parse.quote("경남"))

        make_button(get[1], "<", 118, 400, "2", "2")
        make_button(get[1], "조회", 218, 400, "4", "2")
        make_button(get[1], ">", 338, 400, "2", "2")
        return get[1]

    def make_popup_path():
        global global_font
        get = make_popup("훈련소 가는 길")
        # get[0].xml_connect()

        InputLabel = tkinter.Entry(get[1], font=global_font, width=25, borderwidth=12, relief='flat')
        InputLabel.pack()
        InputLabel.place(x=14, y=96)

        make_button(get[1], "검색", 106, 400, "4", "2")
        make_button(get[1], "조회", 218, 400, "4", "2")
        make_button(get[1], "청소", 338, 400, "4", "2")
        return get[1]

    def make_popup_pubinfo():
        get = make_component("사회 복무 정보")
        get[0].xml_connect("http://apis.data.go.kr/1300000/bmggJeongBo/list",
                           "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D",
                           urllib.parse.quote("경남"))

        check = make_null("공석 조회")
        check[0].xml_connect("http://apis.data.go.kr/1300000/bistGongseok/list/bistGongseok/list",
                             "4954u%2BzYV4y%2F5BRah3wXrxdhkbCaLFoKjzT7dLDNPzn44g%2BUeL30JEGzj2MitqPY9PMyqdb8yW4%2F8eo4xB1xYw%3D%3D",
                             urllib.parse.quote("경남"))

        InputLabel = tkinter.Entry(get[1], font=global_font, width=25, borderwidth=12, relief='flat')
        InputLabel.pack()
        InputLabel.place(x=14, y=96)
        datalist = dict(bjdsgg=[], bokmuGgm=[], dpBokmuGgm=[], jeonhwaNo=[], sbjhjilbyeong=[], gtcdNm=[])
        checklist = dict(bjdsggjusoNm=[], ghjbcNm=[], bmgigwanNm=[], shbmsojipDt=[])

        # datalist_bjdsgg = [] # 지역
        # datalist_bokmuGgm = [] #  복무기관명
        # datalist_dpBokmuGgm = [] # 대표기관명
        # datalist_jeonhwaNo = [] # 전화번호
        # datalist_sbjhjilbyeong = [] # 선발제한질병

        for i in get[0].childbody.iter("item"):
            datalist["bjdsgg"].append("{0}".format(i.findtext("bjdsgg")))
            datalist["bokmuGgm"].append("{0}".format(i.findtext("bokmuGgm")))
            datalist["dpBokmuGgm"].append("{0}".format(i.findtext("dpBokmuGgm")))
            datalist["jeonhwaNo"].append("{0}".format(i.findtext("jeonhwaNo")))
            datalist["sbjhjilbyeong"].append("{0}".format(i.findtext("sbjhjilbyeong")))
            datalist["gtcdNm"].append("{0}".format(i.findtext("gtcdNm")))

        for i in range(0, len(datalist["bjdsgg"])):
            if datalist["gtcdNm"][i] == "서울":
                print("지역 : {0}".format(datalist["bjdsgg"][i]))
                print("복무기관명 : {0}".format(datalist["bokmuGgm"][i]))
                print("대표기관명 : {0}".format(datalist["dpBokmuGgm"][i]))
                print("전화번호 : {0}".format(datalist["jeonhwaNo"][i]))
                print("기피질병 : {0}".format(datalist["sbjhjilbyeong"][i]))

        make_button(get[1], "검색", 106, 400, "4", "2")
        make_button(get[1], "조회", 218, 400, "4", "2")
        make_button(get[1], "청소", 338, 400, "4", "2")
        return get[1]

    def make_popup_calculator():
        get = make_null("근무 일자 계산")
        InputLabel = tkinter.Entry(get[1], font=global_font, width=25, borderwidth=12, relief='flat')
        InputLabel.pack()
        InputLabel.place(x=14, y=96)

        return get[1]

    Caption = tkinter.Label(window, font=global_font, text="작업")
    Caption.place(x=wx, y=20)

    buttons["military"] = make_button(window, "군대 준비 서류\n현황", 280, 80, "18", "7", make_popup_military)
    buttons["milinfo"] = make_button(window, "현역 정보", 280, 300, "18", "7", make_popup_milinfo)
    buttons["path"] = make_button(window, "훈련소 가는 길", 488, 80, "18", "7", make_popup_path)
    buttons["pubinfo"] = make_button(window, "사회 복무 정보", 488, 300, "18", "7", make_popup_pubinfo)
    buttons["calculator"] = make_button(window, "근무 일자\n계산", 8, 442, "10", "3", make_popup_calculator)

    window.mainloop()


if __name__ == '__main__':
    main()
