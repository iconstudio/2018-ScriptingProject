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

		for x in range(1, 6):
			print(x, '*', x, '=', str(x * x).zfill(3))

		dic = {"item": "apple", "color": "red"}
		print("{0[item]} is {0[color]}".format(dic))

		item = "apple"
		_할로 = "red"
		print("{0[item]} is {0[_할로]}".format(locals()))
		print("{0:c}".format(66))
		print("{0:.4f}".format(1 / 3 * 3))

		# with open('test.txt') as f:  # with 코드블록 as는 파일 핸들 지정
		#    print(f.readlines())
		# print(f.closed)

		colors = ['red', 'green', 'black']
		f = open('file_colors', 'wb')  # pickle 을 위해 바이너리 쓰기 파일 오픈
		pickle.dump(colors, f)  # colors 리스트를 file_colors로 dump
		f.close()
		del colors


		class SuperTest:
			pass

		class Test(SuperTest):
			var1 = 0
			var2 = "43571aa826aa439912"
			var3 = 2397034024519028

		a = Test()

		f = open('file_Test', 'wb')
		pickle.dump(a, f)
		f.close()
		del a

		f = open('file_Test', 'rb')  # pickle을 위해 바이너리 읽기 파일 오픈
		a = pickle.load(f)  # 파일에서 리스트 load
		f.close()
		print(a)
		print(f.closed)
		print(a.var1)
		print(a.var2)
		print(a.var3)

	else:
		raise RuntimeError
except RuntimeError:
	print("Program must be run by Main.")
