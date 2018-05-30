from main_loader import *

'''
        저작자: 
        용도:   
        기능:   1. 
        필요 컴포넌트:
                페이지
                그림
                버튼
                목록
                라벨

        흐름:
                페이지 0 (주)
                    넓직한 타일 버튼

                    종료 버튼
                    제작자 표시 버튼
                페이지 1

                    뒤로가기 버튼
                페이지 2
                    지도
                    뒤로가기 버튼
                페이지 3

                    뒤로가기 버튼
                페이지 4

                    뒤로가기 버튼
'''

try:
	if __name__ == "__main__":
		print("begins")
	else:
		raise RuntimeError
except RuntimeError:
	print("Program must be run by Main.")
