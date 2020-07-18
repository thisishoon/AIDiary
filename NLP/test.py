import Diary2

print("문단을 입력해보세요")
para=input()
print("슬픔, 중립, 행복, 불안, 분노, 예외 리스트입니다.")
response = Diary2.predict(para)
print(response)

#print(Diary2.predict("너무 슬퍼요"))
