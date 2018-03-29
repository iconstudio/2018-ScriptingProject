import main_loader

'''
        저작자: 진윤성
        용도:   재난 상황 표시 프로그램
        기능:   1. 재난 대피소 / 지진 대피소 위치 표시
                2. 재난 알림 현황 보기
                3. 재난 피해 현황 보기
        필요 컴포넌트:
                페이지
                그림
                버튼
                목록
                라벨

        흐름:
                페이지 0 (주)
                    넓직한 타일 버튼 (재난 알림, 재난 피해)
                                     (재난 대피소, 지진 대피소)
                        미리 XML 자료를 받아와서 무언가 존재하면 느낌표를 띄운다.
                        만약 최근 자료가 없다면 버튼을 비활성화 한다.
                    종료 버튼
                    제작자 표시 버튼
                페이지 1 (알림 현황)
                    재난 알림 그림
                    뒤로가기 버튼
                페이지 2 (재난 피해 현황)
                    재난 피해 그림
                    뒤로가기 버튼
                페이지 3 (재난 대피소 지도)
                    지도
                    뒤로가기 버튼
                페이지 4 (지진 대피소 지도)
                    지도
                    뒤로가기 버튼
'''

try:
    if __name__ == "__main__":
        print("begins")
        main_loader.initialize()
    else:
        raise RuntimeError
except RuntimeError:
    print("Program must be run by Main.")
