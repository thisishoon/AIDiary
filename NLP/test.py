﻿import DDiary

diary = DDiary.ddiary() #모델 로드 및 형태소분석기 로드

print("문단을 입력해보세요")
para=input()
print("슬픔, 중립, 행복, 불안, 분노, 예외 리스트입니다.")
response = diary.predict(para)
print(response)